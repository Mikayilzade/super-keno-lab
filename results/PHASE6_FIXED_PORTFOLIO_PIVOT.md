# Phase 6 — fixed-portfolio target reset and one-time holdout test

Date: 2026-08-24

Status: **FIXED UNIVERSAL PROFIT TARGET PROVED IMPOSSIBLE; empirical search continues only as a real-draw/predictive problem.**

## User-directed pivot

Physical-machine/video investigation is stopped as a project priority. Treat the lototron as unchanged unless future work specifically needs another assumption.

The practical target is now portfolio-first: search across arbitrary integer N for collections of different tickets with the strongest persistent minimum net result.

## Exact universal result

See `research/FIXED_PORTFOLIO_MAXIMIN_BOUND.md`.

Under the current 1-AZN payout table, every fixed ticket has exact gross expected payout

**0.5985557942634199 AZN**.

Therefore every fixed N-ticket portfolio has average gross payout `0.5985557942634199 * N` over all possible 20-of-70 draws, so at least one draw must return no more than that average.

The universal fixed-portfolio maximin ratio is exactly **0.5985557942634199**, achieved by the portfolio containing all `C(70,10)=396,704,524,216` distinct tickets.

So no fixed ticket list, regardless of N, can pay > cost on every mathematically possible draw.

## Strong finite-history construction

To test the user's intended object directly, a new free-N greedy maximin search was frozen on the first **160 previously exposed real draws**.

Reproducible experiment:
- `experiments/phase6_fixed_portfolio_search.py`
- candidate pool: **30,000** deterministic unique tickets;
- seed: `260824`;
- bottom-scenario targeting: 24 weakest historical draws at each step;
- N searched continuously from 20 through 1200.

The best historical prefix was **N=662**.

### Fit on 160 exposed draws

- tickets: **662**
- worst payout: **1086 AZN**
- worst P/L: **+424 AZN**
- minimum payout/cost: **1.64048**
- profitable draws: **160/160**
- average payout/cost: **5.28834**

Exact selected candidate indices are stored in `results/phase6_candidate_662_indices.json`; together with the deterministic generator/seed they reproduce the exact 662-ticket list. The experiment script can also emit the expanded ticket CSV.

This is an even stronger historical “always plus” construction than Phase 1.

## One-time test on the formerly sealed final 35 draws

After the algorithm and exact 662-ticket list were frozen, the final 35 rows were opened **once**.

Result:

- profitable draws: **0 / 35**
- worst payout: **249 AZN**
- cost: **662 AZN**
- worst P/L: **-413 AZN**
- minimum payout/cost: **0.37613**
- average payout/cost: **0.505999**
- average P/L: **-327.03 AZN**
- best payout/cost: **0.75831**
- worst date: **2026-08-13**

Verdict: **extreme historical overfit**. A list can be engineered to be positive on every known draw and still fail on every next unseen draw.

The final 35 rows are now consumed and must never again be described as untouched holdout.

## What this rules out

Rejected:
- endlessly fitting a fixed list against a finite historical archive and treating 100% historical profitability as evidence of persistent profit;
- searching for a universal fixed list with guaranteed >100% return under current rules.

## What remains worth searching

1. **Adversarial/maximin constructions for finite N** — not to reach impossible >1 universal ratio, but to learn how close smaller portfolios can approach the exact 0.59855579 universal ceiling and to produce worst-draw witnesses.
2. **Walk-forward ticket-generation rules** — portfolio may change before each draw using only past information.
3. **Conditional portfolios** — choose among multiple prebuilt portfolios using a genuine pre-draw observable signal.
4. **Historical regime / predictive models** — only if they improve repeated forward windows, not one fitted archive.
5. **Future forward validation** — because the previous 35-row holdout has now been spent.

## Next action

Build a cutting-plane / adversarial-draw loop:

1. start with a candidate portfolio;
2. search the full draw space heuristically/optimally for a draw that minimizes its payout;
3. add that worst draw as a constraint/witness;
4. rebuild the portfolio with free N against the growing adversarial set;
5. repeat until the guaranteed floor stabilizes;
6. separately keep a walk-forward real-draw track whose goal is positive actual performance, since universal >1 is impossible.

Do not return to equipment/video research unless a later strategy explicitly requires it.
