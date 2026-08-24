from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import rankdata

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"

def load_rows():
    parts=sorted(DATA.glob("super_keno_draws_part_*.csv"))
    df=pd.concat([pd.read_csv(p) for p in parts],ignore_index=True)
    df["date"]=pd.to_datetime(df["date"])
    df=df.sort_values("date").reset_index(drop=True)
    nums=[f"n{i}" for i in range(1,21)]
    X=np.zeros((len(df),70),dtype=np.int8)
    for i,row in df.iterrows():
        vals=row[nums].astype(int).to_numpy()
        assert len(set(vals))==20 and vals.min()>=1 and vals.max()<=70
        X[i,vals-1]=1
    return df,X

def consecutive_pairs(dates, start, end):
    return [(i-1,i) for i in range(max(start,1),end) if (dates[i]-dates[i-1]).days==1]

def overlap_summary(X,pairs):
    vals=np.array([(X[a]&X[b]).sum() for a,b in pairs],dtype=float)
    return {"n":len(vals),"mean":float(vals.mean()),"min":int(vals.min()),"max":int(vals.max())}

def persistence(X,pairs):
    a=[];b=[]
    for i,j in pairs:
        prev=X[i].astype(bool)
        a.extend(X[j,prev]); b.extend(X[j,~prev])
    return {"p_next_if_prev":float(np.mean(a)),"p_next_if_not_prev":float(np.mean(b))}

def topk_hits(X,start,end,window,k,cold,history_floor=0):
    vals=[]
    for t in range(start,end):
        hist=X[max(history_floor,t-window):t].sum(0)
        order=np.argsort(hist) if cold else np.argsort(-hist)
        vals.append(int(X[t,order[:k]].sum()))
    return np.array(vals)

def pair_scores(X,t,window,shrink=5.0,history_floor=0):
    H=X[max(history_floor,t-window):t].astype(float)
    c=H.sum(0); C=H.T@H; n=len(H)
    exp=np.outer(c,c)/max(n,1)
    R=(C-exp)/np.sqrt(exp+shrink)
    np.fill_diagonal(R,0)
    return R[X[t-1].astype(bool)].sum(0)

def pair_topk(X,dates,start,end,window,k,history_floor=0):
    vals=[];aucs=[]
    for t in range(start,end):
        if t==0 or (dates[t]-dates[t-1]).days!=1: continue
        s=pair_scores(X,t,window,history_floor=history_floor)
        top=np.argsort(-s)[:k]
        vals.append(int(X[t,top].sum()))
        ranks=rankdata(s,method="average"); y=X[t]
        pos=ranks[y==1]; neg=ranks[y==0]
        auc=sum((p>neg).sum()+0.5*(p==neg).sum() for p in pos)/(20*50)
        aucs.append(auc)
    return np.array(vals),np.array(aucs)

def draw_features(X):
    rows=[]
    for r in X:
        nums=np.flatnonzero(r)+1
        s=set(nums.tolist())
        rows.append({
            "low35":int((nums<=35).sum()),"odd":int((nums%2==1).sum()),
            "sum":int(nums.sum()),"runs":sum(1 for x in nums if x+1 in s),
            "q1":int((nums<=17).sum()),"q2":int(((nums>=18)&(nums<=35)).sum()),
            "q3":int(((nums>=36)&(nums<=52)).sum()),"q4":int((nums>=53).sum()),
        })
    return pd.DataFrame(rows)

def lag_corr(F,pairs,col):
    a=np.array([F.loc[i,col] for i,j in pairs],float)
    b=np.array([F.loc[j,col] for i,j in pairs],float)
    return float(np.corrcoef(a,b)[0,1])

def freq_block_corr(X,a,b,c,d):
    return float(np.corrcoef(X[a:b].mean(0),X[c:d].mean(0))[0,1])

def pair_resid_vector(X,a,b):
    H=X[a:b].astype(float); n=len(H)
    c=H.sum(0); C=H.T@H; exp=np.outer(c,c)/n
    R=(C-exp)/np.sqrt(exp+5)
    iu=np.triu_indices(70,1)
    return R[iu]

def fair_mean(k): return 20*k/70

def mc_pvalue(k,n,obs,seed=12345,sims=200000):
    rng=np.random.default_rng(seed)
    z=rng.hypergeometric(k,70-k,20,size=(sims,n)).mean(1)
    return float((np.sum(z>=obs)+1)/(sims+1))

def main():
    df,X=load_rows(); dates=df["date"].tolist()
    assert len(df)==195
    current_start=int(np.flatnonzero(df["date"].to_numpy() >= np.datetime64("2025-01-10"))[0])
    assert current_start==8
    train1=(48,84); train2=(84,120); diag=(120,160)
    ptrain=consecutive_pairs(dates,current_start,120); pdiag=consecutive_pairs(dates,120,160)
    out={
      "holdout_opened":False,
      "split":{"legacy_pre_current_rules":[0,current_start],"current_rules_design":[current_start,120],"diagnostic":[120,160],"sealed_holdout":[160,195]},
      "lag1":{"design_overlap":overlap_summary(X,ptrain),"diagnostic_overlap":overlap_summary(X,pdiag),"design_persistence":persistence(X,ptrain),"diagnostic_persistence":persistence(X,pdiag)},
      "rolling_frequency":[],"pair_signal":[],"stability":{},"structural_lag":{},
    }
    for w in [5,10,20,40,80]:
      for k in [10,15,20,25,30,35]:
        rec={"window":w,"k":k}
        for label,(a,b) in [("fold1",train1),("fold2",train2),("diagnostic",diag)]:
          for cold in [False,True]:
            vals=topk_hits(X,a,b,w,k,cold,current_start)
            rec[f"{label}_{'cold' if cold else 'hot'}_mean"]=float(vals.mean())
        out["rolling_frequency"].append(rec)
    for w in [20,40,80]:
      rec={"window":w,"k":30}
      for label,(a,b) in [("fold1",train1),("fold2",train2),("diagnostic",diag)]:
        vals,aucs=pair_topk(X,dates,a,b,w,30,current_start)
        rec[f"{label}_n"]=len(vals);rec[f"{label}_mean_hits"]=float(vals.mean());rec[f"{label}_auc"]=float(aucs.mean())
      out["pair_signal"].append(rec)
    F=draw_features(X)
    for col in F.columns:
      out["structural_lag"][col]={"design":lag_corr(F,ptrain,col),"diagnostic":lag_corr(F,pdiag,col)}
    out["stability"]["number_frequency_corr_8_64_vs_64_120"]=freq_block_corr(X,8,64,64,120)
    out["stability"]["number_frequency_corr_64_120_vs_diag"]=freq_block_corr(X,64,120,120,160)
    r1=pair_resid_vector(X,8,64);r2=pair_resid_vector(X,64,120);rv=pair_resid_vector(X,120,160)
    out["stability"]["pair_residual_corr_8_64_vs_64_120"]=float(np.corrcoef(r1,r2)[0,1])
    out["stability"]["pair_residual_corr_64_120_vs_diag"]=float(np.corrcoef(r2,rv)[0,1])
    cold=topk_hits(X,120,160,80,30,True,current_start)
    pvals,aucs=pair_topk(X,dates,120,160,20,30,current_start)
    out["gated_candidates"]={
      "cold80_top30":{"diagnostic_mean":float(cold.mean()),"fair_mean":fair_mean(30),"mc_one_sided_p":mc_pvalue(30,len(cold),float(cold.mean()))},
      "pair20_top30":{"diagnostic_n":len(pvals),"diagnostic_mean":float(pvals.mean()),"fair_mean":fair_mean(30),"mc_one_sided_p":mc_pvalue(30,len(pvals),float(pvals.mean())),"diagnostic_auc":float(aucs.mean())}
    }
    out["verdict"]="NO_SIGNAL_GATE_PASSED"
    path=ROOT/"results/phase3_signal_audit.json"; path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(json.dumps(out["gated_candidates"],indent=2))
    print(out["lag1"])
    print(out["stability"])
if __name__=="__main__": main()
