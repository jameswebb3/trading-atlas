# PurgedCV - Can cross-validation remove every training label that overlaps a test label window?

**Decision question:** Can cross-validation remove every training label that overlaps a test label window?

| Field | Review |
| --- | --- |
| Upstream | [landtml/purgedcv](https://github.com/landtml/purgedcv) |
| Primary area | Backtesting & Simulation |
| Source commit | [aee3396422192d18bc30d376dfe9e31b2399abab](https://github.com/landtml/purgedcv/commit/aee3396422192d18bc30d376dfe9e31b2399abab) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | It converts event end times to positions, removes interval-overlapping training rows and applies a forward embargo from a declared anchor. Correct interval splitting does not establish that each input feature was published by its decision time or that holdout selection stayed untouched. |

## What this project does

A financial time-series cross-validation splitter with purge and embargo.

## Mechanism inspected

It converts event end times to positions, removes interval-overlapping training rows and applies a forward embargo from a declared anchor.

## Limitation that matters

Correct interval splitting does not establish that each input feature was published by its decision time or that holdout selection stayed untouched.

## Practical check for a trading system

Use the interval mask for label leakage checks, then independently enforce available-at and trial-count gates.

## Why this score

4/5. The inspected implementation directly addresses a common false-validation path and exposes its anchor choice.

## Source trail

[README](https://github.com/landtml/purgedcv/blob/aee3396422192d18bc30d376dfe9e31b2399abab/README.md#L1); [src/purgedcv/_splitter.py](https://github.com/landtml/purgedcv/blob/aee3396422192d18bc30d376dfe9e31b2399abab/src/purgedcv/_splitter.py#L213); [src/purgedcv/_splitter.py](https://github.com/landtml/purgedcv/blob/aee3396422192d18bc30d376dfe9e31b2399abab/src/purgedcv/_splitter.py#L246); [Root license](https://github.com/landtml/purgedcv/blob/aee3396422192d18bc30d376dfe9e31b2399abab/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
