# F12 — Salon Appointment Power BI Dashboard

## Client problem
A growing salon exports appointment records but lacks a reliable view of revenue, completion, cancellations, no-shows, service demand, and staff performance.

## Solution
An import-ready Power BI dashboard specification built on a star schema with documented Power Query logic, reusable DAX measures, a custom theme, validated KPIs, and a decision-focused dashboard blueprint.

## Business questions
- Is revenue improving month over month?
- Which services and staff generate completed revenue?
- Where are cancellation and no-show risks concentrated?
- Which booking channels and time slots drive demand?

## Validated headline results
- **1,231** appointments
- **$62,989.10** completed revenue
- **79.7%** completion rate
- **82** no-shows and **168** cancellations
- **$64.21** average completed ticket

## Repository contents
- `sample-data/` — appointments and dimension tables
- `solution/F12_Salon_Appointment_Model.pbix` — validated Power BI semantic model exported from Power BI Service
- `solution/F12_Salon_Appointment_Performance_Dashboard.pdf` — two-page Power BI Service report export
- `solution/measures.dax` — production-ready measures
- `solution/FactAppointments.pq` — typed Power Query import
- `solution/salon-editorial-theme.json` — Power BI theme
- `solution/validated_kpis.json` — reconciliation baseline
- `documentation/` — model, dashboard specification, and build guide
- `assets/dashboard-preview.png` — portfolio preview

## Report implementation
The semantic model and the Executive Overview dashboard were completed in Power BI Service. The portfolio screenshot documents the finished report, while the included PBIX preserves the downloadable semantic model.

To reproduce or extend the solution:
1. Import the four CSV files.
2. Rename tables to FactAppointments, DimStaff, DimService, and DimCustomer.
3. Create DimDate and relationships exactly as documented.
4. Add the DAX measures and import the theme.
5. Build the report using `DASHBOARD_SPEC.md`.
6. Reconcile the headline cards to `validated_kpis.json`.

## Tools
Power BI Service, Power Query, DAX, star-schema modeling, CSV, and independent KPI validation.

## Data
Synthetic and privacy-safe; designed to represent a realistic six-month salon operation.
