import unittest, pandas as pd
from pathlib import Path
R=Path(__file__).parents[1]
class ReviewAnalysisTests(unittest.TestCase):
 def test_reconciliation(self):
  s=pd.read_csv(R/'sample-data/product_reviews.csv'); e=pd.read_csv(R/'solution/outputs/reviews_enriched.csv'); self.assertEqual(len(s),len(e)); self.assertEqual(len(e),e.review_id.nunique())
 def test_controls_pass(self):
  v=pd.read_csv(R/'evidence/validation_results.csv'); self.assertEqual(len(v),10); self.assertTrue((v.status=='PASS').all())
if __name__=='__main__': unittest.main()
