# Rebuild and Benchmark Guide

1. In Power BI Desktop, import the five files in `sample-data` and apply `solution/optimized-transformations.pq` to FactSales.
2. Apply the data model exactly as documented in `DATA_MODEL_SPEC.md`; mark DimDate as the date table and disable Auto date/time.
3. Create a dedicated Measures table and paste `optimized-measures.dax`. Use dynamic format strings rather than `FORMAT`.
4. Apply the JSON theme. Build no more than 12 visible objects on the executive page; avoid duplicate cards and synchronized slicers that do not affect a decision.
5. Validate every KPI against `validated_kpis.json` before testing speed.
6. Clear cache, close unrelated applications, record Power BI Desktop version and machine profile, and run every scenario three times cold and three times warm.
7. Export Performance Analyzer JSON. In DAX Studio, capture Server Timings and Query Plan; in VertiPaq Analyzer, record table size, column size, cardinality, and encoding.
8. Report medians, not best runs. Compare like-for-like filters, visuals, and data volumes.

## Acceptance criteria
- All 10 controls PASS and all headline KPI variances equal zero.
- Median initial page render ≤1,500 ms.
- Median slicer interaction ≤500 ms.
- No single visual exceeds 800 ms without documented justification.
- No bidirectional or many-to-many relationships.
- No unnecessary text columns in FactSales; no implicit measures.
- Actual PBIX size and VertiPaq footprint are recorded after the Desktop build.
