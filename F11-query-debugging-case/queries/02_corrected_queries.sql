-- Corrected, decision-safe queries (SQLite compatible).
-- F01: aggregate lines and promotions separately at order grain before joining.
WITH line_totals AS (SELECT order_id,SUM(quantity*unit_price*(1-discount_pct)) gross FROM order_lines GROUP BY order_id), promo_totals AS (SELECT order_id,SUM(discount_amount) promo FROM order_promotions GROUP BY order_id) SELECT ROUND(SUM(lt.gross-COALESCE(pt.promo,0)),2) revenue FROM orders o JOIN line_totals lt USING(order_id) LEFT JOIN promo_totals pt USING(order_id) WHERE o.status='Completed';

-- F02: keep the period condition in ON so every customer survives the LEFT JOIN.
SELECT c.region,COUNT(DISTINCT c.customer_id) total_customers,COUNT(DISTINCT CASE WHEN o.order_id IS NOT NULL THEN c.customer_id END) customers_with_2026_orders FROM customers c LEFT JOIN orders o ON c.customer_id=o.customer_id AND o.order_date>='2026-01-01' AND o.order_date<'2027-01-01' GROUP BY c.region;

-- F03: count customers once across the whole reporting window.
SELECT COUNT(DISTINCT customer_id) yearly_customers FROM orders WHERE order_date>='2026-01-01' AND order_date<'2027-01-01';

-- F04: calculate directly from all lines; no average-of-averages.
SELECT ROUND(AVG(unit_price*quantity),2) average_line_value FROM order_lines;

-- F05: half-open date interval remains correct for DATE and TIMESTAMP values.
SELECT COUNT(*) orders_in_july FROM orders WHERE order_date>='2026-07-01' AND order_date<'2026-08-01';

-- F06: sargable range predicates use the date index.
SELECT COUNT(*) completed_2026 FROM orders WHERE order_date>='2026-01-01' AND order_date<'2027-01-01' AND status='Completed';
