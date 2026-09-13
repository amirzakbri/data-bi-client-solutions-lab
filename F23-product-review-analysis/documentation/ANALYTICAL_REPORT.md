# Analytical Report

## Decision
Product leadership should prioritize products with high negative-text rates, meaningful recent deterioration, sufficient review volume, and concentrated issue themes.

## Findings
- The dataset contains 3,600 unique reviews for 30 products over 12 months.
- Average star rating is 3.73; text classification identifies 682 negative reviews (18.9%).
- 4 products meet the urgent threshold and 9 require investigation.
- Rating/text mismatches (70) remain visible rather than forcing agreement between two different signals.

## Recommendation
Begin with the highest priority product in `product_priority_queue.csv`. Review its verbatim negative feedback by primary topic, assign a product or operations owner, implement one corrective action, and compare its next 30-day negative rate with the governed baseline.

## Limitations
The data is synthetic. Rule-based sentiment supports reproducibility and auditability but can miss negation, sarcasm, mixed sentiment, and context. Topic labels indicate keyword evidence, not causal proof. Review volume and verified-purchase status should be considered before acting on small segments.
