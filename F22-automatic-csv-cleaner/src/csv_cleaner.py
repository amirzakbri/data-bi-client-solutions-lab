#!/usr/bin/env python3
"""Config-driven CSV cleaner with clean, rejected, audit, and metrics outputs."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
import pandas as pd

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def _text(value) -> str:
    return "" if pd.isna(value) else " ".join(str(value).strip().split())


def _parse_date(value: str, formats: list[str]) -> str | None:
    value = _text(value)
    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            pass
    return None


def clean_csv(input_path: Path, output_dir: Path, config_path: Path) -> dict:
    rules = json.loads(config_path.read_text(encoding="utf-8"))
    raw = pd.read_csv(input_path, dtype=str, keep_default_na=False)
    raw.columns = [rules["column_aliases"].get(c, c.strip().lower().replace(" ", "_")) for c in raw.columns]
    missing = sorted(set(rules["required_columns"]) - set(raw.columns))
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    output_dir.mkdir(parents=True, exist_ok=True)
    clean_rows, rejected_rows, audit = [], [], []
    seen: set[str] = set()

    for source_row, record in enumerate(raw.to_dict("records"), start=2):
        original = dict(record)
        row = {k: _text(v) for k, v in record.items()}
        reasons: list[str] = []

        # Safe standardization.
        for field in ("customer_id", "full_name", "email", "country", "status", "lifetime_value"):
            before = row[field]
            if field == "customer_id": row[field] = before.upper().replace(" ", "")
            elif field == "full_name": row[field] = before.title()
            elif field == "email": row[field] = before.lower().replace(" ", "")
            elif field == "country": row[field] = rules["country_map"].get(before.lower(), before.title())
            elif field == "status": row[field] = rules["status_map"].get(before, rules["status_map"].get(before.lower(), before.title()))
            elif field == "lifetime_value": row[field] = before.replace("$", "").replace(",", "")
            if row[field] != before:
                audit.append({"source_row": source_row, "customer_id": row["customer_id"], "field": field, "before": before, "after": row[field], "action": "Standardized"})

        parsed = _parse_date(row["signup_date"], rules["date_formats"])
        if parsed and parsed != row["signup_date"]:
            audit.append({"source_row": source_row, "customer_id": row["customer_id"], "field": "signup_date", "before": row["signup_date"], "after": parsed, "action": "Standardized"})
        row["signup_date"] = parsed or row["signup_date"]

        # Rules that require quarantine rather than guessing.
        for field in rules["required_columns"]:
            if not row[field]: reasons.append(f"missing_{field}")
        if row["customer_id"] in seen: reasons.append("duplicate_customer_id")
        if row["email"] and not EMAIL_RE.match(row["email"]): reasons.append("invalid_email")
        if not parsed: reasons.append("invalid_signup_date")
        if row["country"] not in set(rules["country_map"].values()): reasons.append("invalid_country")
        if row["status"] not in rules["allowed_statuses"]: reasons.append("invalid_status")
        try:
            value = round(float(row["lifetime_value"]), 2)
            row["lifetime_value"] = f"{value:.2f}"
            if value < rules["minimum_lifetime_value"]: reasons.append("negative_lifetime_value")
        except ValueError:
            reasons.append("invalid_lifetime_value")

        if reasons:
            rejected_rows.append({**original, "source_row": source_row, "rejection_reasons": ";".join(sorted(set(reasons)))})
        else:
            seen.add(row["customer_id"])
            clean_rows.append(row)

    clean = pd.DataFrame(clean_rows, columns=raw.columns)
    rejected = pd.DataFrame(rejected_rows)
    audit_df = pd.DataFrame(audit, columns=["source_row", "customer_id", "field", "before", "after", "action"])
    clean.to_csv(output_dir / "customers_clean.csv", index=False)
    rejected.to_csv(output_dir / "customers_rejected.csv", index=False)
    audit_df.to_csv(output_dir / "cleaning_audit_log.csv", index=False)

    metrics = {
        "input_rows": int(len(raw)), "clean_rows": int(len(clean)), "rejected_rows": int(len(rejected)),
        "acceptance_rate_pct": round(len(clean) / len(raw) * 100, 1) if len(raw) else 0,
        "field_corrections": int(len(audit_df)), "duplicate_ids_rejected": int(rejected.get("rejection_reasons", pd.Series(dtype=str)).str.contains("duplicate_customer_id").sum()),
        "clean_duplicate_ids": int(clean["customer_id"].duplicated().sum()) if len(clean) else 0,
        "clean_missing_required_values": int(clean[rules["required_columns"]].eq("").sum().sum()) if len(clean) else 0
    }
    (output_dir / "quality_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean and validate a CSV using JSON business rules.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(clean_csv(args.input, args.output_dir, args.config), indent=2))


if __name__ == "__main__":
    main()
