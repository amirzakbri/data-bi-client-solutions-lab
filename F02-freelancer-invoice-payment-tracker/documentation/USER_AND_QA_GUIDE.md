# User and QA Guide

## Purpose

This workbook is a reusable invoice and payment-control template for a freelancer or small service business. It provides an operational ledger, a follow-up queue, management reporting, and a visible validation layer.

## Sheet guide

| Sheet | Role |
|---|---|
| Dashboard | Headline AR and collection KPIs, aging, and top overdue clients |
| Invoice Register | Invoice inputs and formula-derived payment, balance, aging, and status fields |
| Payment Log | Receipt entry and invoice-allocation check |
| Collection Queue | Open invoices ordered by follow-up urgency |
| Client Summary | Billing and collection performance by client |
| Checks | Source ties, roll-forward controls, ID checks, and model status |

## Input rules

- Invoice ID and Payment ID must be unique identifiers.
- Every Payment Log Invoice ID must exist in Invoice Register.
- Payment dates and amounts must represent actual receipts, not promised payments.
- Split payments should use multiple Payment Log rows with the same Invoice ID.
- Do not overwrite the calculated columns in Invoice Register: Amount Paid, Balance, Days Overdue, Status, and Aging Bucket.

## Aging and priority logic

Only unpaid balance is aged. Paid invoices are assigned to `Paid`; unpaid invoices not yet past due are `Current`. Overdue balances are grouped into 1–30, 31–60, 61–90, and 90+ day buckets.

| Priority | Rule | Recommended action |
|---|---|---|
| Critical | More than 90 days overdue or balance of at least $5,000 | Call and escalate |
| High | 31–90 days overdue | Personal follow-up |
| Medium | 1–30 days overdue | Send reminder |
| Routine | Not yet overdue | Monitor due date |

## Validation controls

The Checks sheet verifies invoice count and total, payment total, the AR roll-forward, negative balances, unmatched payment IDs, missing invoice IDs, overdue balance, aging reconciliation, and collection-queue row count. The workbook is ready to share only when all ten controls return `PASS`.

## Refresh procedure

1. Update the reporting date in Checks cell B3.
2. Append invoice and payment records within the prepared ranges.
3. Copy calculated invoice formulas downward if the data range is expanded.
4. Extend dashboard and check ranges when adding more than 180 invoices or 169 payment records.
5. Review Allocation Check, Collection Queue, Dashboard, and Checks in that order.

## Portfolio baseline

The supplied synthetic baseline contains 180 invoices and 169 payment records. It reconciles to $303,327.70 invoiced, $228,210.05 collected, $75,117.65 outstanding, and $72,277.35 overdue as of 2026-08-08.

