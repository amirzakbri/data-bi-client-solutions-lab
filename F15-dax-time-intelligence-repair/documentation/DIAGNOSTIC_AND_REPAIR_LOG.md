# Diagnostic and Repair Log

| Defect | Impact | Repair |
|---|---|---|
| Fact date used in time functions | Missing dates make shifting unreliable | Use `DimDate[Date]` exclusively |
| Incomplete calendar | Prior periods return blanks or partial totals | Add contiguous calendar covering all dates |
| Date table not marked | Time functions lack governed calendar semantics | Mark `DimDate` as date table |
| Bidirectional date relationship | Ambiguous filter propagation | Use `DimDate` 1:* `Sales`, single direction |
| `/` used for growth | Divide-by-zero errors | Use `DIVIDE` |
| Rolling window anchored inconsistently | Window changes unexpectedly by visual | Anchor to last visible date |
| Latest month ignores completion | Partial month can be presented as final | Define explicit latest-complete-period rule |

The repaired model has one active relationship: `DimDate[Date]` (1) to `Sales[OrderDate]` (*) with single-direction filtering.
