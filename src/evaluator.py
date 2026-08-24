from dataclasses import dataclass
from typing import Iterable, Sequence
import numpy as np
from .rules import RuleSet, validate_ticket, validate_draw

@dataclass
class PortfolioMetrics:
    n_tickets: int
    cost: float
    avg_payout: float
    median_payout: float
    min_payout: float
    max_payout: float
    avg_pl: float
    min_pl: float
    profitable_share: float
    worst_index: int
    min_return_ratio: float


def hits(ticket, draw):
    return len(set(ticket).intersection(draw))


def score_ticket(ticket, draw, rules=RuleSet(), after_tax=False):
    t = validate_ticket(ticket)
    d = validate_draw(draw)
    h = hits(t,d)
    payout = rules.net_cash_for_hits(h) if after_tax else rules.gross_for_hits(h)
    return {'hits':h,'payout':payout,'cost':rules.stake,'pl':payout-rules.stake}


def payout_matrix(tickets: Sequence[Iterable[int]], draws: Sequence[Iterable[int]], rules=RuleSet(), after_tax=False):
    tm = np.zeros(len(tickets), dtype=object)
    dm = np.zeros(len(draws), dtype=object)
    for i,t in enumerate(tickets):
        mask=0
        for x in validate_ticket(t): mask |= 1 << (x-1)
        tm[i]=mask
    for j,d in enumerate(draws):
        mask=0
        for x in validate_draw(d): mask |= 1 << (x-1)
        dm[j]=mask
    out=np.empty((len(tickets),len(draws)),dtype=np.float64)
    lookup=np.array([rules.net_cash_for_hits(k) if after_tax else rules.gross_for_hits(k) for k in range(11)],dtype=np.float64)
    for i,m in enumerate(tm):
        hs=np.fromiter(((int(m)&int(x)).bit_count() for x in dm), dtype=np.int8, count=len(dm))
        out[i,:]=lookup[hs]
    return out


def metrics_from_payouts(total_payouts, n_tickets, rules=RuleSet()):
    p=np.asarray(total_payouts,dtype=float)
    cost=n_tickets*rules.stake
    pl=p-cost
    worst=int(np.argmin(pl))
    return PortfolioMetrics(
        n_tickets=n_tickets,cost=cost,
        avg_payout=float(np.mean(p)),median_payout=float(np.median(p)),
        min_payout=float(np.min(p)),max_payout=float(np.max(p)),
        avg_pl=float(np.mean(pl)),min_pl=float(np.min(pl)),
        profitable_share=float(np.mean(pl>0)),worst_index=worst,
        min_return_ratio=float(np.min(p)/cost if cost else 0.0),
    )
