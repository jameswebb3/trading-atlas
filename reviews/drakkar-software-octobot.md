# OctoBot - How does a strategy optimizer compare configurations across time frames?

**Decision question:** How does a strategy optimizer compare configurations across time frames?

| Field | Review |
| --- | --- |
| Upstream | [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) |
| Primary area | Research & Reproducibility |
| Source commit | [c45fdc2c95c5bd3d649251fa90c327e2e8f86b00](https://github.com/Drakkar-Software/OctoBot/commit/c45fdc2c95c5bd3d649251fa90c327e2e8f86b00) |
| Reviewed | 2026-10-11 |
| Declared license | GPL-3.0 |
| Review depth | 3/3: README, relevant implementation and test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Ranks strategy configurations across replayed time frames. The inspected optimizer does not provide an untouched final test. |

## What this project does

A crypto trading platform with a documented replay engine and an in-process strategy optimizer.

## Mechanism inspected

The optimizer runs each evaluator and time-frame combination through a test suite, then sums each configuration rank across time frames. The documentation describes priority-ordered historical replay through the same channel infrastructure as live strategies.

## Limitation that matters

The inspected ranking is over the tested historical periods; this path does not establish an untouched holdout or account for how many configurations were searched. OctoBot is GPL-3.0, so this is an architectural reference, not a proposed dependency.

## Practical check for a trading system

Treat the search space and each run as evidence, then evaluate the selected configuration on a reserved period before promoting a strategy.

## Why this score

3/5. A concrete optimization and replay arrangement is visible, but the rank aggregation is not independent validation.

## Source trail

[README](https://github.com/Drakkar-Software/OctoBot/blob/c45fdc2c95c5bd3d649251fa90c327e2e8f86b00/README.md#L92); [docs/content/developers/packages/backtesting.md](https://github.com/Drakkar-Software/OctoBot/blob/c45fdc2c95c5bd3d649251fa90c327e2e8f86b00/docs/content/developers/packages/backtesting.md#L9); [octobot/strategy_optimizer/strategy_optimizer.py](https://github.com/Drakkar-Software/OctoBot/blob/c45fdc2c95c5bd3d649251fa90c327e2e8f86b00/octobot/strategy_optimizer/strategy_optimizer.py#L185); [octobot/strategy_optimizer/strategy_optimizer.py](https://github.com/Drakkar-Software/OctoBot/blob/c45fdc2c95c5bd3d649251fa90c327e2e8f86b00/octobot/strategy_optimizer/strategy_optimizer.py#L212); [License text](https://github.com/Drakkar-Software/OctoBot/blob/c45fdc2c95c5bd3d649251fa90c327e2e8f86b00/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
