# cryo: explicit backfill partitions

**Decision question:** Does a resumable blockchain extract prove which partitions were actually collected?

| Field | Review |
| --- | --- |
| Upstream | [cryo](https://github.com/paradigmxyz/cryo) |
| Primary area | Market Data & Ingestion |
| Source commit | [559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86](https://github.com/paradigmxyz/cryo/commit/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT OR Apache-2.0](https://github.com/paradigmxyz/cryo/blob/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86/LICENSE-MIT) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Builds explicit extraction partitions and separates completed, failed, and skipped work. Useful for planning auditable historical backfills into columnar files. |

## Project overview

Blockchain data extractor for Parquet, CSV, JSON, and Python dataframes. Supports block ranges, selected datasets and columns, and partitioned extraction through JSON-RPC. [Project documentation](https://github.com/paradigmxyz/cryo/blob/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86/README.md#L26-L41).

## Mechanism worth inspecting

The [README's schema and RPC reference](https://github.com/paradigmxyz/cryo/blob/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86/README.md#L90-L130) spells out dataset types and upstream methods. The [partition planner](https://github.com/paradigmxyz/cryo/blob/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86/crates/freeze/src/freeze.rs#L79-L124) creates work per datatype and partition, detects output-path collisions, and bounds concurrent chunks. The [collection summary](https://github.com/paradigmxyz/cryo/blob/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86/crates/freeze/src/freeze.rs#L149-L191) keeps completed, errored, and skipped partitions separate rather than treating partial success as a single finished job.

[Reports](https://github.com/paradigmxyz/cryo/blob/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86/crates/freeze/src/types/reports.rs#L9-L23) record the tool version, command, arguments, and output paths. This is a useful starting pattern for a backfill receipt: planned ranges, outcome per range, row counts, and transformation configuration.

## Important limit

At [the resume decision](https://github.com/paradigmxyz/cryo/blob/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86/crates/freeze/src/freeze.rs#L93-L99), file existence is enough to skip work unless overwrite is enabled. The inspected report structure has no content digest or canonical block-hash receipt. A previously written file could therefore need independent validation before reuse. [The reorg cookbook page](https://github.com/paradigmxyz/cryo/blob/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86/book/cookbook/reorgs.md#L1) contains no procedure at this commit. The [README](https://github.com/paradigmxyz/cryo/blob/559b65455d7ef6b03e8e9e96a0e50fd4fe8a9c86/README.md#L9-L11) calls the project an early work in progress and documents the need to set rate limits for third-party RPC providers.

## Questions to take into your own design

- Can a skipped file be matched to the exact schema, query, source block hashes, and content digest?
- Is partial success published with explicit missing ranges instead of an overall success flag?

## Why this score for a trading system

Partitioned market-data extraction and explicit outcomes are directly useful for research backfills, but file-existence resume and incomplete reorg guidance keep the score at 3/5.

**Scope of this review:** README dataset/schema reference, acquisition and reorg documentation, partition planning, file collection, and report serialization; RPC completeness and extraction performance were not measured.
