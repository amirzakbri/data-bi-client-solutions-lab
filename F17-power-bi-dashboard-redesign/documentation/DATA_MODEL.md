# Data Model

`Sales` is at one row per order. In Power BI, create conformed `DimDate`, `DimProduct`, `DimRegion`, `DimChannel`, and `DimSegment` tables. Each dimension filters `Sales` through a one-to-many, single-direction relationship. Mark `DimDate[Date]` as the date table and use dimension fields for every slicer.

The redesign intentionally keeps the same governed fact rows and measures as the baseline. This prevents a presentation change from disguising a data-model change.
