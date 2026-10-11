# Baselinr - A drift alert depends on which history became the baseline

**Decision question:** Which prior data does an automatic drift baseline actually use?

| Field | Review |
| --- | --- |
| Upstream | [baselinrhq/baselinr](https://github.com/baselinrhq/baselinr) |
| Primary area | Data Quality & Lineage |
| Source commit | [6f6b78291586ab2404de1b1e4c03efc76e786420](https://github.com/baselinrhq/baselinr/commit/6f6b78291586ab2404de1b1e4c03efc76e786420) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Selects a historical drift baseline and records the contributing run IDs, with automatic choice among variance, seasonality and last-run rules. High variance takes precedence over seasonality, and short history can silently change the selected rule to last run. |

## What this project does

A database profiling and drift detection tool. The inspected selector chooses last-run, moving-average, prior-period or stable-window baselines for column metrics.

## Mechanism inspected

The selector asks for completed runs before the current run, builds a baseline from selected metric values and records contributing run IDs in metadata. Automatic mode chooses moving average for high variance, prior period for detected seasonality and last run otherwise. Source tests construct runs and results in an in-memory database.

## Limitation that matters

Heuristic precedence gives high variance priority over seasonality; a seasonal but volatile series selects moving average. Several branches fall back to the last run when history is short, changing the comparison rule. The code does not encode market sessions, publication time or a point-in-time availability constraint. This is a source review, not a runtime or security test.

## Practical check for a trading system

Pin the baseline rule and contributing run IDs in each market-data quality result. Treat fallback as a named quality state, and construct baselines only from observations available before the decision cutoff.

## Why this score

3/5 because the selector and its tests give a concrete transferable baseline-provenance pattern, while trading-specific time and session validity are absent.

## Source trail

[README](https://github.com/baselinrhq/baselinr/blob/6f6b78291586ab2404de1b1e4c03efc76e786420/README.md#L1); [Strategy dispatch](https://github.com/baselinrhq/baselinr/blob/6f6b78291586ab2404de1b1e4c03efc76e786420/baselinr/drift/baseline_selector.py#L55); [Moving-average fallback](https://github.com/baselinrhq/baselinr/blob/6f6b78291586ab2404de1b1e4c03efc76e786420/baselinr/drift/baseline_selector.py#L140); [Auto choice](https://github.com/baselinrhq/baselinr/blob/6f6b78291586ab2404de1b1e4c03efc76e786420/baselinr/drift/baseline_selector.py#L342); [Selector tests](https://github.com/baselinrhq/baselinr/blob/6f6b78291586ab2404de1b1e4c03efc76e786420/tests/test_baseline_selector.py#L19); [License](https://github.com/baselinrhq/baselinr/blob/6f6b78291586ab2404de1b1e4c03efc76e786420/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
