# Event Registration Reporting Workflow

An end-to-end Excel and Power Query portfolio case that turns raw event-registration exports into an operational dashboard, a validated KPI layer, and an actionable exception queue.

## Client problem

The event team managed registrations, payments, consent, and check-ins in one large export. Management could not reliably answer how many attendees were confirmed, how much cash had been collected, which events were nearing capacity, or which records required follow-up.

## Delivered solution

- Standardized, table-based registration dataset
- Executive operations dashboard covering demand, revenue, attendance, capacity, and channel mix
- Record-level exception queue with priority, owner, and recommended action
- Reusable Power Query transformation for folder-based CSV ingestion
- Explicit KPI definitions and business rules
- Ten validation controls with expected baselines
- Import-ready event and registration CSV files

## Validated results

| KPI | Result |
|---|---:|
| Events | 8 |
| Registration records | 1,245 |
| Confirmed registrations | 1,023 |
| Cash collected | $123,597 |
| Expected revenue | $168,117 |
| Collection rate | 73.5% |
| Checked-in attendees | 801 |
| Attendance rate | 78.3% |
| Actionable exception rows | 123 |
| Duplicate email rows | 2 |

## Business value

The workflow replaces manual counting and fragmented follow-up with one auditable reporting process. Finance receives a payment work queue, event operations can monitor capacity and check-ins, marketing can enforce consent exclusions, and management receives reconciled KPIs.

## Repository contents

```text
sample-data/     Raw registration and event exports
solution/        Excel workflow, Power Query script, and KPI baseline
assets/          Dashboard preview
documentation/   Workflow, refresh, and QA instructions
```

## How to use

1. Open `solution/Event_Registration_Reporting_Workflow.xlsx`.
2. Review the `Dashboard`, `Exceptions`, `KPI Definitions`, and `QA Controls` sheets.
3. To rebuild from new exports, place compatible CSV files in one folder and use the supplied Power Query script, updating the folder parameter.
4. Refresh the query and confirm every control on `QA Controls` returns `PASS` before distribution.

## Tools demonstrated

Excel, Power Query, data cleaning, KPI design, payment reconciliation, operational reporting, exception management, dashboard design, and analytical QA.

> All data is synthetic and created solely for portfolio demonstration.
