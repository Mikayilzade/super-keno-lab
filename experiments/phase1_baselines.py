import csv, json, math, random, sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.rules import RuleSet
from src.evaluator import payout_matrix, metrics_from_payouts
from src.baselines import random_unique_tickets, weighted_frequency_tickets, balanced_cyclic_tickets
from src.data_loader import load_and_validate

ROOT=Path(__file__).resolve().parents[1]

def load():
    rows=load_and_validate(ROOT/'data')
    draws=[tuple(int(r[f'n{i}']) for i in range(1,21)) for r in rows]
    dates=[r['date'] for r in rows]
    assert len(draws)==195
    return draws,dates

def summarize(name,tickets,draws,dates,rules):
    mat=payout_matrix(tickets,draws,rules)
    totals=mat.sum(axis=0)
    m=metrics_from_payouts(totals,len(tickets),rules)
    return {'name':name,'N':len(tickets),'avg_pl':m.avg_pl,'min_pl':m.min_pl,'min_roi':m.min_return_ratio,
            'profitable_share':m.profitable_share,'worst_date':dates[m.worst_index],'max_payout':m.max_payout}

def complementary_search(train, seed=20260824, candidate_count=12000, max_n=700):
    candidates=random_unique_tickets(candidate_count,seed)
    mat=payout_matrix(candidates,train,RuleSet())
    cum=np.zeros(len(train),dtype=float)
    selected=[]; used=np.zeros(candidate_count,dtype=bool)
    checkpoints=[]
    for n in range(1,max_n+1):
        worst=np.argsort(cum)[:min(16,len(train))]
        score=mat[:,worst].sum(axis=1)+0.015*mat.sum(axis=1)
        score[used]=-1e300
        idx=int(np.argmax(score)); used[idx]=True; selected.append(idx); cum += mat[idx]
        if n<=20 or n%5==0:
            checkpoints.append((n,float(cum.min()/n),float(cum.mean()/n),float(cum.min())))
    best=max(checkpoints,key=lambda x:(x[1],x[2]))
    best_n=best[0]
    tickets=[candidates[i] for i in selected[:best_n]]
    return tickets,checkpoints,best

def main():
    draws,dates=load(); rules=RuleSet()
    train,valid,holdout=draws[:120],draws[120:160],draws[160:]
    dt,dv,dh=dates[:120],dates[120:160],dates[160:]
    Ns=[37,83,127,211,347,509]
    rows=[]
    for N in Ns:
        for seed in (11,29,47): rows.append(summarize(f'random_s{seed}',random_unique_tickets(N,seed),valid,dv,rules))
        rows.append(summarize('balanced_cyclic',balanced_cyclic_tickets(N),valid,dv,rules))
        rows.append(summarize('hot_frequency',weighted_frequency_tickets(train,N,71,1.35,False),valid,dv,rules))
        rows.append(summarize('cold_frequency',weighted_frequency_tickets(train,N,73,1.35,True),valid,dv,rules))

    tickets,checkpoints,best=complementary_search(train)
    comp_train=summarize('complementary_greedy_train',tickets,train,dt,rules)
    comp_valid=summarize('complementary_greedy_validation',tickets,valid,dv,rules)

    result={'split':{'train':[dt[0],dt[-1],120],'validation':[dv[0],dv[-1],40],'holdout_sealed':[dh[0],dh[-1],35]},
            'baseline_validation':rows,'complementary':{'selected_N':len(tickets),'train':comp_train,'validation':comp_valid,
            'best_train_checkpoint':best,'checkpoints':checkpoints,'selected_tickets':[list(t) for t in tickets],
            'candidate_count':12000,'seed':20260824},'holdout_opened':False}
    out=ROOT/'results/phase1_results.json'; out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
