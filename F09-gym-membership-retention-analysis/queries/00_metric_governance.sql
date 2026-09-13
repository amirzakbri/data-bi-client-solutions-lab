
-- Grain and governance notes
-- members: one row per member. checkins/payments: event grain. membership_monthly: member-month grain.
-- Reporting cutoff: 2026-07-31 (Europe/Istanbul business date).
-- Observed churn = cancelled members / members joined; it is not a causal estimate.
-- Cohort retention excludes cohorts not yet old enough for each milestone denominator.
-- Active risk is an operational signal, not a prediction of certain cancellation.
