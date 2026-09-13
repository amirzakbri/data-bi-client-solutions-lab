import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from csv_cleaner import clean_csv


class CleanerTests(unittest.TestCase):
    def test_portfolio_sample_reconciles(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder)
            metrics = clean_csv(ROOT / "sample-data/customers_messy.csv", out, ROOT / "config/cleaning_rules.json")
            expected = json.loads((ROOT / "solution/quality_metrics.json").read_text())
            self.assertEqual(metrics, expected)
            self.assertEqual(metrics["clean_duplicate_ids"], 0)
            self.assertEqual(metrics["clean_missing_required_values"], 0)
            self.assertTrue((out / "cleaning_audit_log.csv").exists())

    def test_missing_schema_fails_fast(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "bad.csv"
            source.write_text("customer_id,full_name\nC1,Ada\n")
            with self.assertRaisesRegex(ValueError, "Missing required columns"):
                clean_csv(source, Path(folder) / "out", ROOT / "config/cleaning_rules.json")


if __name__ == "__main__":
    unittest.main()
