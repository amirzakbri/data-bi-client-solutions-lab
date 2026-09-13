# F25 — Duplicate Customer Matching

A reproducible Python entity-resolution case study that converts inconsistent CRM, e-commerce, and support records into a governed customer master while preserving uncertain matches for human review.

## Business result

- **855** source records consolidated into **498** golden customers
- **357** duplicate records consolidated without dropping a source record
- **100.0%** auto-match precision and **91.3%** recall against held-back synthetic truth
- **92** ambiguous candidate pairs routed to review
- **8/8** QA controls passed

## Approach

1. Normalize names, emails, phones and addresses without overwriting raw data.
2. Block candidates on contact details and lightweight geographic/name keys.
3. Score exact contact, date-of-birth, fuzzy name and fuzzy address evidence.
4. Auto-link only high-confidence pairs with exact email or phone evidence.
5. Route plausible but uncertain links to a review queue.
6. Apply survivorship rules to create one golden record per governed cluster.

## Run

```bash
python src/match_customers.py --input sample-data/customer_records_raw.csv --output solution
python -m unittest discover -s tests -v
```

## Repository contents

- `src/match_customers.py` — reusable standard-library matching CLI
- `sample-data/` — messy source records and a validation-only ground-truth file
- `solution/` — golden customers, crosswalk, candidate review queue, metrics and QA evidence
- `docs/` — methodology, QA guide and stakeholder report
- `tests/` — automated reconciliation tests
- `assets/` — portfolio preview

The sample data are synthetic. Ground truth is used only to validate the matching policy, never as an input to matching.
