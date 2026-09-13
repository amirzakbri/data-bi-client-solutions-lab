#!/usr/bin/env python3
import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
metrics = json.loads((ROOT / "solution/quality_metrics.json").read_text())
rejected = pd.read_csv(ROOT / "solution/customers_rejected.csv")
counts = rejected["rejection_reasons"].value_counts().sort_values()
labels = [x.replace("_", " ").title() for x in counts.index]

plt.style.use("seaborn-v0_8-whitegrid")
fig = plt.figure(figsize=(14, 8), facecolor="#F4F7FB")
gs = fig.add_gridspec(3, 4, height_ratios=[0.7, 1, 4], hspace=.55, wspace=.35)
fig.suptitle("Automatic CSV Cleaner | Quality Summary", x=.06, ha="left", fontsize=22, fontweight="bold", color="#172B4D")
fig.text(.06, .91, "Config-driven validation, correction logging, and exception quarantine", fontsize=11, color="#5E6C84")
cards = [("Input rows", metrics["input_rows"]), ("Clean rows", metrics["clean_rows"]), ("Rejected", metrics["rejected_rows"]), ("Acceptance", f'{metrics["acceptance_rate_pct"]}%')]
for i, (label, value) in enumerate(cards):
    ax = fig.add_subplot(gs[1, i]); ax.axis("off")
    ax.text(.03, .78, label.upper(), fontsize=9, color="#5E6C84", fontweight="bold")
    ax.text(.03, .2, str(value), fontsize=25, color="#0052CC", fontweight="bold")
ax = fig.add_subplot(gs[2, :3])
ax.barh(labels, counts.values, color="#2684FF")
ax.set_title("Quarantined rows by primary reason", loc="left", fontweight="bold", color="#172B4D")
ax.set_xlabel("Rows")
for y, value in enumerate(counts.values): ax.text(value + .3, y, str(value), va="center", fontsize=9)
ax2 = fig.add_subplot(gs[2, 3]); ax2.axis("off")
ax2.set_title("Validated controls", loc="left", fontweight="bold", color="#172B4D")
checks = ["Required schema", "Unique customer IDs", "Required values complete", "Email format", "Allowed statuses", "Non-negative value"]
for y, item in enumerate(checks): ax2.text(0, .9-y*.14, f"✓  {item}", fontsize=10, color="#006644")
fig.savefig(ROOT / "assets/quality-summary-preview.png", dpi=170, bbox_inches="tight")
plt.close(fig)
