# Data Model Specification

| Table | Grain | Key | Role |
|---|---|---|---|
| FactSales | One sales line | SalesLineID | Additive sales facts and dimension keys |
| DimDate | One calendar day | DateKey | Mark as date table; sort Month by MonthNumber |
| DimProduct | One product | ProductKey | Product hierarchy and brand |
| DimCustomer | One customer | CustomerKey | Region, segment, city |
| DimStore | One store | StoreKey | Store, region, manager |

Create four active one-to-many relationships from each dimension key to FactSales. Cross-filter direction must be single. Hide surrogate keys from report view. Disable Auto date/time. Do not relate dimensions to each other.
