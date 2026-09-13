
-- F09 Gym Membership Retention Analysis | SQLite
-- Reporting cutoff: 2026-07-31. One row per member unless stated otherwise.

-- 01 Executive retention metrics
SELECT COUNT(*) AS members_joined,
       SUM(status='Active') AS active_members,
       SUM(status='Cancelled') AS cancelled_members,
       ROUND(100.0*SUM(status='Cancelled')/COUNT(*),1) AS observed_churn_pct
FROM members;

-- 02 Monthly active base, joins, and cancellations
WITH months AS (SELECT DISTINCT month_end FROM membership_monthly)
SELECT m.month_end, SUM(mm.active_flag) AS active_members,
       (SELECT COUNT(*) FROM members x WHERE substr(x.join_date,1,7)=substr(m.month_end,1,7)) AS joins,
       (SELECT COUNT(*) FROM members x WHERE substr(x.cancel_date,1,7)=substr(m.month_end,1,7)) AS cancellations
FROM months m JOIN membership_monthly mm USING(month_end)
GROUP BY m.month_end ORDER BY m.month_end;

-- 03 Join-month cohort retention at 3, 6 and 12 months (mature cohorts only)
WITH base AS (
 SELECT member_id, substr(join_date,1,7) cohort_month, join_date, cancel_date,
        CAST((julianday('2026-07-31')-julianday(join_date))/30.44 AS INT) observed_months
 FROM members
)
SELECT cohort_month, COUNT(*) cohort_size,
 ROUND(100.0*SUM(CASE WHEN observed_months>=3 AND (cancel_date IS NULL OR julianday(cancel_date)-julianday(join_date)>=91) THEN 1 ELSE 0 END)/NULLIF(SUM(observed_months>=3),0),1) retention_3m_pct,
 ROUND(100.0*SUM(CASE WHEN observed_months>=6 AND (cancel_date IS NULL OR julianday(cancel_date)-julianday(join_date)>=183) THEN 1 ELSE 0 END)/NULLIF(SUM(observed_months>=6),0),1) retention_6m_pct,
 ROUND(100.0*SUM(CASE WHEN observed_months>=12 AND (cancel_date IS NULL OR julianday(cancel_date)-julianday(join_date)>=365) THEN 1 ELSE 0 END)/NULLIF(SUM(observed_months>=12),0),1) retention_12m_pct
FROM base GROUP BY cohort_month ORDER BY cohort_month;

-- 04 Retention performance by plan
SELECT p.plan_name, COUNT(*) members, SUM(m.status='Active') active_members,
 ROUND(100.0*SUM(m.status='Active')/COUNT(*),1) active_share_pct,
 ROUND(AVG(CASE WHEN m.cancel_date IS NOT NULL THEN julianday(m.cancel_date)-julianday(m.join_date) END),0) avg_days_to_churn
FROM members m JOIN plans p USING(plan_id) GROUP BY p.plan_id ORDER BY active_share_pct DESC;

-- 05 Retention performance by location
SELECT l.location_name, COUNT(*) members, SUM(m.status='Active') active_members,
 ROUND(100.0*SUM(m.status='Cancelled')/COUNT(*),1) observed_churn_pct
FROM members m JOIN locations l USING(location_id) GROUP BY l.location_id ORDER BY observed_churn_pct DESC;

-- 06 Acquisition-channel quality
SELECT acquisition_channel, COUNT(*) members, SUM(status='Active') active_members,
 ROUND(100.0*SUM(status='Active')/COUNT(*),1) active_share_pct
FROM members GROUP BY acquisition_channel ORDER BY active_share_pct DESC;

-- 07 Attendance engagement bands and churn
WITH c AS (
 SELECT m.member_id,m.status,COUNT(ch.checkin_id)*30.44/NULLIF(MIN(julianday(COALESCE(m.cancel_date,'2026-07-31'))-julianday(m.join_date)+1,730),0) visits_per_30d
 FROM members m LEFT JOIN checkins ch ON ch.member_id=m.member_id GROUP BY m.member_id
), b AS (
 SELECT *, CASE WHEN visits_per_30d<2 THEN '0-1 visits' WHEN visits_per_30d<5 THEN '2-4 visits' WHEN visits_per_30d<9 THEN '5-8 visits' ELSE '9+ visits' END engagement_band FROM c
)
SELECT engagement_band,COUNT(*) members,ROUND(AVG(visits_per_30d),1) avg_monthly_visits,
 ROUND(100.0*SUM(status='Cancelled')/COUNT(*),1) observed_churn_pct
FROM b GROUP BY engagement_band ORDER BY avg_monthly_visits;

-- 08 Failed-payment exposure among active members
SELECT COUNT(DISTINCT CASE WHEN p.payment_status='Failed' THEN m.member_id END) active_members_with_failed_payment
FROM members m JOIN payments p USING(member_id)
WHERE m.status='Active' AND p.billing_month>='2026-05-01';

-- 09 Actionable retention queue: active only; rules are mutually prioritized.
WITH recent AS (
 SELECT m.member_id,m.member_code,m.first_name||' '||m.last_name member_name,l.location_name,p.plan_name,m.acquisition_channel,
  SUM(CASE WHEN c.checkin_date>='2026-06-01' THEN 1 ELSE 0 END) visits_last_61d,
  EXISTS(SELECT 1 FROM payments x WHERE x.member_id=m.member_id AND x.billing_month>='2026-05-01' AND x.payment_status='Failed') failed_payment
 FROM members m JOIN locations l USING(location_id) JOIN plans p USING(plan_id)
 LEFT JOIN checkins c USING(member_id) WHERE m.status='Active' GROUP BY m.member_id
)
SELECT *, CASE WHEN failed_payment=1 AND visits_last_61d<=2 THEN 'Critical'
               WHEN failed_payment=1 OR visits_last_61d<=2 THEN 'High'
               WHEN visits_last_61d<=5 THEN 'Medium' END risk_tier,
 CASE WHEN failed_payment=1 THEN 'Resolve payment and contact member' ELSE 'Launch re-engagement outreach' END recommended_action
FROM recent WHERE failed_payment=1 OR visits_last_61d<=5
ORDER BY CASE WHEN failed_payment=1 AND visits_last_61d<=2 THEN 1 WHEN failed_payment=1 OR visits_last_61d<=2 THEN 2 ELSE 3 END, visits_last_61d;

-- 10 Churn timing distribution
SELECT CASE WHEN julianday(cancel_date)-julianday(join_date)<90 THEN '0-2 months'
            WHEN julianday(cancel_date)-julianday(join_date)<180 THEN '3-5 months'
            WHEN julianday(cancel_date)-julianday(join_date)<365 THEN '6-11 months' ELSE '12+ months' END tenure_band,
       COUNT(*) cancellations
FROM members WHERE cancel_date IS NOT NULL GROUP BY tenure_band ORDER BY MIN(julianday(cancel_date)-julianday(join_date));

-- 11 Revenue at risk in the active intervention queue
WITH q AS (
 SELECT DISTINCT m.member_id,m.plan_id FROM members m LEFT JOIN checkins c ON c.member_id=m.member_id AND c.checkin_date>='2026-06-01'
 WHERE m.status='Active' GROUP BY m.member_id
 HAVING COUNT(c.checkin_id)<=5 OR EXISTS(SELECT 1 FROM payments p WHERE p.member_id=m.member_id AND p.billing_month>='2026-05-01' AND p.payment_status='Failed')
)
SELECT COUNT(*) at_risk_members,ROUND(SUM(p.monthly_fee),2) monthly_revenue_at_risk FROM q JOIN plans p USING(plan_id);

-- 12 Data-integrity checks
SELECT 'duplicate_member_id' control,COUNT(*) issue_count FROM (SELECT member_id FROM members GROUP BY member_id HAVING COUNT(*)>1)
UNION ALL SELECT 'cancel_before_join',COUNT(*) FROM members WHERE cancel_date<join_date
UNION ALL SELECT 'orphan_checkin',COUNT(*) FROM checkins c LEFT JOIN members m USING(member_id) WHERE m.member_id IS NULL
UNION ALL SELECT 'orphan_payment',COUNT(*) FROM payments p LEFT JOIN members m USING(member_id) WHERE m.member_id IS NULL;
