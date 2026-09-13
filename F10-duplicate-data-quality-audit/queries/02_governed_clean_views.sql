-- Require every clean order to join to a customer that also survived quality rules
DROP VIEW IF EXISTS orders_clean;
CREATE VIEW orders_clean AS
SELECT o.* FROM orders_raw o JOIN v_order_issues i ON o.rowid=i.source_row
WHERE missing_id+duplicate_id+orphan_customer+invalid_amount+amount_mismatch+invalid_status+future_order=0
AND EXISTS (SELECT 1 FROM customers_clean c WHERE c.customer_id=o.customer_id);
