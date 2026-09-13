# Data Model

| Table | Grain | Primary key | Relationship |
|---|---|---|---|
| Clients | One row per client | Client ID | Clients 1:* Projects |
| Projects | One row per engagement | Project ID | Projects 1:* Time Entries; Projects 1:* Vendor Costs |
| Time Entries | One staff time record | Time ID | Many-to-one Projects |
| Vendor Costs | One external cost item | Vendor Cost ID | Many-to-one Projects |

Add a Date table spanning the earliest project start through the latest transaction date. Use single-direction filters from dimensions to facts. Keep Client ID and Project ID as text.

