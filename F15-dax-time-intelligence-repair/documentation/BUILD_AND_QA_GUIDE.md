# Build and QA Guide

1. Import `retail_sales.csv` and `DimDate.csv`.
2. Set both date columns to Date type.
3. Create an active 1:* relationship from `DimDate[Date]` to `Sales[OrderDate]`, single direction.
4. Mark `DimDate` as the date table. Sort Month by MonthNumber.
5. Add `corrected_measures.dax`; hide raw numeric columns and the fact date from report authors.
6. Import the theme and build the visuals in `DASHBOARD_SPEC.md`.
7. Compare month-level outputs with `validated_monthly_baseline.csv` and headline values with `validated_kpis.json`.

## Twelve required controls
Calendar contiguous; calendar keys unique; sales dates resolve; SaleID unique; base revenue reconciles; profit equation balances; monthly revenue reconciles; previous month reconciles; prior year reconciles; YTD reconciles; rolling 12M reconciles; growth measures use safe division.

A native `.pbix` must be authored in Power BI Desktop. The repository supplies a genuine reproducible build kit instead of a renamed or fabricated binary.
