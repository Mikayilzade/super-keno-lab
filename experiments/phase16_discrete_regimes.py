from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiments.phase14_draw_structure import draw_structure, load_rows
from src.baselines import random_unique_tickets
from src.evaluator import payout_matrix
from src.rules import RuleSet

ROOT = Path(__file__).resolve().parents[1]
WARMUP = 70
TRAIN_START = 15
POOL_SIZE = 5_000
POOL_SEED = 424242
MIN_N = 19
MAX_N = 400
CAL_WINDOW = 32
RANDOM_REPLICATES = 20
KS = (4, 6, 8)
COMBO_DIMS = np.asarray([0,1,2,3,4,5,6], dtype=int)  # quadrants + odd + low35 + mean
WEIGHTS = np.asarray([2.0,2.0,2.0,2.0,1.25,1.0,1.5], dtype=float)
METHODS = ("prior", "markov1", "markov2", "knn", "mixture")


def standardize_past(X):
    mean = X.mean(axis=0)
    sd = X.std(axis=0)
    sd[sd < 1e-8] = 1.0
    return (X-mean)/sd, mean, sd


def deterministic_kmeans(X, k, max_iter=40):
    # deterministic farthest-point initialization; no stochastic model seed
    n = len(X)
    first = int(np.argmin(np.sum((X-X.mean(axis=0))**2, axis=1)))
    centers = [X[first].copy()]
    chosen = {first}
    while len(centers) < k:
        d = np.min(np.stack([np.sum((X-c)**2, axis=1) for c in centers]), axis=0)
        for idx in np.argsort(-d, kind="stable"):
            if int(idx) not in chosen:
                chosen.add(int(idx)); centers.append(X[int(idx)].copy()); break
    C = np.vstack(centers)
    labels = np.zeros(n, dtype=int)
    for _ in range(max_iter):
        dist = ((X[:,None,:]-C[None,:,:])**2).sum(axis=2)
        new_labels = np.argmin(dist, axis=1)
        new_C = C.copy()
        for j in range(k):
            m = new_labels == j
            if np.any(m): new_C[j] = X[m].mean(axis=0)
        if np.array_equal(new_labels, labels) and np.allclose(new_C, C):
            labels = new_labels; C = new_C; break
        labels = new_labels; C = new_C
    return labels, C


def smoothed_counts(labels, k, alpha=1.0, recent=None):
    if recent is not None and len(labels) > recent: labels = labels[-recent:]
    c = np.bincount(labels, minlength=k).astype(float) + alpha
    return c/c.sum()


def transition_probs(labels, k, order=1, alpha=1.0):
    prior = smoothed_counts(labels, k, alpha=alpha, recent=60)
    if order == 1:
        if len(labels) < 2: return prior
        prev = labels[-1]
        idx = [i for i in range(1,len(labels)) if labels[i-1] == prev]
    else:
        if len(labels) < 3: return prior
        pair = tuple(labels[-2:])
        idx = [i for i in range(2,len(labels)) if (labels[i-2],labels[i-1]) == pair]
    if len(idx) < (4 if order==1 else 3): return prior
    c = np.ones(k)*alpha
    for i in idx: c[labels[i]] += 1
    p = c/c.sum()
    # shrink sparse transition toward prior
    strength = min(1.0, len(idx)/(12.0 if order==1 else 8.0))
    return strength*p + (1-strength)*prior


def context_vector(S, t):
    pieces=[]
    for lag in (1,2,3):
        pieces.append(S[t-lag,COMBO_DIMS] if t>=lag else np.zeros(len(COMBO_DIMS)))
    for w in (5,10,20):
        H=S[max(0,t-w):t][:,COMBO_DIMS]
        pieces.append(H.mean(axis=0) if len(H) else np.zeros(len(COMBO_DIMS)))
    return np.concatenate(pieces)


def knn_probs(S, t, labels, k_states, nnei=10):
    current=context_vector(S,t)
    cand=[]
    # context at s predicts label at s; all s < t
    for s in range(max(TRAIN_START,3), t):
        c=context_vector(S,s)
        cand.append((float(np.mean((c-current)**2)), s))
    cand.sort(key=lambda z:(z[0],z[1]))
    ids=[s for _,s in cand[:min(nnei,len(cand))]]
    if not ids: return smoothed_counts(labels,k_states,recent=60)
    c=np.ones(k_states)
    offset=TRAIN_START
    for s in ids:
        li=s-offset
        if 0 <= li < len(labels): c[labels[li]] += 1
    p=c/c.sum()
    prior=smoothed_counts(labels,k_states,recent=60)
    return 0.75*p + 0.25*prior


def expected_ticket_score(ticket_struct_combo, centers_raw, probs):
    diff=(ticket_struct_combo[:,None,:]-centers_raw[None,:,:])*WEIGHTS[None,None,:]
    per_state=-np.sum(diff*diff,axis=2)
    return per_state @ probs


def choose_n(curves,t):
    prior=[s for s in range(max(WARMUP,t-CAL_WINDOW),t) if s in curves]
    if not prior: return MIN_N
    best=None
    for n in range(MIN_N,MAX_N+1):
        ratios=np.asarray([curves[s][n-1]/n for s in prior],dtype=float)
        avg=float(ratios.mean()); q20=float(np.quantile(ratios,.20)); recent=float(ratios[-min(10,len(ratios)):].mean())
        downside=float(np.maximum(0.0,1.0-ratios).mean())
        obj=.45*avg+.30*q20+.25*recent-.15*downside
        key=(obj,q20,avg)
        if best is None or key>best[0]: best=(key,n)
    return int(best[1])


def aggregate(records):
    cost=int(sum(r["N"] for r in records)); payout=float(sum(r["payout"] for r in records)); cap=float(sum(r["capped15"] for r in records))
    return {"targets":len(records),"cost":cost,"payout":payout,"net_pl":payout-cost,"roi":payout/cost,"capped15_roi":cap/cost,
            "profitable_share":float(np.mean([r["payout"]>r["N"] for r in records])),
            "N_min":int(min(r["N"] for r in records)),"N_median":float(np.median([r["N"] for r in records])),"N_max":int(max(r["N"] for r in records))}


def main():
    df,draws=load_rows()
    S=np.vstack([draw_structure(d) for d in draws])
    pool=random_unique_tickets(POOL_SIZE,POOL_SEED)
    TS=np.vstack([draw_structure(t) for t in pool])[:,COMBO_DIMS]
    raw=payout_matrix(pool,draws,RuleSet()).astype(np.float64)
    cap15=np.minimum(raw,15.0)

    result={"method":{"pool_size":POOL_SIZE,"pool_seed":POOL_SEED,"Ks":list(KS),"combo_dims":COMBO_DIMS.tolist(),"methods":list(METHODS),
                      "N_policy":f"free integer {MIN_N}..{MAX_N} selected from prior capped15 curves","no_future_leakage":True},"configs":{}}

    for K in KS:
        names=list(METHODS)+["oracle_state"]
        curves={m:{} for m in names}; recs={m:[] for m in names}
        random_runs={m:[[] for _ in range(RANDOM_REPLICATES)] for m in METHODS}
        class_diag={m:{"correct":0,"n":0,"logloss":[]} for m in METHODS}
        entropy=[]; state_counts=[]

        for t in range(WARMUP,len(draws)):
            H=S[TRAIN_START:t][:,COMBO_DIMS]
            Z,mu,sd=standardize_past(H)
            labels,Cz=deterministic_kmeans(Z,K)
            centers_raw=Cz*sd+mu
            target_z=(S[t,COMBO_DIMS]-mu)/sd
            target_state=int(np.argmin(np.sum((Cz-target_z[None,:])**2,axis=1)))
            prior=smoothed_counts(labels,K,recent=60)
            p1=transition_probs(labels,K,1)
            p2=transition_probs(labels,K,2)
            pk=knn_probs(S,t,labels,K)
            mix=.25*prior+.30*p1+.15*p2+.30*pk; mix=mix/mix.sum()
            probs={"prior":prior,"markov1":p1,"markov2":p2,"knn":pk,"mixture":mix,"oracle_state":np.eye(K)[target_state]}
            entropy.append(float(-np.sum(prior*np.log(prior+1e-12)))); state_counts.append(np.bincount(labels,minlength=K).tolist())

            for mi,m in enumerate(names):
                p=probs[m]
                score=expected_ticket_score(TS,centers_raw,p)
                order=np.argsort(-score,kind="stable")[:MAX_N]
                rc=np.cumsum(raw[order,t]); cc=np.cumsum(cap15[order,t]); curves[m][t]=cc
                n=choose_n(curves[m],t)
                recs[m].append({"t":t,"date":str(df.loc[t,"date"].date()),"N":n,"payout":float(rc[n-1]),"capped15":float(cc[n-1]),"ratio":float(rc[n-1]/n)})
                if m in METHODS:
                    class_diag[m]["correct"] += int(np.argmax(p)==target_state); class_diag[m]["n"] += 1; class_diag[m]["logloss"].append(float(-np.log(max(p[target_state],1e-12))))
                    for r in range(RANDOM_REPLICATES):
                        rng=np.random.default_rng(16_000_000+K*100_000+mi*10_000+r*137+t)
                        idx=rng.choice(POOL_SIZE,n,replace=False)
                        random_runs[m][r].append({"t":t,"N":n,"payout":float(raw[idx,t].sum()),"capped15":float(cap15[idx,t].sum())})

        cfg={"state_entropy_mean":float(np.mean(entropy)),"state_count_min_over_time":int(min(min(x) for x in state_counts)),"methods":{}}
        for m in names:
            strat=aggregate(recs[m]); item={"strategy":strat,"blocks":[]}
            for a,b in ((0,40),(40,80),(80,125)):
                block={"rows":[WARMUP+a,WARMUP+b],"strategy":aggregate(recs[m][a:b])}
                if m in METHODS:
                    rr=np.asarray([aggregate(run[a:b])["roi"] for run in random_runs[m]])
                    block["random_roi_mean"]=float(rr.mean()); block["above_random"]=bool(block["strategy"]["roi"]>rr.mean())
                item["blocks"].append(block)
            if m in METHODS:
                rr=np.asarray([aggregate(run)["roi"] for run in random_runs[m]])
                d=class_diag[m]
                item["random"]={"roi_mean":float(rr.mean()),"roi_p05":float(np.quantile(rr,.05)),"roi_p95":float(np.quantile(rr,.95)),"replicates_beating_strategy":int(np.sum(rr>=strat["roi"]))}
                item["classification"]={"accuracy":d["correct"]/d["n"],"logloss":float(np.mean(d["logloss"]))}
            cfg["methods"][m]=item
        result["configs"][str(K)]=cfg

    promoted=[]
    for K,cfg in result["configs"].items():
        for m in METHODS:
            z=cfg["methods"][m]; beats=sum(1 for b in z["blocks"] if b["above_random"]); pos=sum(1 for b in z["blocks"] if b["strategy"]["net_pl"]>0)
            if z["strategy"]["net_pl"]>0 and z["strategy"]["roi"]>z["random"]["roi_mean"] and beats>=2 and pos>=2: promoted.append({"K":int(K),"method":m})
    result["decision"]={"promoted":promoted,"oracle_state_note":"uses target regime class and is diagnostic only"}
    out=ROOT/"results"/"phase16_discrete_regimes.json"; out.write_text(json.dumps(result,indent=2),encoding="utf-8")

    lines=["# Phase 16 — discrete coarse-regime classification","","Date: 2026-08-25","",f"Status: **{'PROMOTION CANDIDATE(S)' if promoted else 'NO VALID GATE PASSED'}**","",
           "Past-only K-means states on mean/location + quadrants + balance; deterministic fixed 5,000-ticket universe; N free 19..400.","",
           "| K | method | ROI | random mean | P/L | blocks>random | positive blocks | class acc |",
           "|---:|---|---:|---:|---:|---:|---:|---:|"]
    for K,cfg in result["configs"].items():
        for m in METHODS:
            z=cfg["methods"][m]; beats=sum(1 for b in z["blocks"] if b["above_random"]); pos=sum(1 for b in z["blocks"] if b["strategy"]["net_pl"]>0)
            lines.append(f"| {K} | {m} | {z['strategy']['roi']:.5f} | {z['random']['roi_mean']:.5f} | {z['strategy']['net_pl']:.0f} | {beats}/3 | {pos}/3 | {z['classification']['accuracy']:.1%} |")
        o=cfg["methods"]["oracle_state"]["strategy"]
        lines.append(f"| {K} | oracle_state (diagnostic) | **{o['roi']:.5f}** | — | {o['net_pl']:.0f} | — | — | — |")
    lines += ["","## Decision", "", f"Promoted valid configurations: `{promoted}`.", "", "If none pass, the discrete history→structure branch is closed as a primary route; next work must use a genuinely new information source or a different non-history mechanism rather than retuning K/weights/windows."]
    (ROOT/"results"/"PHASE16_DISCRETE_REGIMES.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("\n".join(lines))

if __name__=="__main__": main()
