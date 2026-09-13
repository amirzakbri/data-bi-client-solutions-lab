-- Six deliberately faulty queries. Do not use for decisions.
-- B01: promotion join multiplies order lines when an order has multiple promotions.
SELECT SUM(ol.quantity*ol.unit_price*(1-ol.discount_pct)-COALESCE(op.discount_amount,0)) revenue
FROM orders o JOIN order_lines ol ON o.order_id=ol.order_id LEFT JOIN order_promotions op ON o.order_id=op.order_id
WHERE o.status='Completed';

-- B02: WHERE predicate null-rejects the LEFT JOIN and removes customers with no 2026 orders.
SELECT c.region,COUNT(DISTINCT c.customer_id) customers FROM customers c LEFT JOIN orders o ON c.customer_id=o.customer_id WHERE o.order_date>='2026-01-01' GROUP BY c.region;

-- B03: SUM of monthly distinct customers is not the yearly distinct-customer count.
WITH m AS (SELECT substr(order_date,1,7) month,COUNT(DISTINCT customer_id) n FROM orders WHERE order_date>='2026-01-01' GROUP BY 1) SELECT SUM(n) yearly_customers FROM m;

-- B04: average of category averages weights every category equally.
WITH a AS (SELECT p.category,AVG(ol.unit_price*ol.quantity) avg_line FROM order_lines ol JOIN products p USING(product_id) GROUP BY 1) SELECT AVG(avg_line) average_line_value FROM a;

-- B05: BETWEEN with an inclusive midnight end misses records when timestamps are introduced.
SELECT COUNT(*) orders_in_july FROM orders WHERE order_date BETWEEN '2026-07-01' AND '2026-07-31';

-- B06: wrapping the indexed column in substr prevents an efficient range seek.
SELECT COUNT(*) completed_2026 FROM orders WHERE substr(order_date,1,4)='2026' AND status='Completed';
