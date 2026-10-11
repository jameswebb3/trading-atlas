# polymarket-subgraph - What can an on-chain orderbook index actually prove?

**Decision question:** What can an on-chain orderbook index actually prove?

| Field | Review |
| --- | --- |
| Upstream | [Polymarket/polymarket-subgraph](https://github.com/Polymarket/polymarket-subgraph) |
| Primary area | Market Data & Ingestion |
| Source commit | [7a92ba026a9466c07381e0d245a323ba23ee8701](https://github.com/Polymarket/polymarket-subgraph/commit/7a92ba026a9466c07381e0d245a323ba23ee8701) |
| Reviewed | 2026-10-11 |
| Declared license | LGPL-3.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Indexes on-chain fill events and aggregate token volumes. The indexed entities do not reconstruct live displayed depth or queue position. |

## What this project does

Official Polymarket subgraph mappings for fills, market activity, open interest and PnL aggregates.

## Mechanism inspected

The orderbook mapping persists OrderFilled events with transaction, block time, asset IDs, amounts and fees, then updates token-level volume and trade counts.

## Limitation that matters

These are chain-observed fills and aggregates, not contemporaneous displayed CLOB depth or an order-arrival queue. A transaction-hash plus order-hash event key merits uniqueness checks when multiple fills occur inside one transaction.

## Practical check for a trading system

Use indexed chain events for settled trade provenance, not as an as-of executable orderbook or sole fill-timing source.

## Why this score

3/5. An authoritative event lineage reference is visible, with an important market-data capability boundary.

## Source trail

[README](https://github.com/Polymarket/polymarket-subgraph/blob/7a92ba026a9466c07381e0d245a323ba23ee8701/README.md#L3); [orderbook-subgraph/src/ExchangeMapping.ts](https://github.com/Polymarket/polymarket-subgraph/blob/7a92ba026a9466c07381e0d245a323ba23ee8701/orderbook-subgraph/src/ExchangeMapping.ts#L24); [orderbook-subgraph/src/ExchangeMapping.ts](https://github.com/Polymarket/polymarket-subgraph/blob/7a92ba026a9466c07381e0d245a323ba23ee8701/orderbook-subgraph/src/ExchangeMapping.ts#L60); [License text](https://github.com/Polymarket/polymarket-subgraph/blob/7a92ba026a9466c07381e0d245a323ba23ee8701/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
