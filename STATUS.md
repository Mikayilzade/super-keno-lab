# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 1 — isolated dataset and experiment foundation`

## Completed

- Dedicated repository confirmed: `Mikayilzade/super-keno-lab`.
- Broad `Mikayilzade/loto-research` remains separate and untouched.
- Copied 195 validated Azerbaijan Super Keno draws into four chronological CSV shards.
- Dataset structure validated: exactly 20 unique integers in 1..70 per accepted draw.
- No duplicate dates or duplicate 20-number combinations in the copied set.
- Added deterministic loader/validator capable of reconstructing one master CSV.
- Reconstructed master locally and verified SHA-256 `d36ef577a5b3d3a7828b423bbd5474b504fe3a34f9a6fcbe900b14d44e41390c`.
- Added project isolation/evidence rules and experiment protocol.

## Current dataset

- Draws: **195**
- Earliest: **2022-12-21**
- Latest: **2026-08-23**
- Main recent missing block: **2026-06-22..2026-07-09**
- Older gaps remain; the dataset is not treated as continuous.

## Goal

Develop and stress-test ticket-generation and portfolio-selection approaches aimed at persistent positive net performance across unseen Super Keno draws. Primary metric: improve the worst unseen-draw P/L floor while preventing look-ahead leakage and overfitting.

## Next action

1. Web-verify and snapshot the current official Azerbaijan Super Keno ticket price, payout table and rules with date/source.
2. Implement a configurable ticket scorer and portfolio evaluator.
3. Define chronological train/validation/holdout and walk-forward splits on the 195-draw dataset.
4. Establish random and simple structural baselines.
5. Begin the first matrix/complementary-portfolio search and record concrete worst-draw witnesses.

No autonomous recurring task is enabled for this repository yet.
