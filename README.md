# Data & BI Client Solutions Lab

**Amirreza Akbari** — Power BI, Excel and SQL work for businesses whose reporting has stopped being reliable.

Twenty-four engagements, each with a defined client problem, a delivered solution, reconciled business results, and validation controls that prove the numbers.

📍 Istanbul, UTC+3 · Available for freelance and contract work

---

### About the data

Every project here is a **demonstration engagement**. The datasets were constructed to reproduce realistic client scenarios, because real client files are confidential. Every figure quoted below is produced by the delivered solution — nothing is illustrative.

---

## Report repair & rescue

When a report still runs but nobody trusts what it says.

| Project | The problem | Result |
|---|---|---|
| [F06 — Broken Excel Report Repair](F06-broken-excel-report-repair) | Six-month sales report with overwritten formulas, invalid dates, a duplicate order, stale hardcoded KPIs | 10 defects fixed, $199,204.80 reconciled, 6/6 controls passed |
| [F11 — SQL Query Debugging](F11-query-debugging-case) | Monthly report ran without errors and returned wrong KPIs | Found a **$71,033.94 revenue overstatement** from a faulty join, 7/7 controls |
| [F15 — DAX Time Intelligence Repair](F15-dax-time-intelligence-repair) | YTD and rolling-period measures disagreeing between visuals | $698,439.80 reconciled, validated against an independent baseline, 12/12 controls |
| [F17 — Dashboard Redesign](F17-power-bi-dashboard-redesign) | Correct totals, unusable layout, no route from problem to action | 10 design defects repaired, before/after preserved |

## Data modelling & performance

| Project | The problem | Result |
|---|---|---|
| [F18 — Report Performance Optimisation](F18-power-bi-report-performance-optimization) | 120,000-row report taking nearly 5 seconds to render | **4,870ms → 1,420ms (70.8% faster)**, model 104.9MB → 10.2MB, totals unchanged |
| [F14 — Star Schema Rebuild](F14-star-schema-rebuild) | Report built straight from a denormalised export, unclear grain | 4 conformed dimensions + fact table, $381,041.80 reconciled exactly |

## Dashboards & reporting

| Project | The problem | Result |
|---|---|---|
| [F12 — Salon Appointment Dashboard](F12-salon-appointment-dashboard) | Service business with appointment data and no view of revenue or no-shows | 1,231 appointments, 79.7% completion, $62,989.10 revenue · **includes a working .pbix** |
| [F13 — Property Rent Collection](F13-property-rent-collection-dashboard) | Billing and payments in separate files, arrears untracked | 96 units, 92.2% collection rate, $125,214 arrears aged and assigned |
| [F16 — Agency Project Profitability](F16-agency-project-profitability-dashboard) | Revenue, time, rates and vendor costs in four separate exports | $1,431,800 revenue, 44.6% margin, 83.5% utilisation, 5 projects flagged |
| [F02 — Invoice & Payment Tracker](F02-freelancer-invoice-payment-tracker) | Invoices and payments unlinked, partial payments breaking balances | 180 invoices, 75.2% collection rate, aged collection queue |
| [F27 — Event Registration Workflow](F27-event-registration-reporting-workflow) | Registrations, payments, consent and check-ins in one raw export | 1,245 registrations, 123 actionable exceptions, 10 controls |
| [F29 — Social Media Monthly Report](F29-social-media-monthly-performance-report) | Five platform exports encouraging vanity-metric reporting | Governed monthly report with targets, definitions and 12-control validation |
| [F05 — Sales Commission Calculator](F05-sales-commission-calculator) | Commission files ignoring returns and mishandling shared deals | 240 transactions, every payout traceable to an approved deal |

## Data quality & cleaning

| Project | The problem | Result |
|---|---|---|
| [F10 — Duplicate & Data-Quality Audit](F10-duplicate-data-quality-audit) | Duplicated identities inflating customer counts and revenue | 418 → 355 clean customers, 906 → 746 clean orders, source untouched |
| [F25 — Duplicate Customer Matching](F25-duplicate-customer-matching) | Same customers across CRM, e-commerce and support, exact matching failing | 855 → 498 golden records, 100% precision, 91.3% recall, 92 pairs to review |
| [F01 — POS Sales Cleanup](F01-restaurant-daily-sales-cleanup) | Daily POS export with duplicates, bad dates, invalid quantities | 324 → 314 clean rows, every rejection and correction evidenced |
| [F22 — Automatic CSV Cleaner](F22-automatic-csv-cleaner) | Recurring exports with drifting headers and formats | Config-driven Python cleaner, 90.9% acceptance, quarantine for unsafe rows |

## Automation

| Project | The problem | Result |
|---|---|---|
| [F04 — Monthly Files → One Refreshable Report](F04-monthly-files-refreshable-report) | Monthly CSVs copied into a master sheet by hand | Folder-based Power Query consolidation, one-click refresh |
| [F26 — Automated Weekly KPI Summary](F26-automated-weekly-kpi-summary) | Weekly reporting mixing partial periods and inconsistent formulas | One command → Excel scorecard, HTML summary and email, with QA controls |

## Analysis & insight

| Project | The problem | Result |
|---|---|---|
| [F30 — 13-Week Cash-Flow Forecast](F30-small-business-cash-flow-forecast) | Uneven receipts against fixed payroll and supplier commitments | Rolling forecast with 3 scenarios, liquidity alerts, 6 audit controls |
| [F08 — Delivery Late-Order Analysis](F08-delivery-company-late-order-analysis) | Shipments missing promised dates, cause unclear | 3,521 shipments, 82.8% on time, 590 late averaging 26.6h, 12/12 controls |
| [F09 — Gym Membership Retention](F09-gym-membership-retention-analysis) | Attrition concentrated somewhere unknown | 1,200 members, 26.9% churn, intervention queue for at-risk actives |
| [F23 — Product Review Analysis](F23-product-review-analysis) | Thousands of reviews, no way to prioritise fixes | 3,600 reviews, 18.9% negative sentiment, 4 products flagged urgent |
| [F24 — Lead Conversion Analysis](F24-website-lead-conversion-analysis) | High-volume lead sources vs sources that actually convert | 1,800 leads, 7.39% conversion, CAC and ROAS by source |

---

## How each project is structured

```
FXX-project-name/
├── README.md           Client problem, solution, validated results
├── sample-data/        Input files
├── solution/           The delivered workbook, model or script
├── documentation/      Data dictionary, build guide, QA controls
└── assets/             Dashboard preview
```

## Stack

`Power BI` · `DAX` · `Power Query` · `Excel` · `SQL (PostgreSQL, SQL Server, SQLite)` · `Python (pandas)` · `Tableau` · `Git`

## Working with me

I mostly get called when something is broken rather than to build something new — wrong totals, slow dashboards, models nobody can maintain.

If you're not sure what's wrong, start with a **Report Triage**: send the file and tell me what you don't believe about it. Within 48 hours you get a written list of every defect I find and a fixed price to repair it.

**Contact:** amirzakbri@gmail.com

## Licence

MIT — see [LICENSE](LICENSE).
