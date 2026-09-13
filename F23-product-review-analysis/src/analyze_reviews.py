from pathlib import Path
import pandas as pd, numpy as np, re, json
POS={'excellent','premium','reliable','perfectly','durable','early','fast','smooth','easy','simple','clear','intuitively','great','worth','comfortable','right'}
NEG={'poor','cheap','disappointing','defective','stopped','broke','unacceptable','late','damaged','crushed','confusing','difficult','unclear','frustrating','overpriced','not','badly','tight'}
TOPICS={'quality':['quality','materials','finish'],'durability':['durable','months','weeks','broke','stopped'],'delivery':['delivery','shipping','arrived','packaging','box'],'usability':['setup','controls','instructions','use','intuitively'],'value':['value','price','worth','overpriced'],'fit':['fit','size','comfortable','tight']}
def classify(text):
    s=str(text).lower(); words=set(re.findall(r"[a-z]+",s)); score=len(words&POS)-len(words&NEG)
    sent='positive' if score>0 else 'negative' if score<0 else 'neutral'
    counts={k:sum(x in s for x in v) for k,v in TOPICS.items()}; topic=max(counts,key=counts.get) if max(counts.values()) else 'unclassified'
    return sent,topic,max(counts.values())
def run(input_dir, output_dir):
    inp=Path(input_dir); out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    r=pd.read_csv(inp/'product_reviews.csv'); p=pd.read_csv(inp/'products.csv'); r['review_date']=pd.to_datetime(r.review_date)
    cls=r.review_text.fillna('').map(classify); r[['text_sentiment','primary_topic','topic_evidence']]=pd.DataFrame(cls.tolist(),index=r.index)
    r['rating_sentiment']=np.select([r.rating>=4,r.rating<=2],['positive','negative'],'neutral')
    r['sentiment_mismatch']=r.text_sentiment.ne(r.rating_sentiment) & r.text_sentiment.ne('neutral') & r.rating_sentiment.ne('neutral')
    r['review_month']=r.review_date.dt.to_period('M').astype(str); r.to_csv(out/'reviews_enriched.csv',index=False)
    prod=r.groupby('product_id').agg(review_count=('review_id','count'),average_rating=('rating','mean'),negative_reviews=('text_sentiment',lambda x:(x=='negative').sum()),verified_rate=('verified_purchase','mean'),helpful_votes=('helpful_votes','sum')).reset_index()
    prod['negative_rate']=prod.negative_reviews/prod.review_count
    recent=r[r.review_date>=pd.Timestamp('2026-05-01')].groupby('product_id').text_sentiment.apply(lambda x:(x=='negative').mean()).rename('recent_negative_rate')
    prior=r[r.review_date<pd.Timestamp('2026-05-01')].groupby('product_id').text_sentiment.apply(lambda x:(x=='negative').mean()).rename('prior_negative_rate')
    prod=prod.merge(recent,on='product_id',how='left').merge(prior,on='product_id',how='left').merge(p,on='product_id')
    prod['negative_rate_change']=prod.recent_negative_rate-prod.prior_negative_rate
    prod['priority_score']=(45*prod.negative_rate+25*prod.negative_rate_change.clip(lower=0)+20*np.minimum(prod.review_count/150,1)+10*(prod.average_rating<3.5)).round(1)
    prod['action_tier']=pd.cut(prod.priority_score,[-1,24.9,39.9,100],labels=['Monitor','Investigate','Urgent'])
    prod.sort_values('priority_score',ascending=False).to_csv(out/'product_priority_queue.csv',index=False)
    topic=r[r.primary_topic!='unclassified'].groupby(['primary_topic','text_sentiment']).size().unstack(fill_value=0).reset_index(); topic.to_csv(out/'topic_sentiment_summary.csv',index=False)
    monthly=r.groupby('review_month').agg(review_count=('review_id','count'),average_rating=('rating','mean'),negative_rate=('text_sentiment',lambda x:(x=='negative').mean())).reset_index(); monthly.to_csv(out/'monthly_trend.csv',index=False)
    cats=r.merge(p[['product_id','category']],on='product_id').groupby('category').agg(review_count=('review_id','count'),average_rating=('rating','mean'),negative_rate=('text_sentiment',lambda x:(x=='negative').mean())).reset_index(); cats.to_csv(out/'category_summary.csv',index=False)
    k={'review_count':int(len(r)),'unique_reviews':int(r.review_id.nunique()),'product_count':int(r.product_id.nunique()),'average_rating':round(r.rating.mean(),3),'negative_text_reviews':int((r.text_sentiment=='negative').sum()),'negative_text_rate':round((r.text_sentiment=='negative').mean(),4),'unclassified_reviews':int((r.primary_topic=='unclassified').sum()),'sentiment_mismatches':int(r.sentiment_mismatch.sum()),'urgent_products':int((prod.action_tier=='Urgent').sum()),'investigate_products':int((prod.action_tier=='Investigate').sum())}
    json.dump(k,open(out/'validated_kpis.json','w'),indent=2); return k
if __name__=='__main__': run('sample-data','solution/outputs')
