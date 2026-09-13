# Build and QA Guide

1. Import the three CSV files from `sample-data`.
2. Apply `solution/FactRentLedger.pq` to the ledger query or reproduce its typed-column steps.
3. Create the star schema in `DATA_MODEL.md`; add a calendar table and mark it as the date table.
4. Add the measures in `solution/measures.dax`.
5. Import `solution/property-portfolio-theme.json` and build the two report pages in `DASHBOARD_SPEC.md`.
6. Reconcile the report to `solution/validated_kpis.json`.

## QA checklist

- Invoice IDs are unique.
- Amount paid never exceeds rent billed.
- Balance equals billed less paid.
- Billed equals collected plus arrears.
- Open balances have an aging bucket.
- Vacant units do not generate invoices.
- Collection rate uses billed rent as its denominator.
- All 12 Excel validation controls return `PASS`.

The archive intentionally does not contain a fabricated `.pbix`. Build and save the genuine binary in Power BI Desktop.
