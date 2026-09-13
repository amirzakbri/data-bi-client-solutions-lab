from __future__ import annotations
import argparse, csv, json, re, unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

def norm(v):
    v=unicodedata.normalize("NFKD",str(v or "")).encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9]","",v)
def email(v): return str(v or "").strip().lower().replace(" ","")
def phone(v):
    d=re.sub(r"\D","",str(v or "")); return d[-10:] if len(d)>=10 else d
def similarity(a,b):
    a,b=norm(a),norm(b); return SequenceMatcher(None,a,b).ratio() if a and b else 0
def score(a,b):
    em=bool(email(a["email"]) and email(a["email"])==email(b["email"]))
    ph=bool(phone(a["phone"]) and phone(a["phone"])==phone(b["phone"]))
    dob=bool(a["date_of_birth"] and a["date_of_birth"]==b["date_of_birth"])
    ns,ads=similarity(a["full_name"],b["full_name"]),similarity(a["address"],b["address"])
    city=norm(a["city"])==norm(b["city"])
    s=min((.96+(.02 if em and ph else 0)+(.01 if dob else 0)) if em or ph else .56*ns+.24*ads+.12*dob+.08*city,.999)
    return s,em,ph,dob,ns,ads
class UF:
    def __init__(self,n): self.p=list(range(n))
    def find(self,x):
        while self.p[x]!=x:self.p[x]=self.p[self.p[x]];x=self.p[x]
        return x
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a!=b:self.p[b]=a
def write(path,rows):
    if not rows:return
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def run(input_path,output):
    output.mkdir(parents=True,exist_ok=True)
    with input_path.open(encoding="utf-8") as f: rows=list(csv.DictReader(f))
    blocks=defaultdict(set)
    for i,x in enumerate(rows):
        keys=[]
        if email(x["email"]):keys.append("e:"+email(x["email"]))
        if phone(x["phone"]):keys.append("p:"+phone(x["phone"]))
        keys += ["n:"+norm(x["full_name"])[:5]+"|"+norm(x["city"]),"a:"+norm(x["address"])[:6]+"|"+norm(x["city"])]
        for k in keys:blocks[k].add(i)
    seen=set();pairs=[];uf=UF(len(rows))
    for ids in blocks.values():
        ids=sorted(ids)
        for z,a in enumerate(ids):
            for b in ids[z+1:]:
                if (a,b) in seen:continue
                seen.add((a,b));s,em,ph,dob,ns,ads=score(rows[a],rows[b])
                if s<.72:continue
                d="AUTO_MATCH" if s>=.92 and (em or ph) else "REVIEW"
                pairs.append(dict(left_id=rows[a]["source_customer_id"],right_id=rows[b]["source_customer_id"],score=f"{s:.4f}",decision=d,email_exact=em,phone_exact=ph,dob_exact=dob,name_similarity=f"{ns:.4f}",address_similarity=f"{ads:.4f}"))
                if d=="AUTO_MATCH":uf.union(a,b)
    groups=defaultdict(list)
    for i,x in enumerate(rows):groups[uf.find(i)].append(x)
    membership=[];gold=[]
    for k,g in enumerate(sorted(groups.values(),key=lambda z:min(x["source_customer_id"] for x in z)),1):
        gid=f"GC{k:04d}"
        def choose(field):
            vals=[x[field] for x in sorted(g,key=lambda z:(z["updated_at"],z["source_system"]=="CRM"),reverse=True) if x[field]]
            return vals[0] if vals else ""
        gold.append(dict(golden_customer_id=gid,full_name=choose("full_name").title(),email=email(choose("email")),phone=phone(choose("phone")),address=choose("address"),city=choose("city"),country=choose("country"),postal_code=choose("postal_code"),date_of_birth=choose("date_of_birth"),source_record_count=len(g),source_system_count=len(set(x["source_system"] for x in g)),combined_lifetime_value=f"{sum(float(x['lifetime_value']) for x in g):.2f}"))
        membership += [dict(source_customer_id=x["source_customer_id"],source_system=x["source_system"],golden_customer_id=gid,match_method="SURVIVOR" if len(g)==1 else "AUTO_LINK") for x in g]
    write(output/"candidate_pairs.csv",pairs);write(output/"review_queue.csv",[x for x in pairs if x["decision"]=="REVIEW"]);write(output/"customer_crosswalk.csv",membership);write(output/"golden_customers.csv",gold)
    metrics=dict(source_records=len(rows),golden_customers=len(gold),duplicate_records_consolidated=len(rows)-len(gold),auto_match_pairs=sum(x["decision"]=="AUTO_MATCH" for x in pairs),review_pairs=sum(x["decision"]=="REVIEW" for x in pairs))
    (output/"run_metrics.json").write_text(json.dumps(metrics,indent=2))
    return metrics
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--input",type=Path,required=True);p.add_argument("--output",type=Path,required=True);a=p.parse_args();print(json.dumps(run(a.input,a.output),indent=2))
