# Operational Runbook

1. Replace source CSVs with refreshed extracts using the documented grains.
2. Load the six tables into SQLite and rebuild indexes.
3. Set one explicit reporting cutoff and align all recent-activity windows.
4. Execute the SQL pack in numeric order.
5. Confirm every validation control returns PASS before publishing.
6. Send Critical and High queue items to membership operations; do not contact cancelled members.
7. Record outreach outcomes separately so future analyses can evaluate intervention effectiveness.
