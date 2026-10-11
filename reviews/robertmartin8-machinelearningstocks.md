# MachineLearningStocks — Random stock splits invalidate a temporal trading claim

**Decision question:** Does a classifier backtest preserve time ordering?

| Field | Review |
| --- | --- |
| Upstream | [robertmartin8/MachineLearningStocks](https://github.com/robertmartin8/MachineLearningStocks) |
| Primary area | Backtesting & Simulation |
| Source commit | [1c3712af741a9a030edb678b37ef18d1d2db9147](https://github.com/robertmartin8/MachineLearningStocks/commit/1c3712af741a9a030edb678b37ef18d1d2db9147) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/robertmartin8/MachineLearningStocks/blob/1c3712af741a9a030edb678b37ef18d1d2db9147/LICENSE.txt)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The backtest uses train_test_split on dated rows before fitting and evaluating the classifier; the source itself warns of a methodological flaw. Random splitting can mix eras, and the printed comparison lacks executable fill and cost evidence; it is not HL-perp alpha. |

## What this project does

Unmaintained stock-prediction tutorial with Random Forest and a simple return comparison. [README](https://github.com/robertmartin8/MachineLearningStocks/blob/1c3712af741a9a030edb678b37ef18d1d2db9147/README.md).

## Mechanism inspected

The backtest uses train_test_split on dated rows before fitting and evaluating the classifier; the source itself warns of a methodological flaw. [Implementation](https://github.com/robertmartin8/MachineLearningStocks/blob/1c3712af741a9a030edb678b37ef18d1d2db9147/backtesting.py#L10-L45).

## Limitation that matters

Random splitting can mix eras, and the printed comparison lacks executable fill and cost evidence; it is not HL-perp alpha. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep temporal and entity splits, preregistered N and executable cost models when evaluating any comparable signal.

## Why this score

The backtest uses train_test_split on dated rows before fitting and evaluating the classifier; the source itself warns of a methodological flaw. Random splitting can mix eras, and the printed comparison lacks executable fill and cost evidence; it is not HL-perp alpha.

## Source trail

[README](https://github.com/robertmartin8/MachineLearningStocks/blob/1c3712af741a9a030edb678b37ef18d1d2db9147/README.md) · [Implementation](https://github.com/robertmartin8/MachineLearningStocks/blob/1c3712af741a9a030edb678b37ef18d1d2db9147/backtesting.py#L10-L45) · [License](https://github.com/robertmartin8/MachineLearningStocks/blob/1c3712af741a9a030edb678b37ef18d1d2db9147/LICENSE.txt).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
