# Workflow and QA Guide

1. Replace the sample CSV with a file using the same eight-column schema.
2. Choose the final day of a complete reporting week.
3. Run the Python command from the repository root.
4. Review `weekly_kpis.csv`, the HTML summary, and the email draft.
5. Investigate every `Action` KPI with its named owner before distribution.

## Metric governance

- Grain: one row per date and acquisition channel.
- Reporting week: Monday through Sunday.
- Timezone: Europe/Istanbul.
- Conversion: total orders / total sessions.
- Average order value: total revenue / total orders.
- Gross margin: (revenue − COGS) / revenue.
- Refund rate: refund orders / total orders; lower is better.
- On-time fulfilment: on-time orders / total orders.

## Validation evidence

The reference run uses 280 complete source rows and compares 2026-07-27–2026-08-02 with 2026-07-20–2026-07-26. Results are independently stored in `validated_kpis.json`. The workbook contains eight control assertions and the Python test confirms all seven governed KPIs and stakeholder outputs are produced.

## Known caveat

Refunds may arrive after the reporting week and revise the historical refund rate. Operational reviews should label late adjustments instead of silently overwriting previously distributed results.
