# Phase 16 — discrete coarse-regime classification

Date: 2026-08-25

Status: **NO VALID GATE PASSED**

Past-only K-means states on mean/location + quadrants + balance; deterministic fixed 5,000-ticket universe; N free 19..400.

| K | method | ROI | random mean | P/L | blocks>random | positive blocks | class acc |
|---:|---|---:|---:|---:|---:|---:|---:|
| 4 | prior | 0.58036 | 0.54118 | -6606 | 1/3 | 0/3 | 32.8% |
| 4 | markov1 | 0.56524 | 0.54553 | -7563 | 1/3 | 0/3 | 39.2% |
| 4 | markov2 | 0.56933 | 0.55516 | -7315 | 1/3 | 0/3 | 36.8% |
| 4 | knn | 0.58686 | 0.56420 | -9622 | 1/3 | 0/3 | 28.8% |
| 4 | mixture | 0.55342 | 0.53732 | -9321 | 1/3 | 0/3 | 35.2% |
| 4 | oracle_state (diagnostic) | **0.60790** | — | -7911 | — | — | — |
| 6 | prior | 0.48026 | 0.56280 | -7097 | 0/3 | 0/3 | 19.2% |
| 6 | markov1 | 0.55022 | 0.54918 | -7930 | 1/3 | 0/3 | 16.8% |
| 6 | markov2 | 0.58287 | 0.54961 | -7190 | 1/3 | 0/3 | 18.4% |
| 6 | knn | 0.55042 | 0.52619 | -11810 | 1/3 | 0/3 | 21.6% |
| 6 | mixture | 0.57818 | 0.55080 | -7575 | 1/3 | 0/3 | 18.4% |
| 6 | oracle_state (diagnostic) | **0.68827** | — | -4343 | — | — | — |
| 8 | prior | 0.48976 | 0.52614 | -6053 | 1/3 | 0/3 | 10.4% |
| 8 | markov1 | 0.55417 | 0.53638 | -7708 | 1/3 | 0/3 | 20.8% |
| 8 | markov2 | 0.58939 | 0.55599 | -5395 | 1/3 | 0/3 | 16.0% |
| 8 | knn | 0.54386 | 0.53788 | -11987 | 1/3 | 0/3 | 20.0% |
| 8 | mixture | 0.55614 | 0.54394 | -7290 | 1/3 | 0/3 | 16.8% |
| 8 | oracle_state (diagnostic) | **0.65388** | — | -7390 | — | — | — |

## Decision

Promoted valid configurations: `[]`.

If none pass, the discrete history→structure branch is closed as a primary route; next work must use a genuinely new information source or a different non-history mechanism rather than retuning K/weights/windows.
