# SQD Pipes SDK: A resume cursor belongs to exactly one pipeline

**Decision question:** Can two data pipelines silently overwrite each other’s resume point?

| Field | Review |
| --- | --- |
| Upstream | [subsquid/pipes-sdk](https://github.com/subsquid/pipes-sdk) |
| Primary area | Market Data & Ingestion |
| Source commit | [b1d46a69dcfd264ad8ff5ceaca275e06e7920f2e](https://github.com/subsquid/pipes-sdk/commit/b1d46a69dcfd264ad8ff5ceaca275e06e7920f2e) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/subsquid/pipes-sdk/blob/b1d46a69dcfd264ad8ff5ceaca275e06e7920f2e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Names each pipeline cursor and keeps a persisted finalized watermark monotonic across restarts. A shared pipeline ID can overwrite progress; finality tracking does not by itself prove that every fill was received. |

## Project overview

TypeScript toolkit for streaming SQD Portal blockchain data into your own storage. Separates streams, decoders, and storage targets, with cursor tracking and chain-reorganization handling.

[Project documentation](https://github.com/subsquid/pipes-sdk/blob/b1d46a69dcfd264ad8ff5ceaca275e06e7920f2e/README.md#L9-L18).

## Mechanism worth inspecting

The error guide makes pipe IDs part of cursor identity and warns that sharing one ID lets two targets overwrite progress. The finalized watermark is seeded from persisted state and clamps later heads so the floor cannot move backward. Its separate Hyperliquid fills source makes the pattern relevant beyond generic chain indexing.

**Source trail:** [project overview](https://github.com/subsquid/pipes-sdk/blob/b1d46a69dcfd264ad8ff5ceaca275e06e7920f2e/README.md) · [documentation](https://github.com/subsquid/pipes-sdk/blob/b1d46a69dcfd264ad8ff5ceaca275e06e7920f2e/docs/errors.md#L46-L58) · [implementation](https://github.com/subsquid/pipes-sdk/blob/b1d46a69dcfd264ad8ff5ceaca275e06e7920f2e/packages/pipes/src/core/finalized-watermark.ts#L27-L72) · [additional source](https://github.com/subsquid/pipes-sdk/blob/b1d46a69dcfd264ad8ff5ceaca275e06e7920f2e/packages/pipes/src/hyperliquid/hyperliquid-fills-portal-source.ts#L42-L75).

## Important limit

A monotonic cursor protects against regression, not missing records within a committed range. Chain finality and exchange fill completeness are different claims; consumers still need reconciliation.

## Questions to take into your own design

- Is the cursor key unique per source, stream, and destination?
- After restart, can the consumer prove the interval before the cursor is complete?

## Why this score for a trading system

A unique cursor and monotonic watermark help Hyperliquid fill ingestion recover, but they cannot prove a cursor interval is complete.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
