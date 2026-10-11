# Chain Data Indexer - What happens when a block at a known height has a different hash?

**Decision question:** What happens when a block at a known height has a different hash?

| Field | Review |
| --- | --- |
| Upstream | [citizenweb3/chain-data-indexer](https://github.com/citizenweb3/chain-data-indexer) |
| Primary area | Market Data & Ingestion |
| Source commit | [4e6c846ee20b48377bfcb01ab4e51fc297d2cd08](https://github.com/citizenweb3/chain-data-indexer/commit/4e6c846ee20b48377bfcb01ab4e51fc297d2cd08) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The COPY branch deduplicates by height within a batch; the non-COPY branch inserts with ON CONFLICT (height) DO NOTHING. The non-COPY path does not compare an incoming block hash with the stored hash, so a replacement at the same height is ignored there. |

## What this project does

A PostgreSQL-backed blockchain indexer with progress-based resume.

## Mechanism inspected

The COPY branch deduplicates by height within a batch; the non-COPY branch inserts with ON CONFLICT (height) DO NOTHING.

## Limitation that matters

The non-COPY path does not compare an incoming block hash with the stored hash, so a replacement at the same height is ignored there.

## Practical check for a trading system

Compare canonical hashes before advancing the cursor and represent reorg rollback explicitly.

## Why this score

2/5. The height-only idempotence path is a useful on-chain correction caution.

## Source trail

[README](https://github.com/citizenweb3/chain-data-indexer/blob/4e6c846ee20b48377bfcb01ab4e51fc297d2cd08/README.md#L1); [src/sink/pg/flushers/blocks.ts](https://github.com/citizenweb3/chain-data-indexer/blob/4e6c846ee20b48377bfcb01ab4e51fc297d2cd08/src/sink/pg/flushers/blocks.ts#L13); [src/sink/pg/flushers/blocks.ts](https://github.com/citizenweb3/chain-data-indexer/blob/4e6c846ee20b48377bfcb01ab4e51fc297d2cd08/src/sink/pg/flushers/blocks.ts#L52); [src/index.ts](https://github.com/citizenweb3/chain-data-indexer/blob/4e6c846ee20b48377bfcb01ab4e51fc297d2cd08/src/index.ts#L99); [src/index.ts](https://github.com/citizenweb3/chain-data-indexer/blob/4e6c846ee20b48377bfcb01ab4e51fc297d2cd08/src/index.ts#L106); [Root license](https://github.com/citizenweb3/chain-data-indexer/blob/4e6c846ee20b48377bfcb01ab4e51fc297d2cd08/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
