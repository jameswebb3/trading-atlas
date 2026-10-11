# Duckle: resume individual work without reusing stale outputs

**Decision question:** What must identify a checkpoint before an expensive item can safely be reused?

| Field | Review |
| --- | --- |
| Upstream | [Duckle](https://github.com/slothflowlabs/duckle) |
| Primary area | Research & Reproducibility |
| Source commit | [f85f8960edfb6efbf4cb89d58a7b32e16df0e867](https://github.com/slothflowlabs/duckle/commit/f85f8960edfb6efbf4cb89d58a7b32e16df0e867) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT OR Apache-2.0](https://github.com/slothflowlabs/duckle/blob/f85f8960edfb6efbf4cb89d58a7b32e16df0e867/LICENSE-MIT) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Offers local ETL pipelines with item-level checkpoints keyed by logical identity, input content, and configuration. Checkpoints store the output itself, giving research jobs a concrete reference for resuming completed work without reusing a result for changed inputs. |

## Project overview

A local ETL platform authors and schedules pipelines on user-controlled infrastructure. [Project documentation](https://github.com/slothflowlabs/duckle/blob/f85f8960edfb6efbf4cb89d58a7b32e16df0e867/README.md#L5-L21).

## Mechanism worth inspecting

The [checkpoint design](https://github.com/slothflowlabs/duckle/blob/f85f8960edfb6efbf4cb89d58a7b32e16df0e867/crates/duckdb-engine/src/checkpoint.rs#L16-L43) stores results rather than success markers. [Item identity](https://github.com/slothflowlabs/duckle/blob/f85f8960edfb6efbf4cb89d58a7b32e16df0e867/crates/duckdb-engine/src/checkpoint.rs#L221-L253) includes logical key, input fingerprint, and configuration fingerprint. [Recording](https://github.com/slothflowlabs/duckle/blob/f85f8960edfb6efbf4cb89d58a7b32e16df0e867/crates/duckdb-engine/src/checkpoint.rs#L116-L134) serializes each completed result under a writer mutex.

## Important limit

[Corrupt records are skipped](https://github.com/slothflowlabs/duckle/blob/f85f8960edfb6efbf4cb89d58a7b32e16df0e867/crates/duckdb-engine/src/checkpoint.rs#L144-L153), causing recomputation. [write_all](https://github.com/slothflowlabs/duckle/blob/f85f8960edfb6efbf4cb89d58a7b32e16df0e867/crates/duckdb-engine/src/checkpoint.rs#L124-L134) does not itself guarantee persistence through power loss, and a failure after an external paid call but before recording can still repeat that call. The README marks the platform beta.

## Questions to take into your own design

- Does a resumed result match both the input content and computation configuration?
- Which failures can cause repeated work despite a checkpoint?

## Why this score for a trading system

3/5: a precise reusable checkpoint identity, constrained by local persistence semantics and a beta platform broader than most research jobs need.

**Scope of this review:** README, architecture documentation, checkpoint source and in-file checkpoint fixtures read.
