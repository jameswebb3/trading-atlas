# TradeBot — A menu is not a replay engine

**Decision question:** Does the backtest model the order book or fills?

| Field | Review |
| --- | --- |
| Upstream | [TradeBot](https://github.com/markusaksli/TradeBot) |
| Primary area | Backtesting & Simulation |
| Source commit | [2296fe6c18365f4150a4d47b64b16c26ef4576b6](https://github.com/markusaksli/TradeBot/commit/2296fe6c18365f4150a4d47b64b16c26ef4576b6) |
| Reviewed | 2026-10-06 |
| Declared license | [GPL-3.0](https://github.com/markusaksli/TradeBot/blob/2296fe6c18365f4150a4d47b64b16c26ef4576b6/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The inspected Backtesting class selects a file and initializes the local account for a backtest run. This entry path provides no evidence of realistic fills or latency; the indicator strategy and venue differ from HL perps. |

## What this project does

A Binance indicator bot whose README says it is no longer maintained. [README](https://github.com/markusaksli/TradeBot/blob/2296fe6c18365f4150a4d47b64b16c26ef4576b6/README.md).

## Mechanism inspected

The inspected Backtesting class selects a file and initializes the local account for a backtest run. [Implementation](https://github.com/markusaksli/TradeBot/blob/2296fe6c18365f4150a4d47b64b16c26ef4576b6/src/main/java/modes/Backtesting.java#L26-L76).

## Limitation that matters

This entry path provides no evidence of realistic fills or latency; the indicator strategy and venue differ from HL perps. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Do not treat the project as an execution reference; use the missing fill model as a screening question.

## Why this score

Indirect relevance only: The inspected Backtesting class selects a file and initializes the local account for a backtest run. This entry path provides no evidence of realistic fills or latency; the indicator strategy and venue differ from HL perps.

## Source trail

[README](https://github.com/markusaksli/TradeBot/blob/2296fe6c18365f4150a4d47b64b16c26ef4576b6/README.md) · [Implementation](https://github.com/markusaksli/TradeBot/blob/2296fe6c18365f4150a4d47b64b16c26ef4576b6/src/main/java/modes/Backtesting.java#L26-L76).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
