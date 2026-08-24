# Experiment protocol

## Core question

Search for ticket-generation and portfolio-selection rules that maximize persistent net performance across real Super Keno draws, especially the minimum result over unseen draws.

**Portfolio size N is a free optimization variable.** It must not be restricted to round values such as 10, 100, 1000 or a small preset grid. Round/non-round sample sizes may be used for baselines, but optimizers should track every meaningful intermediate N or otherwise justify the search over N. A result at N=347, 12,354, 81,907, etc. is fully valid.

## Evaluation layers

1. **Training** — strategy discovery and parameter fitting.
2. **Validation** — choose among already-defined candidates; no redesign from validation outcomes.
3. **Holdout** — final untouched historical block. Open only after a strategy is frozen.
4. **Walk-forward** — repeatedly train only on the past and score the next draw to mimic real use.
5. **Forward test** — when practical, freeze a rule and evaluate future draws without changing it.

Because the recovered history is not continuous, splits must be chronological and must explicitly report gaps.

## Primary metrics

For each strategy and ticket count N record:

- total ticket cost;
- payout and net P/L for every draw;
- average P/L;
- median P/L;
- worst P/L;
- best P/L;
- percentage of profitable draws;
- maximum consecutive losing draws;
- worst draw witness;
- payout-tier counts per draw;
- comparison with random portfolios of the same N.

The central optimization target is the **worst unseen-draw P/L floor**, not the best historical average.

## Initial strategy families

- random baseline;
- fixed balanced coverage portfolios;
- hot/cold and recency signals;
- previous-draw overlap rules;
- pair/triple co-occurrence signals;
- range, parity, gap and run-structure signals;
- rolling-window regime detection;
- matrix/complementary portfolios where tickets are selected to cover each other's weak historical draw types;
- hybrid signal + matrix portfolios;
- operational/regime features if draw time, equipment, RNG/physical process or rule changes can be documented.

## Anti-overfitting rule

A strategy that performs well only after seeing the test period is rejected. Any new rule inspired by validation/holdout results becomes a new experiment and must receive a new untouched evaluation period.

An optimizer that directly memorizes historical draw rows is not accepted merely because it creates a positive floor in-sample. Robustness must be established with chronological internal folds, leave-block-out tests, walk-forward evaluation, perturbation/synthetic stress tests and ultimately unseen/forward data.

## Monetary results

Do not hard-code payout assumptions from memory. Before monetary experiments, store a dated, sourced current Super Keno ticket price and payout table and make the scorer configurable so historical rule changes can be represented if necessary.
