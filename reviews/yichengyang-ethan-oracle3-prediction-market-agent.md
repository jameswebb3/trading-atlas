# oracle3-prediction-market-agent - Which risk limits are checked before an agent places a trade?

**Decision question:** Which risk limits are checked before an agent places a trade?

| Field | Review |
| --- | --- |
| Upstream | [YichengYang-Ethan/oracle3-prediction-market-agent](https://github.com/YichengYang-Ethan/oracle3-prediction-market-agent) |
| Primary area | Portfolio & Risk |
| Source commit | [cdab96ec1840face5caf97d5b1e07725b2da894f](https://github.com/YichengYang-Ethan/oracle3-prediction-market-agent/commit/cdab96ec1840face5caf97d5b1e07725b2da894f) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The standard manager checks single-trade size, position, total exposure, drawdown, daily loss and position count before approval. A NoRiskManager implementation exists and the pre-trade check depends on the portfolio state supplied to it. |

## What this project does

An agent-oriented prediction-market trader with pluggable risk managers.

## Mechanism inspected

The standard manager checks single-trade size, position, total exposure, drawdown, daily loss and position count before approval.

## Limitation that matters

A NoRiskManager implementation exists and the pre-trade check depends on the portfolio state supplied to it.

## Practical check for a trading system

Bind the live path to explicit risk policy and fresh account evidence rather than allowing an unguarded manager.

## Why this score

3/5. The guard covers several loss channels, but its data freshness and deployment binding are decisive.

## Source trail

[README](https://github.com/YichengYang-Ethan/oracle3-prediction-market-agent/blob/cdab96ec1840face5caf97d5b1e07725b2da894f/README.md#L1); [docs/index.md](https://github.com/YichengYang-Ethan/oracle3-prediction-market-agent/blob/cdab96ec1840face5caf97d5b1e07725b2da894f/docs/index.md#L1); [oracle3/risk/risk_manager.py](https://github.com/YichengYang-Ethan/oracle3-prediction-market-agent/blob/cdab96ec1840face5caf97d5b1e07725b2da894f/oracle3/risk/risk_manager.py#L31); [Root license](https://github.com/YichengYang-Ethan/oracle3-prediction-market-agent/blob/cdab96ec1840face5caf97d5b1e07725b2da894f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
