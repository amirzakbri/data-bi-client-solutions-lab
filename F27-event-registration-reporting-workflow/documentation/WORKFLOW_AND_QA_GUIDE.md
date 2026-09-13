# Workflow and QA Guide

## Reporting flow

1. Export registration records from the booking platform as CSV.
2. Load files from the selected folder with Power Query.
3. Standardize text, dates, currencies, and business-status values.
4. Join event attributes by `event_id` where needed.
5. Load the clean table to the workbook data model.
6. Refresh the dashboard, exception queue, and validation controls.
7. Publish only after all controls pass.

## Business rules

- One row represents one registration ID.
- Confirmed registrations are the denominator for attendance rate.
- Expected revenue includes non-cancelled ticket value.
- Collected revenue is the signed amount paid; refunds reduce collected cash.
- Confirmed but unpaid bookings are high-priority finance exceptions.
- Duplicate emails require identity review but are not removed automatically.
- Records without consent must be excluded from marketing activity.
- Cancelled records cannot contribute positive collected revenue.

## QA checklist

- Source row count matches the imported table.
- Registration IDs are populated and unique in the source extract.
- Confirmed, expected-revenue, collected-cash, and attendance KPIs reconcile.
- Duplicate email count is reviewed, not silently discarded.
- Every exception has an owner and recommended action.
- Cancelled positive revenue equals zero.
- Dashboard chart and tables use the same refreshed data window.

## Handover note

The workbook includes a reproducible portfolio baseline. When replacing the sample data, preserve the column names and data types listed in the CSV header, refresh the query, and replace the expected baselines on `QA Controls` with an independently approved control total.
