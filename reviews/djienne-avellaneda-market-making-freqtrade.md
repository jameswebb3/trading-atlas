# Hyperliquid Avellaneda Research Bot - Can a market-making strategy know its book and parameters are safe to use?

**Decision question:** Can a market-making strategy know its book and parameters are safe to use?

| Field | Review |
| --- | --- |
| Upstream | [djienne/AVELLANEDA_MARKET_MAKING_FREQTRADE](https://github.com/djienne/AVELLANEDA_MARKET_MAKING_FREQTRADE) |
| Primary area | Market Data & Ingestion |
| Source commit | [7047e8e5a7a8356f8c00c1e584b89c3cb543fda3](https://github.com/djienne/AVELLANEDA_MARKET_MAKING_FREQTRADE/commit/7047e8e5a7a8356f8c00c1e584b89c3cb543fda3) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Publishes validated Hyperliquid tape parts and blocks entries on stale books or invalid parameters. The research strategy still lacks observed maker queue position and exact context exchange time. |

## What this project does

A Hyperliquid perpetuals research strategy with its own book/trade/context collector and a Freqtrade decision loop.

## Mechanism inspected

The collector stores both receipt and exchange timestamps, rejects malformed messages, stops on capture error, and publishes complete Parquet parts via temporary file replacement. The strategy checks fee metadata, parameter validity and book freshness before allowing entries.

## Limitation that matters

The strategy is flat-or-one-long, not a complete two-sided market maker, and a public trade crossing cannot reveal its actual maker queue position. Context records use local receipt time as a proxy for exchange time, so source-specific timestamp semantics still matter. No root license text was verified.

## Practical check for a trading system

Carry source-time and receipt-time through capture, fail closed on stale books or invalid parameters, and evaluate passive fills with explicit queue uncertainty.

## Why this score

4/5. The capture and entry gate are direct, code-visible protections against bad data entering a live decision.

## Source trail

[README](https://github.com/djienne/AVELLANEDA_MARKET_MAKING_FREQTRADE/blob/7047e8e5a7a8356f8c00c1e584b89c3cb543fda3/README.md#L1); [HL_data_collector/hyperliquid_data_collector.py](https://github.com/djienne/AVELLANEDA_MARKET_MAKING_FREQTRADE/blob/7047e8e5a7a8356f8c00c1e584b89c3cb543fda3/HL_data_collector/hyperliquid_data_collector.py#L106); [HL_data_collector/hyperliquid_data_collector.py](https://github.com/djienne/AVELLANEDA_MARKET_MAKING_FREQTRADE/blob/7047e8e5a7a8356f8c00c1e584b89c3cb543fda3/HL_data_collector/hyperliquid_data_collector.py#L142); [HL_data_collector/hyperliquid_data_collector.py](https://github.com/djienne/AVELLANEDA_MARKET_MAKING_FREQTRADE/blob/7047e8e5a7a8356f8c00c1e584b89c3cb543fda3/HL_data_collector/hyperliquid_data_collector.py#L154); [user_data/strategies/avellaneda.py](https://github.com/djienne/AVELLANEDA_MARKET_MAKING_FREQTRADE/blob/7047e8e5a7a8356f8c00c1e584b89c3cb543fda3/user_data/strategies/avellaneda.py#L72); [user_data/strategies/avellaneda.py](https://github.com/djienne/AVELLANEDA_MARKET_MAKING_FREQTRADE/blob/7047e8e5a7a8356f8c00c1e584b89c3cb543fda3/user_data/strategies/avellaneda.py#L115).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
