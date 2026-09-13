# SQL Duplicate and Data-Quality Audit

+A reproducible SQLite audit for an e-commerce customer/order database. The project profiles raw tables, detects exact and normalized duplicates, validates domain and cross-field rules, checks referential integrity, quarantines unsafe records, and exposes clean analytical views without altering source data.

+## Business problem

+CRM and order exports were not safe for reporting: duplicated customer identities could inflate customer counts, duplicated orders could inflate revenue, and orphaned or malformed records could break joins. The client needed quantified evidence, reviewable SQL, and clean outputs.

+## Results

+- 418 raw customer rows → 355 clean rows
+- 906 raw order rows → 746 clean rows
+- 16 customer rows affected by duplicate IDs
+- 36 customer rows affected by normalized-email duplicates
+- 17 order rows affected by duplicate IDs
+- 12 orphan order rows
+- $217,336.73 validated clean revenue
+- 6/6 independent controls passed

+## Repository contents

+- `data/raw/`: intentionally defective CSV exports
+- `data/quality_audit.db`: runnable SQLite database
+- `queries/01_profile_and_audit.sql`: issue views and clean views
+- `data/clean/`: materialized clean outputs
+- `outputs/`: metrics, baseline, and validation results
+- `documentation/`: audit findings and runbook
+- `assets/`: portfolio preview

+## Run

+Open `data/quality_audit.db` in SQLite and run `queries/01_profile_and_audit.sql`. Inspect `v_customer_issues` and `v_order_issues`; use `customers_clean` and `orders_clean` only for analysis.

+## Design principles

+Raw data is immutable. Detection is separated from remediation. Duplicate-email matching is normalized but deterministic; ambiguous identity matches require human review. Clean views exclude any row failing a critical rule.

+## Tools
+SQL (SQLite), Python for reproducible data generation and independent QA.
