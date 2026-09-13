#!/usr/bin/env python3
"""Generate a weekly KPI CSV, management HTML, and plaintext email from daily CSV."""
import argparse, csv, html, json
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

TARGETS={'revenue':48000,'orders':560,'conversion':.033,'aov':84,'gross_margin':.42,'refund_rate':.045,'on_time_rate':.94}
DIRECTION={'revenue':1,'orders':1,'conversion':1,'aov':1,'gross_margin':1,'refund_rate':-1,'on_time_rate':1}
LABELS={'revenue':'Revenue','orders':'Orders','conversion':'Conversion Rate','aov':'Average Order Value','gross_margin':'Gross Margin','refund_rate':'Refund Rate','on_time_rate':'On-Time Fulfilment'}

def aggregate(rows,start,end):
    selected=[r for r in rows if start<=date.fromisoformat(r['date'])<=end]
    sums=defaultdict(float)
    for r in selected:
        for k in ('sessions','orders','revenue','cogs','refund_orders','on_time_orders'): sums[k]+=float(r[k])
    revenue,orders,sessions=sums['revenue'],sums['orders'],sums['sessions']
    return {'revenue':revenue,'orders':int(orders),'sessions':int(sessions),'conversion':orders/sessions,'aov':revenue/orders,'gross_margin':(revenue-sums['cogs'])/revenue,'refund_rate':sums['refund_orders']/orders,'on_time_rate':sums['on_time_orders']/orders}

def classify(key,value):
    target=TARGETS[key]
    if DIRECTION[key]>0: return 'On Track' if value>=target else ('Watch' if value>=target*.95 else 'Action')
    return 'On Track' if value<=target else ('Watch' if value<=target*1.1 else 'Action')

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--week-ending',required=True);p.add_argument('--output-dir',required=True);a=p.parse_args()
    out=Path(a.output_dir);out.mkdir(parents=True,exist_ok=True);end=date.fromisoformat(a.week_ending);start=end-timedelta(days=6);prev_end=start-timedelta(days=1);prev_start=prev_end-timedelta(days=6)
    with open(a.input,newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
    curr,prev=aggregate(rows,start,end),aggregate(rows,prev_start,prev_end);results=[]
    for k in TARGETS: results.append({'metric':LABELS[k],'current':curr[k],'previous':prev[k],'wow_change':(curr[k]-prev[k])/abs(prev[k]),'target':TARGETS[k],'target_variance':curr[k]-TARGETS[k],'status':classify(k,curr[k])})
    with open(out/'weekly_kpis.csv','w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=results[0]);w.writeheader();w.writerows(results)
    rows_html=''.join(f"<tr><td>{html.escape(x['metric'])}</td><td>{x['current']:,.2f}</td><td>{x['wow_change']:.1%}</td><td>{x['target']:,.2f}</td><td class='{x['status'].lower().replace(' ','-')}'>{x['status']}</td></tr>" for x in results)
    page=f"""<!doctype html><meta charset='utf-8'><title>Weekly KPI Summary</title><style>body{{font:15px Arial;max-width:980px;margin:35px auto;color:#24353f}}h1{{color:#153447}}table{{width:100%;border-collapse:collapse}}th{{background:#153447;color:white}}td,th{{padding:11px;border-bottom:1px solid #ccd9dd;text-align:right}}td:first-child,th:first-child{{text-align:left}}.action{{color:#b42318;font-weight:bold}}.watch{{color:#a15c00;font-weight:bold}}.on-track{{color:#14704a;font-weight:bold}}</style><h1>Weekly KPI Summary</h1><p>Complete week {start} to {end} · Europe/Istanbul</p><table><tr><th>KPI</th><th>Current</th><th>WoW</th><th>Target</th><th>Status</th></tr>{rows_html}</table>"""
    (out/'management_summary.html').write_text(page,encoding='utf-8')
    actions=[x for x in results if x['status']=='Action'];email=[f"Subject: Weekly KPI summary | Week ending {end}","",f"Complete reporting week: {start} to {end}",f"Revenue: ${curr['revenue']:,.0f} ({(curr['revenue']/prev['revenue']-1):+.1%} WoW)",f"Orders: {curr['orders']:,} ({(curr['orders']/prev['orders']-1):+.1%} WoW)",f"KPIs requiring action: {len(actions)}"]+[f"- {x['metric']}: {x['current']:.2%}" if 'Rate' in x['metric'] or 'Margin' in x['metric'] or 'Fulfilment' in x['metric'] else f"- {x['metric']}: {x['current']:,.2f}" for x in actions]+["","See the attached workbook/HTML for definitions, targets, and QA controls."]
    (out/'weekly_email.txt').write_text('\n'.join(email),encoding='utf-8');(out/'run_metadata.json').write_text(json.dumps({'generated_at':datetime.now().isoformat(timespec='seconds'),'week_start':str(start),'week_end':str(end),'timezone':'Europe/Istanbul','source_rows':len(rows)},indent=2),encoding='utf-8')

if __name__=='__main__':main()
