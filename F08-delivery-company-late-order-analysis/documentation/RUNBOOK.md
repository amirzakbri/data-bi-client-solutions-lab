# Operational Runbook

1. Open `data/delivery_operations.db` in SQLite 3 or DB Browser for SQLite.
2. Read the metric contract in `queries/00_schema_and_metric_notes.sql`.
3. Execute `queries/01_sla_driver_and_exception_queries.sql` as a script or run individual numbered queries.
4. Reconcile headline results to `outputs/validated_kpi_baseline.json`.
5. Confirm all controls in `outputs/validation_results.csv` are `PASS`.
6. Use `operational_exception_queue.csv` as the daily follow-up list.
7. Refresh the reporting cutoff in Q13 when adapting the project to live data.

For another SQL engine, replace SQLite functions including `julianday`, `substr`, and `strftime`.
