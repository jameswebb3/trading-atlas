# Polymarket Edge Research - Can a multi-outcome arbitrage scanner mistake an incomplete event for an edge?

**Decision question:** Can a multi-outcome arbitrage scanner mistake an incomplete event for an edge?

| Field | Review |
| --- | --- |
| Upstream | [sturzael/polymarket-edge-research](https://github.com/sturzael/polymarket-edge-research) |
| Primary area | Signals & Models |
| Source commit | [628574b0d2b52594aca67c63777a90e38f8adb25](https://github.com/sturzael/polymarket-edge-research/commit/628574b0d2b52594aca67c63777a90e38f8adb25) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Checks active outcome completeness before calling a negative-risk price sum an opportunity. Best-ask sums alone do not establish depth or synchronized fills across every leg. |

## What this project does

A public Polymarket research corpus with negative results and a scanner for negative-risk event bundles.

## Mechanism inspected

The scanner classifies whether the event includes the active outcome set before summing YES asks; it can also request book depth rather than relying only on best price.

## Limitation that matters

A quote-sum violation is an observation, not an executable arb. Depth, fees, simultaneous leg fills and settlement rules still govern capture; the README's strategy verdicts were not replicated here. No root license file was verified despite its README license statement.

## Practical check for a trading system

Treat outcome completeness and executable size as prerequisites before ranking any multi-leg quote discrepancy.

## Why this score

3/5 because A direct structural guard and research negative results are useful, while execution feasibility remains outside the scanner.

## Source trail

[README](https://github.com/sturzael/polymarket-edge-research/blob/628574b0d2b52594aca67c63777a90e38f8adb25/README.md#L98); [experiments/e15_neg_risk_arb/scanner.py](https://github.com/sturzael/polymarket-edge-research/blob/628574b0d2b52594aca67c63777a90e38f8adb25/experiments/e15_neg_risk_arb/scanner.py#L97); [experiments/e15_neg_risk_arb/scanner.py](https://github.com/sturzael/polymarket-edge-research/blob/628574b0d2b52594aca67c63777a90e38f8adb25/experiments/e15_neg_risk_arb/scanner.py#L138).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
