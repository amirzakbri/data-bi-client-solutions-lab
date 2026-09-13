# Client Report — Customer Identity Resolution

## Executive finding

The three source systems contain 855 customer records, but the governed identity layer resolves them to 498 customers. The workflow consolidates 357 redundant records while preserving every source row in a traceable crosswalk.

## Data-quality findings

Exact normalized email and phone values provide the strongest safe evidence. Names and addresses vary through casing, punctuation, transliteration, abbreviations and typographical errors; fuzzy similarity alone is therefore not treated as proof. The workflow sends 92 plausible pairs to manual review instead of creating irreversible false merges.

The automated cluster result achieves 100.0% pair precision and 91.3% pair recall against validation-only truth. All 8 controls pass, including source-record preservation, unique crosswalk membership, cluster purity and monetary reconciliation.

## Recommended operating model

Use the golden table as the governed analytical customer dimension and the crosswalk for source-to-master joins. Review queued pairs using verified contact evidence before approval. Monitor precision on reviewed samples, review-queue aging, cluster-size outliers and changes in missing contact rates. Never overwrite raw source data.
