from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

BASE_PAYOUTS = {0:0.0,1:1.0,2:0.0,3:0.0,4:0.0,5:2.0,6:5.0,7:15.0,8:150.0,9:1500.0,10:100000.0}

@dataclass(frozen=True)
class RuleSet:
    ticket_price: float = 1.0
    payouts: Dict[int,float] = None
    multiplier: int = 1
    tax_rate: float = 0.10
    tax_exempt_profit: float = 500.0

    def __post_init__(self):
        if self.payouts is None:
            object.__setattr__(self, 'payouts', dict(BASE_PAYOUTS))
        if self.multiplier not in (1,2,5,10):
            raise ValueError('multiplier must be one of 1,2,5,10')

    @property
    def stake(self) -> float:
        return self.ticket_price * self.multiplier

    def gross_for_hits(self, hits:int) -> float:
        return self.payouts.get(hits,0.0) * self.multiplier

    def ticketwise_tax(self, gross:float) -> float:
        taxable = max(0.0, gross - self.stake - self.tax_exempt_profit)
        return taxable * self.tax_rate

    def net_cash_for_hits(self, hits:int) -> float:
        gross = self.gross_for_hits(hits)
        return gross - self.ticketwise_tax(gross)


def validate_ticket(ticket: Iterable[int]) -> Tuple[int,...]:
    t = tuple(sorted(int(x) for x in ticket))
    if len(t) != 10 or len(set(t)) != 10 or any(x < 1 or x > 70 for x in t):
        raise ValueError('ticket must contain exactly 10 unique integers in 1..70')
    return t


def validate_draw(draw: Iterable[int]) -> Tuple[int,...]:
    d = tuple(sorted(int(x) for x in draw))
    if len(d) != 20 or len(set(d)) != 20 or any(x < 1 or x > 70 for x in d):
        raise ValueError('draw must contain exactly 20 unique integers in 1..70')
    return d
