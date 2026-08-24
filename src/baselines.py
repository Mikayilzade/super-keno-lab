import random
from collections import Counter
from typing import Sequence


def random_unique_tickets(n, seed=1):
    rng=random.Random(seed); seen=set(); out=[]
    universe=list(range(1,71))
    while len(out)<n:
        t=tuple(sorted(rng.sample(universe,10)))
        if t not in seen:
            seen.add(t); out.append(t)
    return out


def weighted_frequency_tickets(draws: Sequence[Sequence[int]], n, seed=1, exponent=1.0, cold=False):
    rng=random.Random(seed)
    c=Counter(x for d in draws for x in d)
    vals=list(range(1,71))
    counts=[c[x] for x in vals]
    if cold:
        mx=max(counts); weights=[(mx-v+1)**exponent for v in counts]
    else:
        mn=min(counts); weights=[(v-mn+1)**exponent for v in counts]
    seen=set(); out=[]
    while len(out)<n:
        pool=vals[:]; w=weights[:]; pick=[]
        for _ in range(10):
            x=rng.choices(pool,weights=w,k=1)[0]
            j=pool.index(x); pick.append(x); pool.pop(j); w.pop(j)
        t=tuple(sorted(pick))
        if t not in seen:
            seen.add(t); out.append(t)
    return out


def balanced_cyclic_tickets(n):
    out=[]; seen=set()
    steps=[1,3,9,11,13,17,19,23,27,29,31,33]
    for step in steps:
        for start in range(70):
            t=tuple(sorted((((start+i*step)%70)+1) for i in range(10)))
            if t not in seen:
                seen.add(t); out.append(t)
                if len(out)>=n: return out
    raise RuntimeError('could not generate enough unique cyclic tickets')
