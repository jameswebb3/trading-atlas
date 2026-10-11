# Squid SDK: contiguous archives and reversible blocks

**Decision question:** Which evidence makes a blockchain archive continuous and its derived state reversible?

| Field | Review |
| --- | --- |
| Upstream | [Squid SDK](https://github.com/subsquid/squid-sdk) |
| Primary area | Market Data & Ingestion |
| Source commit | [b19df690115eeda90e6b2e29bd6183d8f8d3da5b](https://github.com/subsquid/squid-sdk/commit/b19df690115eeda90e6b2e29bd6183d8f8d3da5b) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/subsquid/squid-sdk/blob/b19df690115eeda90e6b2e29bd6183d8f8d3da5b/LICENSE) |
| Review depth | 3/3: documentation, archive and processor implementation, and rollback-index test source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Separates finalized and reversible block state, and checks consecutive heights in its Hyperliquid fill archive reader. Useful references for backfill continuity and database progress. |

## Project overview

TypeScript toolkit for blockchain ETL, with processors, codecs, database adapters, and selective data access. The repository also contains Hyperliquid archive readers that check consecutive block numbers before yielding batches. [Project documentation](https://github.com/subsquid/squid-sdk/blob/b19df690115eeda90e6b2e29bd6183d8f8d3da5b/README.md#L7-L22).

## Mechanism worth inspecting

The [processor database contract](https://github.com/subsquid/squid-sdk/blob/b19df690115eeda90e6b2e29bd6183d8f8d3da5b/processor/batch-processor/src/database.ts#L7-L51) distinguishes finalized state from a reversible top and carries hash plus height. The [batch path](https://github.com/subsquid/squid-sdk/blob/b19df690115eeda90e6b2e29bd6183d8f8d3da5b/processor/batch-processor/src/run.ts#L227-L275) sends reversible slices through a hot transaction and rejects unfinalized blocks for a final-only database. The [TypeORM implementation](https://github.com/subsquid/squid-sdk/blob/b19df690115eeda90e6b2e29bd6183d8f8d3da5b/typeorm/typeorm-store/src/database.ts#L204-L271) rolls back the replaced tail, applies updates, and updates status in its transaction wrapper. [Rollback-index fixtures](https://github.com/subsquid/squid-sdk/blob/b19df690115eeda90e6b2e29bd6183d8f8d3da5b/processor/batch-processor/src/find-rollback-index.test.ts#L9-L59) include same-height hash changes and partially overlapping histories.

Separately, the [Hyperliquid archive reader](https://github.com/subsquid/squid-sdk/blob/b19df690115eeda90e6b2e29bd6183d8f8d3da5b/hyperliquid/hyperliquid-fills-ingest/src/archive.ts#L34-L72) asserts each accepted block equals the next expected height before yielding batches. That is a concrete continuity gate, not a row-count guess.

## Important limit

The [Hyperliquid fill normalizer](https://github.com/subsquid/squid-sdk/blob/b19df690115eeda90e6b2e29bd6183d8f8d3da5b/hyperliquid/hyperliquid-fills-normalization/src/mapping.ts#L6-L54) converts prices, sizes, fees, and PnL from decimal strings to JavaScript numbers and sets both block and parent hashes to zero. Its output cannot support hash-based fork verification or preserve every original decimal representation. The [ingestion path](https://github.com/subsquid/squid-sdk/blob/b19df690115eeda90e6b2e29bd6183d8f8d3da5b/hyperliquid/hyperliquid-fills-ingest/src/ingest.ts#L26-L56) reads a requester-pays S3 archive and uses block timestamp; it does not record the original publication time of each archive object.

## Questions to take into your own design

- Does an archive manifest prove every requested height was read, including empty blocks?
- Are original decimal strings, real block identity where available, and object observation times retained before normalization?

## Why this score for a trading system

Archive continuity and reversible transaction progress directly support trading-data ingestion; the Hyperliquid hash and numeric conversions materially limit what the normalized output proves.

**Scope of this review:** Batch database interfaces, TypeORM hot transactions, rollback-index fixtures, and Hyperliquid fills ingestion/normalization; the SQD network service and other chain processors were not evaluated.
