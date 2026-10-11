# Alloy: canonical logs include removals

**Decision question:** Does a log consumer receive enough evidence to reverse a changed chain segment?

| Field | Review |
| --- | --- |
| Upstream | [Alloy](https://github.com/alloy-rs/alloy) |
| Primary area | Market Data & Ingestion |
| Source commit | [88aff80193213e16d428c337a9041e25bc016e43](https://github.com/alloy-rs/alloy/commit/88aff80193213e16d428c337a9041e25bc016e43) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT OR Apache-2.0](https://github.com/alloy-rs/alloy/blob/88aff80193213e16d428c337a9041e25bc016e43/LICENSE-MIT) |
| Review depth | 3/3: documentation, canonical-log stream implementation, and reorg fixture source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Emits removed log batches before replacement batches and includes blocks with no matching logs. A useful reference for canonical event streams and measurable block coverage. |

## Project overview

Rust libraries for Ethereum-compatible RPC, contracts, and network types. Its canonical-log stream reports removed blocks before replacements and retains empty log batches so progress follows blocks rather than event count. [Project documentation](https://github.com/alloy-rs/alloy/blob/88aff80193213e16d428c337a9041e25bc016e43/crates/provider/src/provider/watch_canonical_logs_from.rs#L24-L44).

## Mechanism worth inspecting

[The canonical stream contract](https://github.com/alloy-rs/alloy/blob/88aff80193213e16d428c337a9041e25bc016e43/crates/provider/src/provider/watch_canonical_logs_from.rs#L24-L44) describes block-consistent log batches, removal events, and empty blocks. [The reconciler](https://github.com/alloy-rs/alloy/blob/88aff80193213e16d428c337a9041e25bc016e43/crates/provider/src/provider/watch_canonical_logs_from.rs#L190-L265) compares parent hashes, removes buffered batches, walks missing parents, and emits the replacement segment. It abandons an item if a second reorg changes the parent while reconciliation is in flight.

[The reorg fixture](https://github.com/alloy-rs/alloy/blob/88aff80193213e16d428c337a9041e25bc016e43/crates/provider/src/provider/watch_canonical_logs_from.rs#L345-L387) expects removal of the old block before additions and separately checks an empty batch advances canonical progress. [The deeper-fork fixture](https://github.com/alloy-rs/alloy/blob/88aff80193213e16d428c337a9041e25bc016e43/crates/provider/src/provider/watch_canonical_logs_from.rs#L538-L572) expects available removals followed by an error. These fixtures were read, not run.

## Important limit

[The buffer setting](https://github.com/alloy-rs/alloy/blob/88aff80193213e16d428c337a9041e25bc016e43/crates/provider/src/provider/watch_canonical_logs_from.rs#L97-L120) caps retained block/log history; [the stream state](https://github.com/alloy-rs/alloy/blob/88aff80193213e16d428c337a9041e25bc016e43/crates/provider/src/provider/watch_canonical_logs_from.rs#L145-L152) is held in a fixed buffer. It is not a persistent application checkpoint or an undo journal for a database. Consumers must apply removals to their own rows and derived aggregates, define restart behavior, and choose a justified finality/depth policy. A removed event can precede a terminal error, so partially applied rollback needs explicit handling.

## Questions to take into your own design

- Are empty blocks acknowledged so event absence can be distinguished from an unscanned range?
- Can the sink apply removals, replacements, and restart checkpoints without exposing inconsistent aggregates?

## Why this score for a trading system

Canonical add/remove semantics and empty-block progress directly support reliable on-chain features, with source fixtures for normal and excessive reorg depth; persistent sink correctness is still external.

**Scope of this review:** Root/provider documentation, canonical log stream, buffer limits, and reorg/empty-block fixtures; signing and the rest of Alloy were not evaluated.
