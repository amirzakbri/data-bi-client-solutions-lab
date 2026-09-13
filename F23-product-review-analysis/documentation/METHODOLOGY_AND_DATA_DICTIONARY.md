# Methodology and Data Dictionary

## Grain and period
One row per unique review from 2025-08-01 through 2026-07-31. `review_id` is the primary key; `product_id` joins the product catalog.

## Metrics
- **Average rating:** arithmetic mean of 1–5 star ratings.
- **Negative text rate:** negative text classifications / all reviews.
- **Recent negative rate:** negative text rate from 2026-05-01 onward.
- **Negative-rate change:** recent rate minus the earlier-period rate.
- **Priority score:** 45×negative rate + 25×positive recent deterioration + up to 20 points for review volume + 10 points when average rating is below 3.5.
- **Action tier:** Monitor <25; Investigate 25–39.9; Urgent ≥40.

## Classification
Normalized English words are scored against transparent positive and negative lexicons. Topic evidence is assigned from keyword dictionaries for quality, durability, delivery, usability, value, and fit. Reviews without topic evidence are retained as `unclassified`.
