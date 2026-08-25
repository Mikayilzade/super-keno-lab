from __future__ import annotations

from dataclasses import dataclass
from math import comb

from .rules import RuleSet


def hit_probability(hits: int) -> float:
    if hits < 0 or hits > 10:
        return 0.0
    misses = 20 - hits
    if misses < 0 or misses > 60:
        return 0.0
    return comb(10, hits) * comb(60, misses) / comb(70, 20)


def expected_ticket_cash(multiplier: int = 1, after_tax: bool = True) -> float:
    rules = RuleSet(multiplier=multiplier)
    total = 0.0
    for h in range(11):
        cash = rules.net_cash_for_hits(h) if after_tax else rules.gross_for_hits(h)
        total += hit_probability(h) * cash
    return total


def expected_return_ratio(multiplier: int = 1, after_tax: bool = True) -> float:
    rules = RuleSet(multiplier=multiplier)
    return expected_ticket_cash(multiplier, after_tax=after_tax) / rules.stake


def direct_cash_subsidy_break_even_ratio(multiplier: int = 1) -> float:
    """Cash-equivalent subsidy / paid stake needed for EV >= personal outlay."""
    e = expected_return_ratio(multiplier, after_tax=True)
    return 1.0 - e


def one_wager_bonus_break_even_ratio(multiplier: int = 1) -> float:
    """Bonus / paid stake needed when bonus must itself be wagered once at same EV."""
    e = expected_return_ratio(multiplier, after_tax=True)
    return 1.0 / e - 1.0


def overlay_ev_per_qualifying_spend(
    prize_pool: float,
    competition_entries: float,
    entries_earned: float = 1.0,
    qualifying_spend: float = 5.0,
) -> float:
    """Expected overlay prize value per 1 AZN qualifying spend.

    Assumes equal-probability entries and a known/valued aggregate prize pool.
    Returns 0 for an empty prize pool or zero entries earned. Invalid denominator/spend
    raises ValueError rather than silently fabricating EV.
    """
    if competition_entries <= 0:
        raise ValueError("competition_entries must be > 0")
    if qualifying_spend <= 0:
        raise ValueError("qualifying_spend must be > 0")
    if prize_pool < 0 or entries_earned < 0:
        raise ValueError("prize_pool and entries_earned must be >= 0")
    return (prize_pool / competition_entries) * entries_earned / qualifying_spend


def combined_return_ratio_with_overlay(
    base_return_ratio: float,
    prize_pool: float,
    competition_entries: float,
    entries_earned: float = 1.0,
    qualifying_spend: float = 5.0,
) -> float:
    """Personal-capital expected return ratio from base play plus an independent overlay."""
    return base_return_ratio + overlay_ev_per_qualifying_spend(
        prize_pool=prize_pool,
        competition_entries=competition_entries,
        entries_earned=entries_earned,
        qualifying_spend=qualifying_spend,
    )


@dataclass(frozen=True)
class Promotion:
    paid_stake: float
    bonus: float = 0.0
    bonus_wager_turnover: float = 1.0
    cash_rebate: float = 0.0
    withdrawal_fee_rate: float = 0.0
    withdrawal_fee_min: float = 0.0
    multiplier: int = 1

    def expected_cash_before_withdrawal_fee(self) -> float:
        e = expected_return_ratio(self.multiplier, after_tax=True)
        paid_play_return = self.paid_stake * e
        bonus_play_return = self.bonus * self.bonus_wager_turnover * e
        return paid_play_return + bonus_play_return + self.cash_rebate

    def expected_net_cash(self) -> float:
        cash = self.expected_cash_before_withdrawal_fee()
        if cash <= 0 or self.withdrawal_fee_rate <= 0:
            return cash
        fee = max(self.withdrawal_fee_min, cash * self.withdrawal_fee_rate)
        return max(0.0, cash - fee)

    def expected_profit_vs_personal_outlay(self) -> float:
        return self.expected_net_cash() - self.paid_stake

    def expected_personal_capital_roi(self) -> float:
        return self.expected_net_cash() / self.paid_stake if self.paid_stake else float('inf')
