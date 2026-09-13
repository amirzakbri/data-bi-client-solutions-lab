# F04 — Monthly Files to One Refreshable Report

## Client problem

A growing specialty coffee retailer receives one CSV sales export every month. Management manually copies each file into a master spreadsheet, creating delays, inconsistent formulas, and a high risk of missed rows.

## Solution delivered

A folder-based consolidation workflow and Excel management report that combines monthly files into one standardized dataset. The report provides revenue, profit, margin, order volume, monthly trends, channel performance, and product performance.

## Business value

- Replaces repetitive monthly copy-and-paste work with a repeatable refresh process.
- Creates one governed dataset for management reporting.
- Reduces formula drift and omitted-file risk.
- Makes monthly and channel performance visible in one dashboard.

## Tools

Excel, Power Query, CSV, data modeling, KPI reporting, data-quality checks

## Repository contents

```text
F04-monthly-files-refreshable-report/
├── README.md
├── solution/
│   ├── Monthly_Sales_Refreshable_Report.xlsx
│   └── Folder_Consolidation_Query.pq
├── sample-data/
│   └── monthly-sales-files/
│       └── 6 monthly CSV exports
└── assets/
    └── dashboard-preview.png
```

## Refresh workflow

1. Place monthly CSV exports in `sample-data/monthly-sales-files/`.
2. In Excel, create a one-cell named range called `SourceFolder` containing the absolute path of that folder.
3. Select **Data → Get Data → From Other Sources → Blank Query**.
4. Open **Advanced Editor**, paste `Folder_Consolidation_Query.pq`, and load the result as the `SalesData` table.
5. For future months, add the new CSV and select **Data → Refresh All**.

The portfolio workbook includes the validated January–June 2026 consolidated result so reviewers can inspect the finished dashboard without reconnecting a local path.

## Data-quality controls

- CSV-only file filter
- Explicit column data types
- Blank Order ID removal
- Standardized `yyyy-MM` reporting month
- Row-count and revenue reconciliation checks
- Required-schema checklist in the workbook

## Key outputs

- Total revenue, total profit, profit margin, and order count
- Revenue and profit trend by month
- Channel revenue and margin comparison
- Product revenue and margin summary

## Portfolio framing

This is a simulated client project created to demonstrate a practical reporting-automation service. The dataset is synthetic and contains no confidential business information.

