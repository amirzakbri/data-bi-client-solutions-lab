# F23 — Product Review Analysis

A reproducible voice-of-customer analytics workflow for turning raw product reviews into governed sentiment, issue themes, trends, and a product intervention queue.

## Business question
Which products and recurring customer issues should product and operations teams address first?

## Headline results
- **3,600** unique reviews across **30 products**
- **3.73/5** average star rating
- **18.9%** negative text-sentiment rate
- **4 urgent** and **9 investigate** products
- All 10 validation controls pass

## Run
```bash
pip install -r requirements.txt
python src/analyze_reviews.py
python -m unittest discover -s tests -v
```

## Repository structure
- `sample-data/` — synthetic products and reviews
- `src/` — reusable analysis pipeline
- `solution/outputs/` — enriched reviews, trends, issue summaries, priority queue
- `documentation/` — methodology, report, and operating guide
- `evidence/` — independent reconciliation controls
- `assets/` — portfolio preview

## Governance
Text sentiment is lexicon-based and interpretable. It is not a claim of human-level language understanding. Sparse, sarcastic, multilingual, and ambiguous reviews require human review. Synthetic data is used throughout.
