# Morningside Wagewise - Does a local matching engine preserve a real exchange queue?

**Decision question:** Does a local matching engine preserve a real exchange queue?

| Field | Review |
| --- | --- |
| Upstream | [azarandi/morningside-wagewise](https://github.com/azarandi/morningside-wagewise) |
| Primary area | Backtesting & Simulation |
| Source commit | [1372feea3a067feadfdecf065d245ae2140d0a75](https://github.com/azarandi/morningside-wagewise/commit/1372feea3a067feadfdecf065d245ae2140d0a75) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Matches local Kalshi orders by price and FIFO with partial fills. REST depth levels cannot reveal the queue of individual venue orders. |

## What this project does

A C++ Kalshi market-data handler and local orderbook matcher.

## Mechanism inspected

The matcher walks best price levels FIFO, applies partial fills, removes completed orders, and cancels residual FillAndKill orders. The market-data handler can populate this book from a REST orderbook response.

## Limitation that matters

The REST response supplies aggregate price levels, which the adapter converts to local orders with synthetic IDs. Local FIFO then describes the simulator queue, not observed Kalshi order priority. No message-sequence or historical add/cancel reconstruction is shown in this path.

## Practical check for a trading system

Separate a deterministic unit-test matcher from an exchange-grounded fill model, and label queue position as assumed.

## Why this score

2/5. The matcher is a useful mechanical reference with a severe limit when seeded from level snapshots.

## Source trail

[README](https://github.com/azarandi/morningside-wagewise/blob/1372feea3a067feadfdecf065d245ae2140d0a75/README.md#L7); [src/marketdata/MarketDataFeedHandler.cpp](https://github.com/azarandi/morningside-wagewise/blob/1372feea3a067feadfdecf065d245ae2140d0a75/src/marketdata/MarketDataFeedHandler.cpp#L58); [src/marketdata/MarketDataFeedHandler.cpp](https://github.com/azarandi/morningside-wagewise/blob/1372feea3a067feadfdecf065d245ae2140d0a75/src/marketdata/MarketDataFeedHandler.cpp#L81); [src/orderbook/Orderbook.cpp](https://github.com/azarandi/morningside-wagewise/blob/1372feea3a067feadfdecf065d245ae2140d0a75/src/orderbook/Orderbook.cpp#L25); [License text](https://github.com/azarandi/morningside-wagewise/blob/1372feea3a067feadfdecf065d245ae2140d0a75/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
