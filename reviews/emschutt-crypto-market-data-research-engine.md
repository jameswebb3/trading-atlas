# Crypto Market Data Research Engine - Can a captured order-book dataset pass quality checks while live coverage is thin?

**Decision question:** Can a captured order-book dataset pass quality checks while live coverage is thin?

| Field | Review |
| --- | --- |
| Upstream | [emschutt/crypto-market-data-research-engine](https://github.com/emschutt/crypto-market-data-research-engine) |
| Primary area | Market Data & Ingestion |
| Source commit | [058090da8d7902d9b7181e70ce8a2c08eeb2a5a9](https://github.com/emschutt/crypto-market-data-research-engine/commit/058090da8d7902d9b7181e70ce8a2c08eeb2a5a9) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Its validator checks timestamps, prices, update IDs, book geometry and derived-feature consistency, then can throw on failed checks. Expected row-count minimums are enforced only in strict mock mode; non-strict live capture can pass with fewer observations than expected. |

## What this project does

A Binance high-frequency capture and research pipeline.

## Mechanism inspected

Its validator checks timestamps, prices, update IDs, book geometry and derived-feature consistency, then can throw on failed checks.

## Limitation that matters

Expected row-count minimums are enforced only in strict mock mode; non-strict live capture can pass with fewer observations than expected.

## Practical check for a trading system

Keep schema and geometry checks, and add live sequence and expected-coverage gates.

## Why this score

3/5. A detailed market-data invariant suite with a clear completeness boundary.

## Source trail

[README](https://github.com/emschutt/crypto-market-data-research-engine/blob/058090da8d7902d9b7181e70ce8a2c08eeb2a5a9/README.md#L1); [src/CryptoMarketDataResearchEngine/Diagnostics/MarketDataQualityValidator.cs](https://github.com/emschutt/crypto-market-data-research-engine/blob/058090da8d7902d9b7181e70ce8a2c08eeb2a5a9/src/CryptoMarketDataResearchEngine/Diagnostics/MarketDataQualityValidator.cs#L10); [src/CryptoMarketDataResearchEngine/Diagnostics/MarketDataQualityValidator.cs](https://github.com/emschutt/crypto-market-data-research-engine/blob/058090da8d7902d9b7181e70ce8a2c08eeb2a5a9/src/CryptoMarketDataResearchEngine/Diagnostics/MarketDataQualityValidator.cs#L125); [src/CryptoMarketDataResearchEngine/Diagnostics/MarketDataQualityValidator.cs](https://github.com/emschutt/crypto-market-data-research-engine/blob/058090da8d7902d9b7181e70ce8a2c08eeb2a5a9/src/CryptoMarketDataResearchEngine/Diagnostics/MarketDataQualityValidator.cs#L100); [src/CryptoMarketDataResearchEngine/Diagnostics/MarketDataQualityValidator.cs](https://github.com/emschutt/crypto-market-data-research-engine/blob/058090da8d7902d9b7181e70ce8a2c08eeb2a5a9/src/CryptoMarketDataResearchEngine/Diagnostics/MarketDataQualityValidator.cs#L123).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
