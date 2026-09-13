# Data Model

Recommended Power BI star schema:

```text
DimProperty (1) ── (*) DimUnit (1) ── (*) FactRentLedger
                                  └── tenant attributes in DimUnit/Lease
DimDate     (1) ──────────────────── (*) FactRentLedger
```

## Tables

- `DimProperty`: one row per property; property name, district, manager, and unit count.
- `DimUnit`: one row per unit/lease combination; unit, rent, occupancy, tenant, and lease dates.
- `FactRentLedger`: one row per monthly invoice; billed rent, cash received, balance, status, days late, and aging bucket.
- `DimDate`: continuous calendar related to `FactRentLedger[due_date]`.

Use single-direction one-to-many relationships. Keep monetary measures in the fact table and descriptive slicing fields in dimensions.
