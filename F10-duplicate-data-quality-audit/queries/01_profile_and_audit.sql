-- F10 Data Quality Audit (SQLite-compatible)
DROP VIEW IF EXISTS v_customer_issues;
CREATE VIEW v_customer_issues AS
SELECT rowid source_row, customer_id,
 trim(lower(email)) normalized_email,
 CASE WHEN customer_id IS NULL OR trim(customer_id)='' THEN 1 ELSE 0 END missing_id,
 CASE WHEN trim(first_name)='' OR trim(last_name)='' THEN 1 ELSE 0 END missing_name,
 CASE WHEN email NOT LIKE '%_@_%._%' THEN 1 ELSE 0 END invalid_email,
 CASE WHEN country_code NOT IN ('US','GB','DE','TR','CA') THEN 1 ELSE 0 END invalid_country,
 CASE WHEN date(signup_date)>date('2026-08-08') THEN 1 ELSE 0 END future_signup,
 CASE WHEN status NOT IN ('active','inactive') THEN 1 ELSE 0 END invalid_status,
 CASE WHEN count(*) OVER(PARTITION BY customer_id)>1 THEN 1 ELSE 0 END duplicate_id,
 CASE WHEN count(*) OVER(PARTITION BY trim(lower(email)))>1 THEN 1 ELSE 0 END duplicate_email
FROM customers_raw;
DROP VIEW IF EXISTS v_order_issues;
CREATE VIEW v_order_issues AS
SELECT o.rowid source_row,o.*,
 CASE WHEN order_id IS NULL OR trim(order_id)='' THEN 1 ELSE 0 END missing_id,
 CASE WHEN count(*) OVER(PARTITION BY order_id)>1 THEN 1 ELSE 0 END duplicate_id,
 CASE WHEN c.customer_id IS NULL THEN 1 ELSE 0 END orphan_customer,
 CASE WHEN quantity<=0 OR unit_price<0 OR order_total<0 THEN 1 ELSE 0 END invalid_amount,
 CASE WHEN abs(order_total-round(quantity*unit_price,2))>0.009 THEN 1 ELSE 0 END amount_mismatch,
 CASE WHEN status NOT IN ('paid','shipped','cancelled') THEN 1 ELSE 0 END invalid_status,
 CASE WHEN date(order_date)>date('2026-08-08') THEN 1 ELSE 0 END future_order
FROM orders_raw o LEFT JOIN (SELECT DISTINCT customer_id FROM customers_raw) c USING(customer_id);
DROP VIEW IF EXISTS customers_clean;
CREATE VIEW customers_clean AS SELECT c.* FROM customers_raw c JOIN v_customer_issues i ON c.rowid=i.source_row
WHERE missing_id+missing_name+invalid_email+invalid_country+future_signup+invalid_status+duplicate_id+duplicate_email=0;
DROP VIEW IF EXISTS orders_clean;
CREATE VIEW orders_clean AS SELECT o.* FROM orders_raw o JOIN v_order_issues i ON o.rowid=i.source_row
WHERE missing_id+duplicate_id+orphan_customer+invalid_amount+amount_mismatch+invalid_status+future_order=0;
