# Shuttle — Can a saved race trace prove it replayed completely

**Decision question:** Can a saved race trace prove it replayed completely?

| Field | Review |
| --- | --- |
| Upstream | [Shuttle](https://github.com/awslabs/shuttle) |
| Primary area | Testing & Verification |
| Source commit | [4cb87c1c37ea0d9b412a2716e95e70188d2157ee](https://github.com/awslabs/shuttle/commit/4cb87c1c37ea0d9b412a2716e95e70188d2157ee) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/awslabs/shuttle/blob/4cb87c1c37ea0d9b412a2716e95e70188d2157ee/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful concurrency reference for saving and replaying failing schedules. Keep code identity and completion policy with the trace, and distinguish deterministic reproduction from exhaustive race coverage. |

## Project overview

Shuttle tests concurrent Rust code with controlled schedulers and replayable execution traces. [Project documentation](https://github.com/awslabs/shuttle/blob/4cb87c1c37ea0d9b412a2716e95e70188d2157ee/shuttle-schedulers/README.md#L3-L23).

## Mechanism worth inspecting

ReplayScheduler recreates its data source from the recorded seed and selects recorded runnable tasks. An early end is rejected unless incomplete replay is explicitly enabled. [Replay initialization](https://github.com/awslabs/shuttle/blob/4cb87c1c37ea0d9b412a2716e95e70188d2157ee/shuttle-schedulers/src/replay.rs#L40-L58), [schedule gate](https://github.com/awslabs/shuttle/blob/4cb87c1c37ea0d9b412a2716e95e70188d2157ee/shuttle-schedulers/src/replay.rs#L79-L118).

## Important limit

A saved schedule depends on the code and controlled sources of nondeterminism. Allowing an incomplete schedule weakens what a replay pass establishes; neither random scheduling nor one replay proves all interleavings.

## Questions to take into your own design

- Can a saved race trace prove it replayed completely?
- Is incomplete replay disabled when claiming reproduction of a complete failing trace?

## Why this score for a trading system

3/5: concrete transferable replay contract, without exchange-event modeling or a guarantee for uncontrolled I/O and randomness.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
