from src.ev_modifiers import (
    Promotion,
    direct_cash_subsidy_break_even_ratio,
    expected_return_ratio,
    expected_ticket_cash,
    one_wager_bonus_break_even_ratio,
)


def test_gross_ev_matches_exact_project_result():
    assert abs(expected_return_ratio(1, after_tax=False) - 0.5985557942634199) < 1e-12


def test_after_tax_multiplier_ordering():
    vals = [expected_return_ratio(m, after_tax=True) for m in (1,2,5,10)]
    assert vals[0] > vals[1] > vals[2] > vals[3]
    assert abs(vals[0] - 0.5918070335083189) < 1e-12


def test_break_even_thresholds():
    assert abs(direct_cash_subsidy_break_even_ratio(1) - 0.4081929664916811) < 1e-12
    assert abs(one_wager_bonus_break_even_ratio(1) - 0.6897399716117829) < 1e-12


def test_100_percent_one_wager_bonus_is_positive_ev_before_fees():
    p = Promotion(paid_stake=10.0, bonus=10.0, bonus_wager_turnover=1.0)
    assert p.expected_personal_capital_roi() > 1.18
    assert p.expected_profit_vs_personal_outlay() > 1.8
