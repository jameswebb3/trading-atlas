# crypto-market-maker - Is a trade-based maker fill really a FIFO queue fill?

**Decision question:** Is a trade-based maker fill really a FIFO queue fill?

| Field | Review |
| --- | --- |
| Upstream | [wooyoungcode/crypto-market-maker](https://github.com/wooyoungcode/crypto-market-maker) |
| Primary area | Backtesting & Simulation |
| Source commit | [325c87d93f0751de113fba7d9495aec88d6f05de](https://github.com/wooyoungcode/crypto-market-maker/commit/325c87d93f0751de113fba7d9495aec88d6f05de) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Gates maker fills on latency and crossing trades, with partial fills; its queue reserve is a fixed fraction rather than observed queue ahead. Changing the queue fraction changes modeled fillability, and trade-only reconstruction cannot identify actual resting depth. |

## What this project does

A crypto market-making simulator with a trade-driven fill engine, latency gate, inventory controls and synthetic or downloaded input data.

## Mechanism inspected

A pending order cannot fill before its configured age, and trades must cross its side and price. A trade can cause a partial fill; tests explicitly cover fills before and after the latency threshold.

## Limitation that matters

The queue reserve is recomputed from the order remaining size times a fixed fraction on each trade, not maintained as an observed queue-ahead state. The data reconstructor also synthesizes top-of-book snapshots from trade-only rows. This is a useful sensitivity model, but it cannot claim true FIFO position on a venue.

## Practical check for a trading system

Treat the queue fraction as a scenario parameter and evaluate a range; use actual L2 or order-level data before interpreting maker fill rates as empirical.

## Why this score

3/5 because Direct latency and partial-fill mechanics are implemented and tested, but queue position is a per-trade heuristic over synthetic book state.

## Source trail

[README execution model](https://github.com/wooyoungcode/crypto-market-maker/blob/325c87d93f0751de113fba7d9495aec88d6f05de/README.md#L190); [Latency and queue rule](https://github.com/wooyoungcode/crypto-market-maker/blob/325c87d93f0751de113fba7d9495aec88d6f05de/simulator/fill_engine.py#L98); [Trade-only book reconstruction](https://github.com/wooyoungcode/crypto-market-maker/blob/325c87d93f0751de113fba7d9495aec88d6f05de/data/reconstructor.py#L41); [Latency tests](https://github.com/wooyoungcode/crypto-market-maker/blob/325c87d93f0751de113fba7d9495aec88d6f05de/tests/test_fill_engine.py#L19); [License](https://github.com/wooyoungcode/crypto-market-maker/blob/325c87d93f0751de113fba7d9495aec88d6f05de/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
