# stockgecko.com — Check market-to-context alignment before ingest

**Decision question:** Can a Hyperliquid market snapshot silently pair the wrong market and metric?

| Field | Review |
| --- | --- |
| Upstream | [Anish-Agnihotri/stockgecko.com](https://github.com/Anish-Agnihotri/stockgecko.com) |
| Primary area | Market Data & Ingestion |
| Source commit | [03261e67510263c1ecfd173fd5e103da2c60820b](https://github.com/Anish-Agnihotri/stockgecko.com/commit/03261e67510263c1ecfd173fd5e103da2c60820b) |
| Reviewed | 2026-10-09 |
| Declared license | AGPL-3.0 ([source](https://github.com/Anish-Agnihotri/stockgecko.com/blob/03261e67510263c1ecfd173fd5e103da2c60820b/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | It validates locally configured markets against the discovered universe, fans out one context request per HIP-3 DEX, and throws when a response's market and metrics arrays differ in length before index joining them. Equal array lengths do not independently prove identity or order. The inspected workflow covers colon-prefixed builder-DEX markets, filters missing mid prices, and does not preserve a source receipt timestamp in these rows. |

## What this project does

Market-data collector with a Hyperliquid workflow that discovers HIP-3 builder DEX namespaces and stores per-market reference price, volume and open interest. [README](https://github.com/Anish-Agnihotri/stockgecko.com/blob/03261e67510263c1ecfd173fd5e103da2c60820b/README.md).

## Mechanism inspected

It validates locally configured markets against the discovered universe, fans out one context request per HIP-3 DEX, and throws when a response's market and metrics arrays differ in length before index joining them. [Implementation](https://github.com/Anish-Agnihotri/stockgecko.com/blob/03261e67510263c1ecfd173fd5e103da2c60820b/src/workflows/collection/hyperliquid.ts#L40-L109). [Related implementation](https://github.com/Anish-Agnihotri/stockgecko.com/blob/03261e67510263c1ecfd173fd5e103da2c60820b/src/workflows/shared/validate.ts#L10-L32).

## Limitation that matters

Equal array lengths do not independently prove identity or order. The inspected workflow covers colon-prefixed builder-DEX markets, filters missing mid prices, and does not preserve a source receipt timestamp in these rows. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Assert market/context cardinality and coverage before writing each HL snapshot; distinguish missing price from an absent market and record which DEX namespace was requested.

## Why this score

It validates locally configured markets against the discovered universe, fans out one context request per HIP-3 DEX, and throws when a response's market and metrics arrays differ in length before index joining them. Equal array lengths do not independently prove identity or order. The inspected workflow covers colon-prefixed builder-DEX markets, filters missing mid prices, and does not preserve a source receipt timestamp in these rows.

## Source trail

[README](https://github.com/Anish-Agnihotri/stockgecko.com/blob/03261e67510263c1ecfd173fd5e103da2c60820b/README.md) · [Implementation](https://github.com/Anish-Agnihotri/stockgecko.com/blob/03261e67510263c1ecfd173fd5e103da2c60820b/src/workflows/collection/hyperliquid.ts#L40-L109) · [Related implementation](https://github.com/Anish-Agnihotri/stockgecko.com/blob/03261e67510263c1ecfd173fd5e103da2c60820b/src/workflows/shared/validate.ts#L10-L32) · [License](https://github.com/Anish-Agnihotri/stockgecko.com/blob/03261e67510263c1ecfd173fd5e103da2c60820b/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
