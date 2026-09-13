# User and QA Guide

## Purpose

The workbook calculates monthly sales commissions from approved transaction records. It is designed for Sales Operations, Finance, and sales managers who need a transparent payout process and rep-level statements.

## Workbook flow

1. **Commission Rules** — review tier thresholds, rates, bonus rate, approval value, and period.
2. **Rep Master** — maintain the roster, segment, region, and monthly quota.
3. **Sales Inputs** — paste or update one row per credited deal.
4. **Commission Calc** — review the formula-driven aggregation and tier calculations.
5. **Rep Statements** — share or export the summarized representative statements.
6. **Commission Dashboard** — review team attainment, total payout, exceptions, and payout composition.
7. **Checks** — release the payout only when the model status is `PASS`.

## Required transaction fields

Each transaction needs a unique deal ID, close date, valid rep ID, gross revenue, returns, credit percentage, bonus eligibility, approval status, and account ID. Credit percentage must be greater than 0% and no more than 100%.

## Policy interpretation

The plan uses marginal tiers, not a retroactive flat rate. A representative above quota still earns 3% on the first 80% of quota, 5% on the next 20%, and 8% only on revenue above quota. Returns reduce credited revenue before the tiers are calculated. Product bonus applies only to approved, eligible net credited revenue.

## Monthly refresh

1. Save a dated copy of the prior approved workbook.
2. Confirm the period and rates on **Commission Rules**.
3. Update the roster and quotas on **Rep Master**.
4. Replace or extend transaction rows on **Sales Inputs** without changing column definitions.
5. Resolve pending or rejected approvals with the sales manager.
6. Review unusual split-credit values and negative or excessive returns.
7. Confirm all ten controls on **Checks** return `PASS`.
8. Obtain Finance and Sales approval before payment release.

## Validation controls

- Source transaction count
- Approved transaction count
- Pending transaction count
- Approved gross credited revenue
- Approved credited returns
- Net commissionable revenue
- Rep quota reconciliation
- Total payout reconciliation
- Accelerator-rep count
- Invalid credit-percentage count

The validated portfolio baseline is stored in `solution/validated_kpis.json`. A delta below one cent is accepted to accommodate normal floating-point precision in the independently generated baseline.

## Governance notes

- Pending and rejected transactions are not paid.
- Shared-deal credit reflects only the percentage assigned to the represented seller; this file does not invent a balancing recipient.
- A change to a rate or threshold will recalculate all payouts and should require documented approval.
- The workbook supports operational review but does not replace payroll, tax, employment-contract, or legal review.
