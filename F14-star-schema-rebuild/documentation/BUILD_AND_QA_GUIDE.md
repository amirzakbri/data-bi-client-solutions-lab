# Build and QA Guide

+1. Import the five CSV files from `solution/` into Power BI Desktop.
+2. Disable load for staging queries if you introduce them.
+3. Create the four one-to-many, single-direction relationships documented in `DATA_MODEL.md`.
+4. Mark `DimDate` as the date table using its `Date` column.
+5. Add the measures from `measures.dax`; hide numeric fact columns from report view.
+6. Import `retail-model-theme.json`, then build the report from `DASHBOARD_SPEC.md`.
+7. Compare all headline values with `validated_kpis.json`.
+
+## Validation controls
+
+| Control | Expected result |
+|---|---|
+| Fact row count equals flat-export row count | PASS |
+| SalesLineKey is unique | PASS |
+| Customer, product, store, and date keys are unique | PASS |
+| Every fact foreign key resolves | PASS |
+| Revenue reconciles before and after | PASS |
+| Cost reconciles before and after | PASS |
+| Profit equals revenue minus cost | PASS |
+| Order distinct count reconciles | PASS |
+| Units reconcile | PASS |
+| No blank dimension keys | PASS |
+
+Native `.pbix` files must be created in Power BI Desktop; this repository provides the reproducible model, transformations, measures, theme, specification, and verified baseline rather than a fabricated binary.
+