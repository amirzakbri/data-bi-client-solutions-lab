# Automated Weekly KPI Summary

A reusable reporting workflow for a multi-channel e-commerce business. It converts daily operational data into a governed weekly Excel scorecard, management HTML, concise email update, and auditable KPI output.

## Business problem

Manual weekly reporting often mixes partial periods, inconsistent formulas, and unowned exceptions. This solution enforces complete Monday–Sunday comparisons, explicit targets, higher/lower-is-better rules, owners, and QA controls.

## Deliverables

- `solution/Automated_Weekly_KPI_Summary.xlsx` — executive scorecard, source table, metric dictionary, and controls
- `src/generate_weekly_summary.py` — dependency-free command-line automation
- `solution/management_summary.html` and `solution/weekly_email.txt` — stakeholder outputs
- `sample-data/daily_channel_performance.csv` — 280 daily-channel records across 10 weeks
- `solution/weekly_kpis.csv` and `validated_kpis.json` — machine-readable results
- `tests/test_weekly_summary.py` — automated smoke test

## Run

```bash
python src/generate_weekly_summary.py --input sample-data/daily_channel_performance.csv --week-ending 2026-08-02 --output-dir solution
python -m pytest tests/test_weekly_summary.py
```

## KPI framework

Revenue and orders measure commercial scale; conversion and average order value diagnose demand quality; gross margin protects unit economics; refund rate and on-time fulfilment are customer/operational guardrails. All ratios are recomputed from summed numerators and denominators rather than averaged daily rates.

## Controls

The workbook verifies source row count, seven complete current-week dates, revenue and order reconciliation, metric count, date completeness, and non-negative revenue. The automated output uses the same definitions and reporting cutoff.

## Privacy

All records are synthetic and contain no personal or confidential data.
