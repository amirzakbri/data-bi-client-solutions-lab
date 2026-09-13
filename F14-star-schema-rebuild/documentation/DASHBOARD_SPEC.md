# Dashboard Specification
+
+Audience: retail commercial manager. Reporting period: 1 January–31 July 2026.
+
+## Page 1 — Executive Sales
+Hero cards: Total Revenue, Gross Profit, Gross Margin %, Orders, Units Sold.
+Visuals: monthly revenue trend; revenue by category; revenue by channel; top products table.
+Filters: month, category, segment, channel.
+
+## Page 2 — Model Health
+Cards: fact rows, dimension rows, orphan keys, duplicate dimension keys, checks passed.
+Visuals: before/after model diagram, relationship register, reconciliation matrix.
+
+All slicers should originate in dimensions. Never expose raw foreign keys to report users.
+