# Property Rent Collection Dashboard

A portfolio-ready property-management analytics case that converts unit, lease, and rent-ledger exports into a validated collection dashboard and tenant follow-up queue.

## Client problem

A residential property manager tracked rent billing and payments in separate files. Management could not consistently distinguish occupancy from collection performance, quantify arrears by age, rank properties by unpaid balance, or assign tenant follow-up.

## Delivered solution

- Executive dashboard for rent billed, cash collected, collection rate, arrears, and occupancy
- Monthly billed-versus-collected trend
- Arrears aging across 1–30, 31–60, 61–90, and 90+ days
- Property ranking by unpaid balance
- Tenant-level collections queue with risk and recommended action
- Import-ready fact and dimension data
- Power BI star-schema specification, DAX measures, Power Query script, and theme
- Twelve reconciliation and data-quality controls

## Validated results

| KPI | Result |
|---|---:|
| Properties | 12 |
| Total units | 96 |
| Occupied units | 88 |
| Occupancy rate | 91.7% |
| Rent billed | $1,602,000 |
| Rent collected | $1,476,786 |
| Collection rate | 92.2% |
| Total arrears | $125,214 |
| Open invoices | 110 |
| High-risk tenant accounts | 60 |

## Business value

The solution replaces manual totals with an auditable portfolio view. Finance can reconcile billed rent to cash, property managers can focus on the highest-risk accounts, and leasing teams can monitor vacancy separately from payment performance.

## Repository contents

```text
sample-data/     Properties, units/leases, and rent-ledger CSV files
solution/        Excel dashboard, Power BI build assets, and KPI baseline
assets/          Dashboard preview
documentation/   Data model, dashboard design, and build/QA guide
```

## How to use

1. Open `solution/Property_Rent_Collection_Dashboard.xlsx` for the finished analytical workbook.
2. Review the dashboard, tenant arrears queue, KPI definitions, and QA controls.
3. To build the native Power BI report, import the three CSV files, follow `documentation/DATA_MODEL.md`, add `solution/measures.dax`, and apply the theme.
4. Confirm every control on `QA Controls` returns `PASS` before publishing.

## Tools demonstrated

Excel, Power BI, Power Query, DAX, star-schema modeling, rent reconciliation, aging analysis, exception management, dashboard design, and analytical QA.

> All data is synthetic and created solely for portfolio demonstration.
