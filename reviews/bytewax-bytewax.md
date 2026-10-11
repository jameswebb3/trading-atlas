# Bytewax — Can a recovered dataflow resume from a checkpoint with missing partitions

**Decision question:** Can a recovered dataflow resume from a checkpoint with missing partitions?

| Field | Review |
| --- | --- |
| Upstream | [Bytewax](https://github.com/bytewax/bytewax) |
| Primary area | Data Quality & Lineage |
| Source commit | [9fce5b6ee43780329b05a2ecc1057ffddd51255d](https://github.com/bytewax/bytewax/commit/9fce5b6ee43780329b05a2ecc1057ffddd51255d) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/bytewax/bytewax/blob/9fce5b6ee43780329b05a2ecc1057ffddd51255d/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Rejects incomplete recovery partitions and derives a coordinated resume point. Useful for consistent checkpoint sets, with external-output deduplication still required after recovery. |

## Project overview

A Python framework backed by a Rust engine for stateful event and stream processing, including recovery and event-time windows. [Project documentation](https://github.com/bytewax/bytewax/blob/9fce5b6ee43780329b05a2ecc1057ffddd51255d/README.md#L23-L27).

## Mechanism worth inspecting

The recovery calculator requires a consistent partition count and all expected partition IDs, then computes a shared resume frontier from worker progress. It rejects snapshots whose collected partition state cannot cover that frontier. [Partition checks and resume calculation](https://github.com/bytewax/bytewax/blob/9fce5b6ee43780329b05a2ecc1057ffddd51255d/src/recovery.rs#L1180-L1272).

## Important limit

The recovery guide explicitly warns that some connectors can duplicate outputs around a restart and recommends idempotent or at-least-once designs. Recovering internal state does not establish exactly-once external effects. [Recovery caveat](https://github.com/bytewax/bytewax/blob/9fce5b6ee43780329b05a2ecc1057ffddd51255d/docs/guide/concepts/recovery.md#L35-L42).

## Questions to take into your own design

- Can every required state partition reconstruct the chosen resume boundary?
- Does the resumed output carry an identity that survives duplicate delivery?

## Why this score for a trading system

3/5: a concrete transferable completeness gate for checkpoints; connector effects remain a separate guarantee.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
