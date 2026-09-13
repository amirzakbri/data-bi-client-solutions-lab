# User and QA Guide

## Run the cleaner

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/csv_cleaner.py sample-data/customers_messy.csv \
  --config config/cleaning_rules.json \
  --output-dir solution
```

## Outputs

- `customers_clean.csv`: accepted records, standardized for analysis
- `customers_rejected.csv`: quarantined source records with rejection reasons
- `cleaning_audit_log.csv`: field-level before/after evidence
- `quality_metrics.json`: machine-readable run controls

## Business-rule approach

Safe, deterministic fixes—trimming whitespace, normalizing casing, mapping approved country/status aliases, parsing approved date formats, and removing currency symbols—are automated. Ambiguous or analytically unsafe values are never guessed; those rows are quarantined with a reason.

To reuse the tool for another client, edit `config/cleaning_rules.json` and align the required fields in `src/csv_cleaner.py`. Keep the raw file unchanged for traceability.

## Validation

Run:

```bash
python -m unittest discover -s tests -v
```

The automated suite verifies the published output baseline, confirms that clean keys are unique and complete, checks audit-output creation, and confirms that missing schema fails fast.
