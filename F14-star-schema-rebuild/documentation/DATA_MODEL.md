# Data Model

+## Grain
+`FactSales` contains one row per order line. Its grain must not change during reporting.
+
+## Relationships
+
+| From | To | Cardinality | Filter direction |
+|---|---|---:|---|
+| DimDate[DateKey] | FactSales[DateKey] | 1:* | Single |
+| DimCustomer[CustomerKey] | FactSales[CustomerKey] | 1:* | Single |
+| DimProduct[ProductKey] | FactSales[ProductKey] | 1:* | Single |
+| DimStore[StoreKey] | FactSales[StoreKey] | 1:* | Single |
+
+All dimension keys are unique and nonblank. All fact foreign keys resolve. There are no dimension-to-dimension or bidirectional relationships. Mark `DimDate[Date]` as the date table.
+
+## Why the original model was unsafe
+The original export repeated customer, product, store, and calendar labels on every sales line. That increased file size, allowed conflicting labels for the same business key, encouraged direct column summation, and made relationship design ambiguous. The star schema centralizes descriptive attributes and keeps additive measures at transaction-line grain.
+