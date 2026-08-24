# Phase 3 — walk-forward empirical signal audit

Date: 2026-08-24

Status: **NO SIGNAL GATE PASSED**. Final 35-row holdout remains sealed.

## Regime correction

Official current-rule registration is effective from **2025-01-10**. The first 8 copied rows predate that regime and are no longer used by default for current-regime signal fitting.

Current-regime design rows used here: accepted rows **8..119**. Reused diagnostic rows: **120..159**. Final holdout: **160..194**, still untouched.

## Lag-1 / previous-draw behavior

Only genuine consecutive-calendar-day transitions are used.

Current-regime design: **95** consecutive pairs.
- mean overlap between consecutive draws: **5.579** numbers;
- overlap range: **1..9**;
- P(number appears next | appeared previous draw): **0.2789**;
- P(number appears next | absent previous draw): **0.2884**.

Reused diagnostic block: **39** consecutive transitions.
- mean overlap: **6.000**;
- overlap range: **3..11**;
- P(next | previous): **0.3000**;
- P(next | absent): **0.2800**.

Direction reverses between design and diagnostic. Simple repeat/avoid-previous-draw rules are rejected.

## Rolling hot/cold signals

Audited rolling windows: **5, 10, 20, 40, 80** accepted draws. Audited top-k sets: **10, 15, 20, 25, 30, 35** numbers. All scores are walk-forward: only earlier rows are visible for a target draw.

The strongest internally stable-looking family was long-window **cold** ranking. For top-30 with an 80-draw window:
- internal fold 1 mean hits: **8.722**;
- internal fold 2 mean hits: **9.139**;
- fair top-30 expectation: **8.571**;
- reused diagnostic mean: **8.875**.

The diagnostic lift is small. Monte Carlo one-sided fair-control p-value: **0.165**. It does not pass the signal gate.

Number-frequency ranking itself is unstable across periods:
- correlation of per-number frequencies in current-regime design halves: **-0.109**;
- correlation of later design-half frequencies with diagnostic frequencies: **0.021**.

Conclusion: there is no evidence yet for persistent hot/cold number identity.

## Pair/co-occurrence signals

A shrinkage pair-residual score was built from past draws and used with the previous day's 20 numbers as context. The best-looking tested configuration was a 20-draw pair window with top-30 candidates.

- internal fold 1 mean hits: **8.500**;
- internal fold 2 mean hits: **8.788**;
- diagnostic mean hits on 39 consecutive targets: **9.026**;
- diagnostic rank AUC: **0.5155**;
- fair top-30 expectation: **8.571**;
- Monte Carlo one-sided fair-control p-value: **0.073**.

Interesting enough to retain as a weak lead, but below the gate and not strong enough to justify opening holdout or building a money strategy around it.

Pair structure is not stable as a fixed map:
- residual-pair correlation between two current-regime design halves: **0.0286**;
- later design half vs diagnostic block: **0.0035**.

Therefore persistent fixed pair identities are effectively absent in the current sample.

## Structural draw features

Checked lag behavior for low/high balance, odd/even, sum, consecutive runs, and four numeric quarters.

Most apparent design correlations reverse or disappear in diagnostic. The only visually persistent sign was mild negative lag correlation in the first quarter (1..17): roughly **-0.143** in design and **-0.132** in diagnostic. This is descriptive only; magnitude is weak and has not produced a validated monetary edge.

## Gate decision

No tested empirical family meets the standard required to feed the Phase 2 portfolio layer as a claimed predictive signal.

Rejected as current edges:
- previous-draw repeat/avoid rules;
- raw hot/cold identity;
- fixed persistent pair map;
- simple range/parity/sum/run persistence.

Retained weak leads:
- short-window contextual pair score (20-draw window, previous-draw context);
- mild group-level mean reversion in 1..17 composition;
- possible operational/regime metadata rather than number identity.

## Operational clue discovered during this phase

Official sources create an unresolved mechanism/time question:
- Super Keno is described as a **virtual numeric lottery** with 20 balls taken from a **lototron**;
- official material also discusses computer/virtual draw execution for online draw lotteries;
- public schedule says live draw **19:45**, while recent result metadata is stamped **18:45**.

This is not treated as an edge. It is documented in `research/OPERATIONAL_MECHANICS_2026-08-24.md` and becomes the next research direction.

## Holdout policy

The final **35 real draws were not scored or inspected for these signals**.

## Next direction

Phase 4 should focus on **operational/regime discovery** before more portfolio optimization:
1. establish actual Super Keno randomization mechanism (physical lototron vs software/RNG/virtual process) from authoritative evidence;
2. inspect historical broadcast/video metadata for equipment/software/studio changes;
3. resolve 19:45 vs 18:45 timestamp discrepancy;
4. identify cancellations, postponements, rule changes and draw-number regime boundaries;
5. once regimes are documented, rerun signal tests separately within each regime;
6. only then combine a supported signal with robust free-N portfolio selection.
