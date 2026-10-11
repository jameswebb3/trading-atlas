# Backtesting - Are funding and mark-price series distinct from trade candles in a futures backtest?

**Decision question:** Are funding and mark-price series distinct from trade candles in a futures backtest?

| Field | Review |
| --- | --- |
| Upstream | [Traderhs/Backtesting](https://github.com/Traderhs/Backtesting) |
| Primary area | Backtesting & Simulation |
| Source commit | [bc82a2308891bf63cc19e1f549d9ba16c45e0565](https://github.com/Traderhs/Backtesting/commit/bc82a2308891bf63cc19e1f549d9ba16c45e0565) |
| Reviewed | 2026-10-11 |
| Declared license | Custom: personal, educational and non-commercial use only |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Keeps mark-price and funding inputs separate in a multi-symbol futures replay. Bar-level liquidation and the custom non-commercial license limit direct reuse. |

## What this project does

A C++ multi-symbol Binance Futures backtester with separate mark-price and funding data paths.

## Mechanism inspected

The engine configuration admits a mark-price series and a funding-rate directory rather than deriving both from OHLCV trade candles. Its loader adds funding inputs before the simulation path.

## Limitation that matters

The code inspected is bar-driven and tied to Binance Futures, so it does not establish Hyperliquid liquidation or intrabar execution fidelity. The root license grants personal, educational and non-commercial use, not a standard permissive license.

## Practical check for a trading system

Keep funding, mark and traded-price provenance separate; adapt the mechanism rather than lifting venue rules or code.

## Why this score

2/5 because The data separation is useful, but venue specificity and restrictive reuse terms sharply limit direct transfer.

## Source trail

[README](https://github.com/Traderhs/Backtesting/blob/bc82a2308891bf63cc19e1f549d9ba16c45e0565/README.md#L10); [Includes/Engines/Backtesting.hpp](https://github.com/Traderhs/Backtesting/blob/bc82a2308891bf63cc19e1f549d9ba16c45e0565/Includes/Engines/Backtesting.hpp#L125); [Sources/Cores/Engines/Backtesting.cpp](https://github.com/Traderhs/Backtesting/blob/bc82a2308891bf63cc19e1f549d9ba16c45e0565/Sources/Cores/Engines/Backtesting.cpp#L448); [Sources/Cores/Engines/Backtesting.cpp](https://github.com/Traderhs/Backtesting/blob/bc82a2308891bf63cc19e1f549d9ba16c45e0565/Sources/Cores/Engines/Backtesting.cpp#L486); [License text](https://github.com/Traderhs/Backtesting/blob/bc82a2308891bf63cc19e1f549d9ba16c45e0565/LICENSE#L1); [README limitation](https://github.com/Traderhs/Backtesting/blob/bc82a2308891bf63cc19e1f549d9ba16c45e0565/README.md#L550).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
