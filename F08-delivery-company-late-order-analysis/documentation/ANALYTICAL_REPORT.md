# Delivery SLA Diagnostic Report

## Executive Summary
- **Network SLA is below an assumed 90% operating target:** 82.8% of 3,439 delivered shipments arrived by their promise time.
- **The problem is concentrated:** Bursa Hub posts the lowest hub SLA at 69.8%, while RouteOne is the weakest carrier at 72.7%.
- **The largest recorded delay driver is Hub Congestion:** 162 late shipments, or 27.5% of all late deliveries.
- **Operations has a concrete worklist:** 332 severe-late or overdue-open shipments are retained in the governed exception queue.

## Where performance breaks down
The network handled 3,521 shipments created from January through July 2026; promise dates extend into early August. SLA is calculated only for completed deliveries, while failed and in-transit shipments remain visible as separate operational outcomes. This prevents unresolved shipments from being silently classified as on time or late.

Bursa Hub and RouteOne are the clearest intervention points. Their volume is shown beside their rate, so small segments do not dominate prioritization. The hub-by-carrier SQL cut should be used to determine whether the weakness is broad or concentrated in a specific operating partnership.

## Delay causes and severity
Late delivery is not a single operational problem. The reason Pareto separates network constraints, address/customer issues, weather, and vehicle failures. Severe cases are defined as more than 24 hours late and are exported individually for follow-up.

The analysis is descriptive. The synthetic data supports strong association statements, but it does not prove that a hub, carrier, or recorded reason caused a delay independently of distance, service mix, or seasonality.

## Recommended next steps
1. Review the lowest-performing hub-carrier combinations weekly and assign owners to combinations below the 90% SLA threshold.
2. Work `operational_exception_queue.csv` daily, prioritizing open overdue shipments before closed severe-late cases.
3. Track corrective actions against the largest delay-reason category and compare the next four weeks with the current baseline.
4. Add delivery cost and compensation fields before making carrier-award or contract decisions.

## Further questions
- Are low-SLA routes also high-cost routes after compensation and re-delivery expense?
- Do scans show a specific dwell stage inside the weakest hub-carrier combination?
- Are customer-facing promise times calibrated consistently across service levels?

## Caveats and assumptions
The dataset is synthetic. The reporting cutoff is 2026-08-15 00:00. On-time rate uses delivered shipments as the denominator, promise timestamps are assumed to share one timezone, and delay reasons are treated as the final operational classification. The 90% target is an illustrative management benchmark, not a contractual SLA.
