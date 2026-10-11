# PingPong.jl - Is bar illiquidity a maker-fill model?

**Decision question:** Is bar illiquidity a maker-fill model?

| Field | Review |
| --- | --- |
| Upstream | [femtotrader/PingPong.jl](https://github.com/femtotrader/PingPong.jl) |
| Primary area | Signals & Models |
| Source commit | [3ef7dd4cf48a9ff956ec53d3b4cf732fd8e18675](https://github.com/femtotrader/PingPong.jl/commit/3ef7dd4cf48a9ff956ec53d3b4cf732fd8e18675) |
| Reviewed | 2026-10-11 |
| Declared license | AGPL |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its helper computes a windowed return-to-quote-volume illiquidity statistic. Bar closes and volume do not reveal queue, depth or executable spread. |

## What this project does

A Julia crypto trading and simulation toolkit.

## Mechanism inspected

Its helper computes a windowed return-to-quote-volume illiquidity statistic.

## Limitation that matters

Bar closes and volume do not reveal queue, depth or executable spread.

## Practical check for a trading system

Use the metric only as a coarse regime feature.

## Why this score

2/5. Transparent statistic, too coarse for execution realism.

## Source trail

[README](https://github.com/femtotrader/PingPong.jl/blob/3ef7dd4cf48a9ff956ec53d3b4cf732fd8e18675/README.md#L1); [Simulations/src/liq.jl](https://github.com/femtotrader/PingPong.jl/blob/3ef7dd4cf48a9ff956ec53d3b4cf732fd8e18675/Simulations/src/liq.jl#L35); [Root license](https://github.com/femtotrader/PingPong.jl/blob/3ef7dd4cf48a9ff956ec53d3b4cf732fd8e18675/LICENSE.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
