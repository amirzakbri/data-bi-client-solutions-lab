# F08 — Delivery Company Late-Order Analysis

## Business problem
A parcel-delivery operator needs to understand why shipments miss their promised date, which hubs and carriers require intervention, and which individual shipments need immediate follow-up.

## Outcome
- **3,521** shipments assessed and **3,439** completed deliveries
- **82.8%** delivered on time; **590** late deliveries
- **26.6 hours** average delay among late deliveries
- **326** severe late deliveries and **6** open shipments
- **84.8%** first-attempt success
- **15 SQL analyses** and **12/12 validation controls passed**

## Decision coverage
| Area | Decisions supported |
|---|---|
| SLA governance | On-time definition, monthly movement, severity, open/failed populations |
| Network performance | Hub, carrier, service, distance, weekday, and hotspot comparisons |
| Root causes | Delay-reason concentration and repeat-attempt drivers |
| Operations | Severe-late, open-overdue, failed-delivery, and latest-event queues |

## Run
```bash
sqlite3 data/delivery_operations.db < queries/01_sla_driver_and_exception_queries.sql
```

All data is synthetic and safe to publish.
