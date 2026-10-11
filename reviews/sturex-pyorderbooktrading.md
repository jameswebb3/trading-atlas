# pyOrderbookTrading - Can a snapshot-only order-book backtest prove executable fills?

**Decision question:** Can a snapshot-only order-book backtest prove executable fills?

| Field | Review |
| --- | --- |
| Upstream | [sturex/pyOrderbookTrading](https://github.com/sturex/pyOrderbookTrading) |
| Primary area | Backtesting & Simulation |
| Source commit | [2020fe3760dbbd7c32570d000a44fc7b229101c7](https://github.com/sturex/pyOrderbookTrading/commit/2020fe3760dbbd7c32570d000a44fc7b229101c7) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | A BitMEX websocket saver records book messages and OrderBookContainer replays signals over the stored snapshots. It also builds a next-mid-price label from successive books. The backtest opens buys at best bid and sells at best ask, which is optimistic for crossing orders. Its final close is conditional on having no trades, so an empty signal path indexes a nonexistent trade while an open position is left unclosed. |

## What this project does

Stores order-book snapshots and replays signals, but uses optimistic bid/ask fills and has an inverted terminal-close guard.

## Mechanism inspected

A BitMEX websocket saver records book messages and OrderBookContainer replays signals over the stored snapshots. It also builds a next-mid-price label from successive books.

## Limitation that matters

The backtest opens buys at best bid and sells at best ask, which is optimistic for crossing orders. Its final close is conditional on having no trades, so an empty signal path indexes a nonexistent trade while an open position is left unclosed.

## Practical check for a trading system

Compare book-derived signals with side-correct executable prices, spread and queue assumptions; assert both empty-signal and still-open terminal paths.

## Why this score

2/5. The snapshot-to-signal path is concrete, but the fill and close logic makes its reported performance unsuitable as evidence.

## Source trail

[README.md](https://github.com/sturex/pyOrderbookTrading/blob/2020fe3760dbbd7c32570d000a44fc7b229101c7/README.md#L1); [BitmexOrderBookSaver.py](https://github.com/sturex/pyOrderbookTrading/blob/2020fe3760dbbd7c32570d000a44fc7b229101c7/BitmexOrderBookSaver.py#L15); [OrderBookContainer.py](https://github.com/sturex/pyOrderbookTrading/blob/2020fe3760dbbd7c32570d000a44fc7b229101c7/OrderBookContainer.py#L36); [OrderBook.py](https://github.com/sturex/pyOrderbookTrading/blob/2020fe3760dbbd7c32570d000a44fc7b229101c7/OrderBook.py#L25); [OrderBookContainer.py](https://github.com/sturex/pyOrderbookTrading/blob/2020fe3760dbbd7c32570d000a44fc7b229101c7/OrderBookContainer.py#L49); [OrderBookContainer.py](https://github.com/sturex/pyOrderbookTrading/blob/2020fe3760dbbd7c32570d000a44fc7b229101c7/OrderBookContainer.py#L72); [LICENSE](https://github.com/sturex/pyOrderbookTrading/blob/2020fe3760dbbd7c32570d000a44fc7b229101c7/LICENSE#L1)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
