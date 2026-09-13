# Data Dictionary

| Table | Grain | Purpose |
|---|---|---|
| members | One row per member | Join, cancellation, status, plan, gym, channel |
| membership_monthly | One member-month | Month-end active-base reconstruction |
| checkins | One gym visit | Attendance engagement |
| payments | One monthly billing event | Paid and failed payment signals |
| plans | One membership plan | Commercial terms |
| locations | One gym | Location attributes and capacity |

Dates use ISO `YYYY-MM-DD`. `status=Cancelled` requires a cancellation date. Active risk is an operational rule, not a predicted probability.
