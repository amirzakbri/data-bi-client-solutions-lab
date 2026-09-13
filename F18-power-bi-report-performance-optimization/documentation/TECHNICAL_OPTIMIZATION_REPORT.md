# Technical Optimization Report

## Technical summary
The optimization retains the exact 120,000-line business baseline while removing the principal sources of avoidable report latency. The controlled benchmark trace shows a 70.8% faster initial render and 68–77% improvement across tested interactions.

## Root causes and repairs
1. **Wide flat model:** repeated customer, product, store, and date text increased cardinality. Replaced with one fact and four conformed dimensions.
2. **Ambiguous filter paths:** four bidirectional relationships increased propagation work. Replaced with active, one-to-many, single-direction relationships.
3. **Iterator-heavy DAX:** repeated `SUMX` and `FILTER(ALL(Fact))` forced formula-engine work. Replaced with additive columns and dimension filters.
4. **Calculated-column load:** seven fact calculated columns expanded refresh and model size. Business logic moved upstream; only governed GrossProfit remains materialized.
5. **Non-folding steps:** late type changes and row-by-row logic were replaced by early typing, projection, and source-side materialization guidance.
6. **Visual overload:** 27 visuals and overlapping slicers were reduced to 12 decision-relevant visuals.

## Evidence
- Initial page: 4,870 ms to 1,420 ms.
- Slicer interaction: 1,530 ms to 460 ms.
- Refresh transformation: 12,800 ms to 4,100 ms.
- Estimated dataframe footprint: 104.9 MB to 10.2 MB. This is a reproducible proxy, not a VertiPaq Analyzer export.

## Interpretation and caveat
The benchmark CSV is a controlled reference trace for this portfolio scenario. Actual timings depend on hardware, Desktop version, cache state, connector, and PBIX implementation. The guide requires cold/warm runs and median reporting before production sign-off.

## Recommendation
Rebuild in Desktop, capture Performance Analyzer traces, inspect Server Timings and VertiPaq Analyzer, and accept only if all KPI controls pass and the median initial render stays below 1.5 seconds on the agreed test machine.
