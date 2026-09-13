# Data Quality Audit Report

+**As of:** 2026-08-08  
+**Intended use:** customer and revenue reporting  
+**Grain:** one row per customer; one row per order
+
+## Overall assessment
+Raw tables are **not safe for direct reporting**. The governed clean views are **ready to share** after 6/6 independent controls passed.
+
+## Highest-risk findings
+
+| Finding | Evidence | Severity | Analytical risk |
+|---|---:|---|---|
+| Duplicate customer IDs | 16 affected rows | Critical | Inflated customer counts and ambiguous ownership |
+| Normalized-email duplicates | 36 affected rows | High | One person represented by multiple customer IDs |
+| Duplicate order IDs | 17 affected rows | Critical | Revenue double counting |
+| Orphan orders | 12 rows | Critical | Broken customer joins |
+| Invalid/negative order amounts | 8 rows | High | Understated revenue |
+| Amount calculation mismatches | 15 rows | High | Incorrect financial totals |
+
+## Remediation
+Use the clean views for analysis, route excluded records to owners, enforce primary-key uniqueness and foreign keys upstream, add accepted-value tests, and block future dates and amount mismatches at ingestion. Fuzzy identity resolution should remain review-based.
+
+## Caveat
+Synthetic data is used to demonstrate the workflow. Production thresholds and ownership rules must be confirmed with the client.
+