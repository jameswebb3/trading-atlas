# Ponder: reversible indexing state

**Decision question:** Can an indexer undo derived rows when the canonical chain changes?

| Field | Review |
| --- | --- |
| Upstream | [Ponder](https://github.com/ponder-sh/ponder) |
| Primary area | Market Data & Ingestion |
| Source commit | [6b0bd2cb598c99ea8a36bc17b005352ef5856b36](https://github.com/ponder-sh/ponder/commit/6b0bd2cb598c99ea8a36bc17b005352ef5856b36) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/ponder-sh/ponder/blob/6b0bd2cb598c99ea8a36bc17b005352ef5856b36/LICENSE) |
| Review depth | 3/3: documentation, implementation, and rollback test source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Indexes EVM events into queryable tables and uses a database change log to undo forked state. The same handlers serve backfills and live indexing. |

## Project overview

TypeScript framework for indexing EVM contracts and accounts into PostgreSQL, with SQL and GraphQL access. Its indexing engine records reversible database changes so derived tables can follow the canonical chain. [Project documentation](https://github.com/ponder-sh/ponder/blob/6b0bd2cb598c99ea8a36bc17b005352ef5856b36/README.md#L18-L24).

## Mechanism worth inspecting

The [indexing guide](https://github.com/ponder-sh/ponder/blob/6b0bd2cb598c99ea8a36bc17b005352ef5856b36/docs/pages/docs/indexing/overview.mdx#L33-L57) describes cache eviction, rollback to a common ancestor, and replay through the same handlers. In the [database implementation](https://github.com/ponder-sh/ponder/blob/6b0bd2cb598c99ea8a36bc17b005352ef5856b36/packages/core/src/database/actions.ts#L418-L485), reversion selects logged operations after a checkpoint and restores the earlier row state inside a transaction. [The restoration SQL](https://github.com/ponder-sh/ponder/blob/6b0bd2cb598c99ea8a36bc17b005352ef5856b36/packages/core/src/database/actions.ts#L792-L821) distinguishes inserted rows from updates and deletions.

The [rollback test](https://github.com/ponder-sh/ponder/blob/6b0bd2cb598c99ea8a36bc17b005352ef5856b36/packages/core/src/database/actions.test.ts#L407-L462) inserts, updates, and deletes an account across blocks, then asserts that rollback restores its earlier balance and removes a later insertion. This test was read, not run. The reusable design is a bounded undo journal for derived tables, with canonical replay using the original transformation.

## Important limit

The [realtime reconciler](https://github.com/ponder-sh/ponder/blob/6b0bd2cb598c99ea8a36bc17b005352ef5856b36/packages/core/src/sync-realtime/index.ts#L890-L952) follows parent hashes within retained unfinalized blocks and errors when no common ancestor remains. Its [finalization calculation](https://github.com/ponder-sh/ponder/blob/6b0bd2cb598c99ea8a36bc17b005352ef5856b36/packages/core/src/sync-realtime/index.ts#L1159-L1206) uses the configured block count; that policy must be chosen for the target chain. The [crash-recovery documentation](https://github.com/ponder-sh/ponder/blob/6b0bd2cb598c99ea8a36bc17b005352ef5856b36/docs/pages/docs/indexing/overview.mdx#L49-L57) conditions recovery on the same exact configuration. This journal does not by itself preserve the time a trading process first received each value.

## Questions to take into your own design

- Are derived rows and their undo records committed together, including deletes and repeated updates?
- What happens when a fork crosses the retained history, or the indexing configuration changes?

## Why this score for a trading system

Reverting derived market observations and replaying canonical events address a direct trading-data integrity risk; the source and rollback fixture are concrete, while finality and observation-time policy remain external.

**Scope of this review:** EVM handler ordering, database undo operations, one rollback fixture, and the realtime finality boundary; API deployment and runtime performance were not evaluated.
