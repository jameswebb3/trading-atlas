# binance_grid_trader — A grid replaces orders only after full fills

**Decision question:** How does a futures grid react to partial fills and order-count limits?

| Field | Review |
| --- | --- |
| Upstream | [51bitquant/binance_grid_trader](https://github.com/51bitquant/binance_grid_trader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [97a65982541b93d412b4e6e8a9bc6582509f826a](https://github.com/51bitquant/binance_grid_trader/commit/97a65982541b93d412b4e6e8a9bc6582509f826a) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/51bitquant/binance_grid_trader/blob/97a65982541b93d412b4e6e8a9bc6582509f826a/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Its timer cancels the furthest tracked orders when the grid exceeds a configured count; `on_order` replenishes opposite and outer levels only on `ALLTRADED`. The inspected strategy records position updates on order events but has no partial-fill replenishment branch; its Binance contract rules do not establish HL behavior. |

## What this project does

Binance spot and USDT futures grid trader with a GUI and scripted mode. [README](https://github.com/51bitquant/binance_grid_trader/blob/97a65982541b93d412b4e6e8a9bc6582509f826a/README.md).

## Mechanism inspected

Its timer cancels the furthest tracked orders when the grid exceeds a configured count; `on_order` replenishes opposite and outer levels only on `ALLTRADED`. [Implementation](https://github.com/51bitquant/binance_grid_trader/blob/97a65982541b93d412b4e6e8a9bc6582509f826a/gridtrader/trader/strategies/futures_grid_long_short_strategy.py#L88-L224).

## Limitation that matters

The inspected strategy records position updates on order events but has no partial-fill replenishment branch; its Binance contract rules do not establish HL behavior. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Test partial fill, cancel acknowledgement and restart against target inventory before borrowing a grid replacement rule.

## Why this score

Its timer cancels the furthest tracked orders when the grid exceeds a configured count; `on_order` replenishes opposite and outer levels only on `ALLTRADED`. The inspected strategy records position updates on order events but has no partial-fill replenishment branch; its Binance contract rules do not establish HL behavior.

## Source trail

[README](https://github.com/51bitquant/binance_grid_trader/blob/97a65982541b93d412b4e6e8a9bc6582509f826a/README.md) · [Implementation](https://github.com/51bitquant/binance_grid_trader/blob/97a65982541b93d412b4e6e8a9bc6582509f826a/gridtrader/trader/strategies/futures_grid_long_short_strategy.py#L88-L224) · [License](https://github.com/51bitquant/binance_grid_trader/blob/97a65982541b93d412b4e6e8a9bc6582509f826a/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
