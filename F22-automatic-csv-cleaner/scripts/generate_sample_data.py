#!/usr/bin/env python3
"""Generate a deterministic synthetic customer export with controlled defects."""
from pathlib import Path
import random
import pandas as pd

random.seed(22)
ROOT = Path(__file__).resolve().parents[1]
first = ["Ada", "Noah", "Mia", "Liam", "Sofia", "Ethan", "Leyla", "Oliver", "Emma", "Lucas"]
last = ["Stone", "Martin", "Kaya", "Brown", "Demir", "Wilson", "Yilmaz", "Miller", "Taylor", "Clark"]
countries = ["USA", "us", "United States", "UK", "u.k.", "Turkey", "Türkiye", "DE", "Germany", "FR", "France"]
statuses = ["active", "ACTIVE", "Inactive", "IN-ACTIVE", "prospect", "lead"]
rows = []
for i in range(1, 501):
    fn, ln = random.choice(first), random.choice(last)
    date = pd.Timestamp("2025-01-01") + pd.Timedelta(days=random.randint(0, 570))
    fmt = random.choice(["%Y-%m-%d", "%d/%m/%Y", "%d-%b-%Y"])
    value = round(random.uniform(20, 4500), 2)
    rows.append({
        "Customer ID": f"c-{i:04d}" if i % 7 else f" C- {i:04d} ",
        "Full Name": f" {fn.lower()}  {ln.upper()} " if i % 5 == 0 else f"{fn} {ln}",
        "E-mail": f" {fn}.{ln}{i}@Example.COM " if i % 6 == 0 else f"{fn}.{ln}{i}@example.com",
        "Signup Date": date.strftime(fmt), "Country": random.choice(countries),
        "Account Status": random.choice(statuses), "Lifetime Value": f"${value:,.2f}" if i % 4 == 0 else str(value)
    })

# 22 duplicates and 28 invalid records, deliberately appended for auditability.
for i in range(1, 23):
    duplicate = dict(rows[i * 3])
    duplicate["Full Name"] = " " + duplicate["Full Name"] + " "
    rows.append(duplicate)
for j in range(28):
    i = j * 11
    bad = dict(rows[i])
    bad["Customer ID"] = f"BAD-{j+1:03d}"
    defect = j % 7
    if defect == 0: bad["E-mail"] = "not-an-email"
    elif defect == 1: bad["Signup Date"] = "31/31/2026"
    elif defect == 2: bad["Country"] = "Atlantis"
    elif defect == 3: bad["Account Status"] = "Blocked"
    elif defect == 4: bad["Lifetime Value"] = "-50"
    elif defect == 5: bad["Full Name"] = ""
    else: bad["Lifetime Value"] = "unknown"
    rows.append(bad)

out = ROOT / "sample-data/customers_messy.csv"
out.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(rows).to_csv(out, index=False)
print(f"Wrote {len(rows)} rows to {out}")
