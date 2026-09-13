# Build and QA Guide

1. Import `retail_dashboard_source.csv` with `transformations.pq`.
2. Build the conformed dimensions in `DATA_MODEL.md`; use one-to-many, single-direction relationships.
3. Mark the date table and add `measures.dax`.
4. Import `executive-retail-theme.json` and follow `DASHBOARD_SPEC.md`.
5. Use the supplied before/after images as design evidence, not as substitutes for the report.
6. Reconcile the report to `validated_kpis.json` and the product table to `product_action_queue.csv`.

## Ten validation controls
Source row count; unique OrderID; complete date coverage; revenue reconciliation; cost reconciliation; profit equation; target reconciliation; monthly rollup reconciliation; category rollup reconciliation; exception-queue reconciliation. All must pass before publishing.

A native `.pbix` must be authored and saved through Power BI Desktop. This project includes the complete reproducible build kit rather than a fabricated binary.
