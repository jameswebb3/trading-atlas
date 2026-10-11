# pm-calibration - Does calibration skill survive spread, depth, fees and correlated events?

**Decision question:** Does calibration skill survive spread, depth, fees and correlated events?

| Field | Review |
| --- | --- |
| Upstream | [crollila/pm-calibration](https://github.com/crollila/pm-calibration) |
| Primary area | Signals & Models |
| Source commit | [7311a844b101f7062b09e67305dc94655201c8b3](https://github.com/crollila/pm-calibration/commit/7311a844b101f7062b09e67305dc94655201c8b3) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Tests forecast calibration with event clusters and converts candidate trades to depth-capped, fee-adjusted outcomes. A snapshot ask and a calibrated probability do not certify an obtainable fill. |

## What this project does

A prediction-market calibration study with market snapshots, event-clustered inference and an executable-price backtest.

## Mechanism inspected

The backtest sizes at displayed top-of-book depth, charges venue-specific taker fees and settles locked capital. Calibration tables can use event-clustered bootstrap intervals rather than treating many markets in one event as independent.

## Limitation that matters

Top-of-book depth observed at a snapshot is not a fill guarantee at order arrival. The README notes source overwrite between live and backfilled records sharing a primary key, so provenance must be checked before causal comparison. Results were not reproduced.

## Practical check for a trading system

Separate forecast calibration from tradable net edge and report event-clustered uncertainty with source-aware snapshots.

## Why this score

4/5 because The statistical and execution lenses are both implemented, but arrival-time fillability and mixed-source keys constrain conclusions.

## Source trail

[README](https://github.com/crollila/pm-calibration/blob/7311a844b101f7062b09e67305dc94655201c8b3/README.md#L1); [analysis/calibration.py](https://github.com/crollila/pm-calibration/blob/7311a844b101f7062b09e67305dc94655201c8b3/analysis/calibration.py#L99); [analysis/backtest.py](https://github.com/crollila/pm-calibration/blob/7311a844b101f7062b09e67305dc94655201c8b3/analysis/backtest.py#L71); [analysis/backtest.py](https://github.com/crollila/pm-calibration/blob/7311a844b101f7062b09e67305dc94655201c8b3/analysis/backtest.py#L89); [License text](https://github.com/crollila/pm-calibration/blob/7311a844b101f7062b09e67305dc94655201c8b3/LICENSE#L1); [README limitation](https://github.com/crollila/pm-calibration/blob/7311a844b101f7062b09e67305dc94655201c8b3/README.md#L707).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
