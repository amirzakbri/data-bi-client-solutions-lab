# Validation Report

## Dataset and grain

The input represents one customer account per row. `customer_id` is the required business key. The synthetic export contains 550 rows and seven business fields.

## Results

| Control | Result | Status |
|---|---:|:---:|
| Input rows | 550 | PASS |
| Clean rows + rejected rows | 500 + 50 = 550 | PASS |
| Acceptance rate | 90.9% | INFO |
| Duplicate IDs in clean output | 0 | PASS |
| Missing required values in clean output | 0 | PASS |
| Duplicate source IDs quarantined | 22 | PASS |
| Field-level corrections logged | 2,504 | PASS |
| Automated tests | 2 of 2 | PASS |

## Exceptions

Twenty-two repeated customer IDs were quarantined. The remaining 28 rejected records are evenly distributed across malformed email, invalid date, unknown country, invalid status, negative lifetime value, missing name, and nonnumeric lifetime value—four rows in each category.

## Analytical risk and remediation

Duplicate keys would overcount customers and lifetime value; invalid domains would fragment segmentation; invalid dates would break cohort reporting. The cleaner therefore blocks these records from downstream use and preserves them for source-owner correction. Stable rules are configuration-controlled, while ambiguous values remain in the exception queue.
