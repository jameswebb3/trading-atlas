# AI for Trading: Backtesting Project - Can a shifted return label be paired to the wrong feature date?

**Decision question:** Can a shifted return label be paired to the wrong feature date?

| Field | Review |
| --- | --- |
| Upstream | [purvasingh96/AI-for-Trading](https://github.com/purvasingh96/AI-for-Trading) |
| Primary area | Backtesting & Simulation |
| Source commit | [9413da27bf136eb1869a9b5122add518d7f5d906](https://github.com/purvasingh96/AI-for-Trading/commit/9413da27bf136eb1869a9b5122add518d7f5d906) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | It pairs sorted feature-date keys with sorted return-date keys shifted by two positions. Positional zipping does not check that each feature has the intended calendar relationship to its label, and it assumes both date sets align. |

## What this project does

A course notebook for factor backtesting on equity data.

## Mechanism inspected

It pairs sorted feature-date keys with sorted return-date keys shifted by two positions.

## Limitation that matters

Positional zipping does not check that each feature has the intended calendar relationship to its label, and it assumes both date sets align.

## Practical check for a trading system

Join labels to feature rows by explicit dates and verify every horizon before training.

## Why this score

1/5. The notebook is a concrete caution about date alignment, with no runnable trading-system component to adopt.

## Source trail

[README](https://github.com/purvasingh96/AI-for-Trading/blob/9413da27bf136eb1869a9b5122add518d7f5d906/README.md#L1); [Term 2/Projects/Project - 8 - Backtesting/project_8_backtesting.ipynb](https://github.com/purvasingh96/AI-for-Trading/blob/9413da27bf136eb1869a9b5122add518d7f5d906/Term%202/Projects/Project%20-%208%20-%20Backtesting/project_8_backtesting.ipynb#L171); [Term 2/Projects/Project - 8 - Backtesting/project_8_backtesting.ipynb](https://github.com/purvasingh96/AI-for-Trading/blob/9413da27bf136eb1869a9b5122add518d7f5d906/Term%202/Projects/Project%20-%208%20-%20Backtesting/project_8_backtesting.ipynb#L181).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
