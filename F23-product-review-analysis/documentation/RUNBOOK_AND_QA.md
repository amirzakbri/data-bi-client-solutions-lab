# Runbook and QA

1. Place `product_reviews.csv` and `products.csv` in `sample-data/`.
2. Confirm unique review IDs, valid 1–5 ratings, parseable dates, and product-key coverage.
3. Run `python src/analyze_reviews.py` from the project root.
4. Review `solution/outputs/product_priority_queue.csv` and supporting topic/trend outputs.
5. Run `pytest -q` and inspect `evidence/validation_results.csv`.

Human review is required for unclassified text, rating/text mismatches, and any product decision based on a small review count. Rebaseline thresholds when the catalog, language mix, or reporting window changes.
