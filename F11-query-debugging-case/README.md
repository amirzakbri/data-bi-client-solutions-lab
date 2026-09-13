# F11 — SQL Query Debugging Case

## Business problem
A monthly e-commerce report ran successfully but returned misleading KPIs. This case diagnoses six correctness and performance defects, repairs them, and proves the results against independent controls.

## Outcome
- 1,451 orders and 2,901 order lines tested
- Correct completed-order revenue: **$843,743.19**
- Faulty join result: **$914,777.13** (**$71,033.94 overstatement**)
- All 7 end-to-end controls pass

## Defects repaired
| ID | Defect | Business risk | Repair |
|---|---|---|---|
| B01 | Many-to-many promotion join | Revenue inflation | Aggregate lines and promotions to order grain |
| B02 | LEFT JOIN filter in WHERE | Customers silently disappear | Move period condition into ON |
| B03 | Sum of monthly distincts | Annual customers double-counted | Count distinct once at annual grain |
| B04 | Average of averages | Biased KPI | Aggregate from line-level numerator |
| B05 | Inclusive end-date pattern | Boundary records can be missed | Use half-open interval |
| B06 | Function on indexed date | Avoidable full index scan | Use sargable date range |

## Run
```bash
sqlite3 data/query_debugging_case.db < queries/02_corrected_queries.sql
```

## Repository contents
- `queries/01_broken_queries.sql` — unsafe queries with diagnoses
- `queries/02_corrected_queries.sql` — decision-safe replacements
- `data/query_debugging_case.db` — runnable SQLite database
- `data/raw/` — five import-ready source tables
- `outputs/` — baseline, validation results, and query plans
- `documentation/` — debugging report and runbook
- `assets/` — portfolio preview

Synthetic data is used so the project is reproducible and safe to publish.
