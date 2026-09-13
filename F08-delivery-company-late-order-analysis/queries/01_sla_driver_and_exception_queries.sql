-- F08 Delivery Company Late-Order Analysis — SQLite compatible
-- Q01 Executive SLA summary
SELECT COUNT(*) shipments, SUM(status='Delivered') delivered, SUM(status='Failed') failed,
 SUM(status='In Transit') in_transit,
 ROUND(100.0*SUM(status='Delivered' AND delivered_at<=promised_at)/SUM(status='Delivered'),1) on_time_pct,
 ROUND(AVG(CASE WHEN status='Delivered' AND delivered_at>promised_at THEN (julianday(delivered_at)-julianday(promised_at))*24 END),1) avg_late_hours
FROM shipments;

-- Q02 Monthly SLA trend
SELECT substr(promised_at,1,7) month,COUNT(*) promised_shipments,SUM(status='Delivered') delivered,
 SUM(status='Delivered' AND delivered_at>promised_at) late_deliveries,
 ROUND(100.0*SUM(status='Delivered' AND delivered_at<=promised_at)/NULLIF(SUM(status='Delivered'),0),1) on_time_pct
FROM shipments GROUP BY 1 ORDER BY 1;

-- Q03 Hub performance with volume context
SELECT h.hub_name,COUNT(*) shipments,SUM(s.status='Delivered') delivered,SUM(s.status='Delivered' AND s.delivered_at>s.promised_at) late,
 ROUND(100.0*SUM(s.status='Delivered' AND s.delivered_at<=s.promised_at)/NULLIF(SUM(s.status='Delivered'),0),1) on_time_pct,
 ROUND(AVG(CASE WHEN s.status='Delivered' AND s.delivered_at>s.promised_at THEN (julianday(s.delivered_at)-julianday(s.promised_at))*24 END),1) avg_late_hours
FROM shipments s JOIN hubs h ON h.hub_id=s.origin_hub_id GROUP BY 1 ORDER BY on_time_pct;

-- Q04 Carrier SLA scorecard
SELECT c.carrier_name,COUNT(*) shipments,SUM(s.status='Delivered') delivered,SUM(s.status='Failed') failed,
 ROUND(100.0*SUM(s.status='Delivered' AND s.delivered_at<=s.promised_at)/NULLIF(SUM(s.status='Delivered'),0),1) on_time_pct,
 ROUND(100.0*SUM(s.status='Failed')/COUNT(*),1) failure_pct
FROM shipments s JOIN carriers c USING(carrier_id) GROUP BY 1 ORDER BY on_time_pct;

-- Q05 Service-level SLA
SELECT service_level,COUNT(*) shipments,SUM(status='Delivered' AND delivered_at>promised_at) late,
 ROUND(100.0*SUM(status='Delivered' AND delivered_at<=promised_at)/NULLIF(SUM(status='Delivered'),0),1) on_time_pct,
 ROUND(AVG(CASE WHEN status='Delivered' AND delivered_at>promised_at THEN (julianday(delivered_at)-julianday(promised_at))*24 END),1) avg_late_hours
FROM shipments GROUP BY 1 ORDER BY on_time_pct;

-- Q06 Delay-reason Pareto table
SELECT delay_reason,COUNT(*) late_shipments,
 ROUND(100.0*COUNT(*)/SUM(COUNT(*)) OVER(),1) late_share_pct,
 ROUND(AVG((julianday(delivered_at)-julianday(promised_at))*24),1) avg_late_hours
FROM shipments WHERE status='Delivered' AND delivered_at>promised_at GROUP BY 1 ORDER BY late_shipments DESC;

-- Q07 Hub x carrier hotspot matrix
SELECT h.hub_name,c.carrier_name,COUNT(*) delivered,SUM(s.delivered_at>s.promised_at) late,
 ROUND(100.0*SUM(s.delivered_at<=s.promised_at)/COUNT(*),1) on_time_pct
FROM shipments s JOIN hubs h ON h.hub_id=s.origin_hub_id JOIN carriers c USING(carrier_id)
WHERE s.status='Delivered' GROUP BY 1,2 HAVING COUNT(*)>=25 ORDER BY on_time_pct;

-- Q08 Distance-band SLA
SELECT CASE WHEN distance_km<100 THEN '0-99 km' WHEN distance_km<300 THEN '100-299 km' WHEN distance_km<600 THEN '300-599 km' ELSE '600+ km' END distance_band,
 COUNT(*) delivered,ROUND(100.0*SUM(delivered_at<=promised_at)/COUNT(*),1) on_time_pct
FROM shipments WHERE status='Delivered' GROUP BY 1 ORDER BY MIN(distance_km);

-- Q09 Weekday effect based on shipment creation
SELECT CASE strftime('%w',created_at) WHEN '0' THEN 'Sun' WHEN '1' THEN 'Mon' WHEN '2' THEN 'Tue' WHEN '3' THEN 'Wed' WHEN '4' THEN 'Thu' WHEN '5' THEN 'Fri' ELSE 'Sat' END created_weekday,
 COUNT(*) delivered,ROUND(100.0*SUM(delivered_at<=promised_at)/COUNT(*),1) on_time_pct
FROM shipments WHERE status='Delivered' GROUP BY strftime('%w',created_at) ORDER BY strftime('%w',created_at);

-- Q10 First-attempt success
SELECT ROUND(100.0*SUM(attempt_result='Success')/COUNT(*),1) first_attempt_success_pct,COUNT(*) first_attempts
FROM delivery_attempts WHERE attempt_number=1;

-- Q11 Repeat-attempt drivers
SELECT COALESCE(failure_reason,'Unspecified') failure_reason,COUNT(*) failed_first_attempts
FROM delivery_attempts WHERE attempt_number=1 AND attempt_result='Failed' GROUP BY 1 ORDER BY 2 DESC;

-- Q12 Severe late deliveries (>24 hours)
SELECT s.shipment_id,h.hub_name,c.carrier_name,s.service_level,s.destination_city,
 ROUND((julianday(s.delivered_at)-julianday(s.promised_at))*24,1) late_hours,s.delay_reason,s.order_value
FROM shipments s JOIN hubs h ON h.hub_id=s.origin_hub_id JOIN carriers c USING(carrier_id)
WHERE s.status='Delivered' AND (julianday(s.delivered_at)-julianday(s.promised_at))*24>24 ORDER BY late_hours DESC;

-- Q13 Open shipment exception queue at reporting cutoff 2026-08-15 00:00
SELECT s.shipment_id,h.hub_name,c.carrier_name,s.service_level,s.destination_city,s.promised_at,
 ROUND((julianday('2026-08-15 00:00:00')-julianday(s.promised_at))*24,1) overdue_hours
FROM shipments s JOIN hubs h ON h.hub_id=s.origin_hub_id JOIN carriers c USING(carrier_id)
WHERE s.status='In Transit' AND s.promised_at<'2026-08-15 00:00:00' ORDER BY overdue_hours DESC;

-- Q14 Failed-delivery queue
SELECT s.shipment_id,h.hub_name,c.carrier_name,s.destination_city,s.delay_reason,s.order_value
FROM shipments s JOIN hubs h ON h.hub_id=s.origin_hub_id JOIN carriers c USING(carrier_id) WHERE s.status='Failed' ORDER BY s.order_value DESC;

-- Q15 Latest shipment event for open cases
WITH ranked AS (SELECT e.*,ROW_NUMBER() OVER(PARTITION BY shipment_id ORDER BY event_at DESC,event_id DESC) rn FROM tracking_events e)
SELECT s.shipment_id,s.promised_at,r.event_type latest_event,r.event_at latest_event_at,h.hub_name
FROM shipments s JOIN ranked r ON r.shipment_id=s.shipment_id AND r.rn=1 JOIN hubs h ON h.hub_id=r.hub_id WHERE s.status='In Transit' ORDER BY s.promised_at;
