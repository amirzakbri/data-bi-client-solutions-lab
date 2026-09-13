# Runbook

1. Open `data/query_debugging_case.db` with SQLite 3 or DB Browser for SQLite.
2. Run `queries/01_broken_queries.sql` only to reproduce the defects.
3. Run `queries/02_corrected_queries.sql` for governed results.
4. Compare outputs with `outputs/validated_baseline.json`.
5. Confirm every row in `outputs/validation_results.csv` is PASS.

Never publish results from the broken query pack. Preserve table grain in every future join and use half-open date windows (`>= start`, `< next_period`).
