# Substreams: roll back data and cursor together

**Decision question:** Can an on-chain sink reverse a fork without leaving its saved cursor ahead of its data?

| Field | Review |
| --- | --- |
| Upstream | [Substreams](https://github.com/streamingfast/substreams) |
| Primary area | Market Data & Ingestion |
| Source commit | [9993cd94b53fad358235aa52ff43e57334c1e33d](https://github.com/streamingfast/substreams/commit/9993cd94b53fad358235aa52ff43e57334c1e33d) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Pairs row-change history with a transactional cursor update during SQL rollback. Also exposes block-hash undo notifications to cancel work based on invalidated blocks. |

## Project overview

Blockchain stream-processing system with composable modules and SQL sinks. Its database-changes path records reversible row operations and updates the stream cursor in the same transaction as a rollback. [Project documentation](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/docs/references/sql/reorg-handling.md#L17-L38).

## Mechanism worth inspecting

The [SQL reorg reference](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/docs/references/sql/reorg-handling.md#L17-L38) describes insert/update/delete history for the reversible chain segment. [The PostgreSQL implementation](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/sink/sql/db_changes/db/dialect_postgres.go#L36-L82) collects operations after the rollback target and applies their inverses. [The loader](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/sink/sql/db_changes/db/flush.go#L50-L75) performs that reversion, updates the module's cursor through the same transaction, and commits.

There is also a [block-hash undo manager](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/pipeline/exec/undo_manager.go#L91-L115): a subscription is cancelled immediately if its block was already undone, and [undo processing](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/pipeline/exec/undo_manager.go#L40-L63) notifies existing subscribers. This is useful for invalidating computations whose inputs leave the canonical chain. The [fixture](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/pipeline/exec/undo_manager_test.go#L33-L98) explicitly checks both subscription timings; it was read, not executed.

## Important limit

The [documentation](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/docs/references/sql/reorg-handling.md#L9-L15) distinguishes database changes, relational mappings, and delayed signalling; the latter modes are not explained by this reference. It [requires primary keys](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/docs/references/sql/reorg-handling.md#L166-L171) and records storage/write overhead. [The file cursor writer](https://github.com/streamingfast/substreams/blob/9993cd94b53fad358235aa52ff43e57334c1e33d/sink/cursor.go#L25-L53) uses a temporary file and rename, which protects that file replacement but does not atomically acknowledge a separate destination write. Undo events also require downstream computations to implement cancellation or invalidation.

## Questions to take into your own design

- Are destination updates, undo history, and the resume cursor one database transaction?
- Can every derived feature name the input block hashes whose removal invalidates it?

## Why this score for a trading system

Transactional rollback progress and block-specific invalidation directly protect trading datasets from fork-induced inconsistency; guarantees remain specific to the inspected sink path.

**Scope of this review:** README, database-changes reorg documentation, PostgreSQL reversion and cursor transaction, undo subscriptions and their fixtures, and standalone cursor persistence; other SQL modes and distributed execution were not evaluated.
