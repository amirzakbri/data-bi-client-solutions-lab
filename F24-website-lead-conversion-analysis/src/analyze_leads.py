from pathlib import Path
import argparse, json
import pandas as pd
import numpy as np

def safe_div(a,b):
    return a/b if b else 0.0

def analyze(leads_path, spend_path, output_dir):
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(leads_path,parse_dates=['CreatedDate'])
    spend=pd.read_csv(spend_path)
    required={'LeadID','CreatedDate','LeadSource','LandingPage','Device','FirstResponseHours','Qualified','Opportunity','Converted','Revenue'}
    missing=required-set(df.columns)
    if missing: raise ValueError(f'Missing columns: {sorted(missing)}')
    if df['LeadID'].duplicated().any(): raise ValueError('LeadID must be unique')
    if ((df['Converted']==0)&(df['Revenue']!=0)).any(): raise ValueError('Revenue must belong only to converted leads')
    if ((df['Converted']>df['Opportunity'])|(df['Opportunity']>df['Qualified'])).any(): raise ValueError('Invalid funnel sequence')

    def segment(col):
        g=df.groupby(col,dropna=False).agg(Leads=('LeadID','count'),Qualified=('Qualified','sum'),Opportunities=('Opportunity','sum'),Customers=('Converted','sum'),Revenue=('Revenue','sum'),MedianResponseHours=('FirstResponseHours','median')).reset_index()
        g['LeadToCustomerPct']=g['Customers']/g['Leads']
        g['RevenuePerLead']=g['Revenue']/g['Leads']
        g['QualificationPct']=g['Qualified']/g['Leads']
        return g.sort_values(['LeadToCustomerPct','Leads'],ascending=[False,False])

    by_source=segment('LeadSource').merge(spend,on='LeadSource',how='left')
    by_source['MarketingSpend']=by_source['MarketingSpend'].fillna(0)
    by_source['CostPerLead']=np.where(by_source['MarketingSpend']>0,by_source['MarketingSpend']/by_source['Leads'],0)
    by_source['CustomerAcquisitionCost']=np.where(by_source['Customers']>0,by_source['MarketingSpend']/by_source['Customers'],0)
    by_source['ROAS']=np.where(by_source['MarketingSpend']>0,by_source['Revenue']/by_source['MarketingSpend'],0)
    by_page=segment('LandingPage'); by_device=segment('Device')
    bands=pd.cut(df['FirstResponseHours'],[-.01,2,8,24,float('inf')],labels=['≤2 hours','2–8 hours','8–24 hours','>24 hours'])
    temp=df.assign(ResponseBand=bands)
    by_response=temp.groupby('ResponseBand',observed=False).agg(Leads=('LeadID','count'),Customers=('Converted','sum'),Revenue=('Revenue','sum')).reset_index()
    by_response['LeadToCustomerPct']=by_response['Customers']/by_response['Leads']
    monthly=df.assign(Month=df['CreatedDate'].dt.to_period('M').astype(str)).groupby('Month').agg(Leads=('LeadID','count'),Qualified=('Qualified','sum'),Opportunities=('Opportunity','sum'),Customers=('Converted','sum'),Revenue=('Revenue','sum')).reset_index()
    monthly['LeadToCustomerPct']=monthly['Customers']/monthly['Leads']
    funnel=pd.DataFrame({'Stage':['Leads','Qualified','Opportunities','Customers'],'Count':[len(df),int(df.Qualified.sum()),int(df.Opportunity.sum()),int(df.Converted.sum())]})
    funnel['StageConversionPct']=[1, safe_div(funnel.Count[1],funnel.Count[0]),safe_div(funnel.Count[2],funnel.Count[1]),safe_div(funnel.Count[3],funnel.Count[2])]
    funnel['CumulativeConversionPct']=funnel.Count/funnel.Count.iloc[0]
    queue=df[(df['Converted']==0)&((df['Opportunity']==1)|(df['FirstResponseHours']>24))].copy()
    queue['Priority']=np.select([(queue.Opportunity==1)&(queue.FirstResponseHours>24),queue.Opportunity==1,queue.FirstResponseHours>24],['Critical','High','Watch'],'Review')
    queue=queue.sort_values(['Priority','FirstResponseHours'],ascending=[True,False])

    for name,data in [('conversion_by_source.csv',by_source),('conversion_by_landing_page.csv',by_page),('conversion_by_device.csv',by_device),('conversion_by_response_time.csv',by_response),('monthly_funnel.csv',monthly),('funnel_summary.csv',funnel),('lead_follow_up_queue.csv',queue)]:
        data.to_csv(out/name,index=False)
    metrics={'input_rows':len(df),'unique_leads':df.LeadID.nunique(),'qualified_leads':int(df.Qualified.sum()),'opportunities':int(df.Opportunity.sum()),'customers':int(df.Converted.sum()),'lead_to_customer_pct':round(df.Converted.mean()*100,2),'revenue':round(df.Revenue.sum(),2),'revenue_per_lead':round(df.Revenue.sum()/len(df),2),'median_response_hours':round(df.FirstResponseHours.median(),1),'open_follow_up_rows':len(queue),'coverage_start':str(df.CreatedDate.min().date()),'coverage_end':str(df.CreatedDate.max().date())}
    (out/'validated_kpis.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
    return metrics

if __name__=='__main__':
    p=argparse.ArgumentParser(description='Analyze website lead conversion and produce governed outputs.')
    p.add_argument('--leads',default='sample-data/website_leads.csv'); p.add_argument('--spend',default='sample-data/channel_spend.csv'); p.add_argument('--output',default='solution')
    a=p.parse_args(); print(json.dumps(analyze(a.leads,a.spend,a.output),indent=2))
