# Runbook

+1. Load the raw CSVs into the two raw tables.
+2. Run `queries/01_profile_and_audit.sql`.
+3. Review rows in issue views where any flag equals 1.
+4. Export clean views only after validation controls pass.
+5. Never delete raw rows; resolve exceptions in the source system.
+