# txindex - Can an index answer what was known at a block height?

**Decision question:** Can an index answer what was known at a block height?

| Field | Review |
| --- | --- |
| Upstream | [PsyProtocol/txindex](https://github.com/PsyProtocol/txindex) |
| Primary area | Data Quality & Lineage |
| Source commit | [e54ab495bbdcaab231d0108a6fc5400db50d478a](https://github.com/PsyProtocol/txindex/commit/e54ab495bbdcaab231d0108a6fc5400db50d478a) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Executive assessment | Its store reads exact or latest-less-than-equal values at a given block and tracks the latest synced block. Bitcoin height is not a Hyperliquid publication timestamp; this store alone does not prove reorg finality. |

## What this project does

A Bitcoin transaction indexer using block-indexed key-value tables.

## Mechanism inspected

Its store reads exact or latest-less-than-equal values at a given block and tracks the latest synced block.

## Limitation that matters

Bitcoin height is not a Hyperliquid publication timestamp; this store alone does not prove reorg finality.

## Practical check for a trading system

Carry source block identity and query as-of boundaries only with explicit finality rules.

## Why this score

2/5. Block-versioned reads transfer as a pattern, not as a venue clock.

## Source trail

[README](https://github.com/PsyProtocol/txindex/blob/e54ab495bbdcaab231d0108a6fc5400db50d478a/README.md#L1); [txindex_common/src/db/indexed_block_db.rs](https://github.com/PsyProtocol/txindex/blob/e54ab495bbdcaab231d0108a6fc5400db50d478a/txindex_common/src/db/indexed_block_db.rs#L36); [Root license](https://github.com/PsyProtocol/txindex/blob/e54ab495bbdcaab231d0108a6fc5400db50d478a/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
