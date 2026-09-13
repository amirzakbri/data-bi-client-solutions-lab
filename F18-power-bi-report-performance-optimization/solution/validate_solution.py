from pathlib import Path
import pandas as pd, json, sys
p=Path(__file__).resolve().parents[1]
f=pd.read_csv(p/'sample-data/fact_sales.csv')
b=json.loads((p/'solution/validated_kpis.json').read_text())
checks={'rows':len(f)==b['sales_lines'],'revenue':round(f.Revenue.sum(),2)==b['revenue'],'profit':round(f.GrossProfit.sum(),2)==b['gross_profit'],'units':int(f.Quantity.sum())==b['units'],'customers':f.CustomerKey.nunique()==b['customers'],'products':f.ProductKey.nunique()==b['products'],'date_keys':f.DateKey.between(20240101,20251231).all(),'no_null_revenue':f.Revenue.notna().all()}
for k,v in checks.items(): print(f'{k}: {"PASS" if v else "FAIL"}')
sys.exit(0 if all(checks.values()) else 1)
