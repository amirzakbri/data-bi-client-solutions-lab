# F06 — Broken Excel Report Repair

## Client problem
A six-month sales report could not be trusted. It contained broken and overwritten formulas, invalid dates, inconsistent region labels, a duplicate order, an incomplete product lookup, stale KPI values, and a chart that excluded two months.

## Solution delivered
The workbook was audited at cell and record level, repaired, reconciled, and redesigned for recurring use. The final version contains a structured sales table, formula-driven KPIs, a six-month trend, a ten-item repair log, and six validation controls.

## Business result
- 241 source rows reviewed and 240 unique orders retained
- 10 documented issues fixed
- 3 formula defects repaired
- 3 invalid dates corrected
- 1 duplicate removed
- 1,080 units and $199,204.80 net revenue reconciled
- 6 of 6 validation checks passed

## Files
- `sample-data/Broken_Client_Sales_Report.xlsx` — intentionally damaged client-style source
- `solution/Repaired_Sales_Report.xlsx` — audited and repaired delivery
- `documentation/repair-metrics.csv` — concise QA baseline
- `assets/dashboard-preview.png` — portfolio preview

## Tools and skills demonstrated
Excel formulas, structured tables, data-quality auditing, reconciliation, formula debugging, workbook redesign, validation controls, chart repair, and client handover documentation.

## Repair approach
1. Profiled formulas, dates, IDs, labels, lookups, KPIs, and chart ranges.
2. Quarantined or corrected source defects while preserving the audit trail.
3. Rebuilt calculation columns with consistent formulas.
4. Replaced hardcoded summaries with linked formulas.
5. Added visible validation checks and documented each repair.
6. Reconciled totals and visually checked every worksheet.

> Portfolio note: the data is synthetic and created solely to demonstrate a realistic report-repair engagement.
