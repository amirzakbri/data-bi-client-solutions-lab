# Matching Methodology and QA

## Grain and fields

The raw table has one row per source-system customer record. A person may appear in multiple systems. Matching uses normalized email, phone, name, address, city and date of birth. Monetary values do not influence identity.

## Decision policy

| Band | Rule | Action |
|---|---|---|
| Auto-match | Score at least 0.92 and exact normalized email or phone | Link automatically |
| Review | Score from 0.72 to below 0.92 | Preserve as candidate for a reviewer |
| No match | Below 0.72 | Keep separate |

Candidate generation uses exact contact blocks plus compact name/city and address/city blocks, preventing a full Cartesian comparison. Connected components form clusters from auto-approved links only.

## Survivorship

The latest populated value is selected, with CRM preferred on ties. All source IDs remain in the crosswalk. Lifetime value is summed across source records for reconciliation purposes; in a production implementation, business ownership must decide whether source values are additive.

## Controls

The validation suite checks record preservation, crosswalk uniqueness, cluster purity, precision, recall, cluster counts, lifetime-value reconciliation and review-queue retention. Ground truth is synthetic and isolated from the algorithm.

## Production safeguards

Encrypt or tokenize personal data, restrict reviewer access, record reviewer decisions, version the scoring policy, and require sampled precision checks before threshold changes. Fuzzy-only links should not be auto-merged.
