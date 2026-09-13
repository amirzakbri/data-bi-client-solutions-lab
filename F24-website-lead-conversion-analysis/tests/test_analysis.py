from pathlib import Path
import sys, tempfile, unittest, pandas as pd
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from analyze_leads import analyze
class LeadAnalysisTests(unittest.TestCase):
    def test_reconciliation(self):
        with tempfile.TemporaryDirectory() as tmp:
            m=analyze(ROOT/'sample-data'/'website_leads.csv',ROOT/'sample-data'/'channel_spend.csv',tmp)
            df=pd.read_csv(ROOT/'sample-data'/'website_leads.csv')
            self.assertEqual(m['input_rows'],len(df)); self.assertEqual(len(df),m['unique_leads'])
            self.assertEqual(m['customers'],int(df.Converted.sum()))
            self.assertAlmostEqual(m['revenue'],df.Revenue.sum(),places=2)
    def test_governed_funnel(self):
        with tempfile.TemporaryDirectory() as tmp:
            analyze(ROOT/'sample-data'/'website_leads.csv',ROOT/'sample-data'/'channel_spend.csv',tmp)
            f=pd.read_csv(Path(tmp)/'funnel_summary.csv')
            self.assertTrue(all(f.Count.iloc[i]>=f.Count.iloc[i+1] for i in range(3)))
            self.assertTrue(f.StageConversionPct.between(0,1).all())
if __name__=='__main__': unittest.main()
