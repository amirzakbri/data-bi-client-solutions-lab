# Build and QA Guide

1. Import all four CSV files from sample-data.
2. Confirm date, decimal, whole-number, and text types.
3. Create relationships described in DATA_MODEL.md.
4. Add and mark a Date table.
5. Import the theme and create the measures from measures.dax.
6. Build the two pages in DASHBOARD_SPEC.md.
7. Reconcile the Power BI cards to validated_kpis.json.

## Validation baseline

- Projects: 24
- Revenue: $1,431,800.00
- Delivery cost: $793,728.48
- Gross profit: $638,071.52
- Gross margin: 44.56%
- Total hours: 8,738
- Billable hours: 7,297
- Billable utilization: 83.51%
- Critical projects: 5
- Watch projects: 4

Check that project revenue equals the client rollup, labor and vendor facts sum to actual cost, and each project is counted once.

