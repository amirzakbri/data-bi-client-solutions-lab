import csv, json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class TestMatching(unittest.TestCase):
    def test_delivered_controls(self):
        with (ROOT/'solution/validation_results.csv').open() as f: rows=list(csv.DictReader(f))
        self.assertTrue(rows); self.assertTrue(all(x['status']=='PASS' for x in rows))
    def test_cli_preserves_records_and_value(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d); subprocess.run([sys.executable,str(ROOT/'src/match_customers.py'),'--input',str(ROOT/'sample-data/customer_records_raw.csv'),'--output',str(out)],check=True,capture_output=True)
            with (ROOT/'sample-data/customer_records_raw.csv').open() as f: raw=list(csv.DictReader(f))
            with (out/'customer_crosswalk.csv').open() as f: cross=list(csv.DictReader(f))
            with (out/'golden_customers.csv').open() as f: gold=list(csv.DictReader(f))
            self.assertEqual(len(raw),len(cross));self.assertEqual(len({x['source_customer_id'] for x in cross}),len(raw))
            self.assertAlmostEqual(sum(float(x['lifetime_value']) for x in raw),sum(float(x['combined_lifetime_value']) for x in gold),2)
if __name__=='__main__':unittest.main()
