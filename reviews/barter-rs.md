# Barter: replay an audit stream into a checked state replica

**Decision question:** Can an external monitor prove that its order state has not skipped an engine event?

| Field | Review |
| --- | --- |
| Upstream | [Barter](https://github.com/barter-rs/barter-rs) |
| Primary area | Execution & Exchange Integration |
| Source commit | [9770b27a83f844472b93b593b08063affc974b0d](https://github.com/barter-rs/barter-rs/commit/9770b27a83f844472b93b593b08063affc974b0d) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/barter-rs/barter-rs/blob/9770b27a83f844472b93b593b08063affc974b0d/LICENSE) |
| Review depth | 2/3: README, audit, replica, order state, and test source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Emits sequenced engine audit ticks and seeds a separate state replica from a snapshot. The replica ignores duplicate or older ticks but errors on a sequence gap before applying the next event. Its order types also distinguish open and cancel requests in flight from exchange-confirmed states. |

## Mechanism worth inspecting

The [README](https://github.com/barter-rs/barter-rs/blob/9770b27a83f844472b93b593b08063affc974b0d/README.md#L43-L58) describes live/mock execution, order management, and an audit-stream state replica. The [auditor](https://github.com/barter-rs/barter-rs/blob/9770b27a83f844472b93b593b08063affc974b0d/barter/src/engine/audit/mod.rs#L20-L65) emits a snapshot or event with a sequence and clock time. The [replica constructor and run loop](https://github.com/barter-rs/barter-rs/blob/9770b27a83f844472b93b593b08063affc974b0d/barter/src/engine/audit/state_replica.rs#L20-L95) start from a snapshot and process later audit events. The [contiguity check](https://github.com/barter-rs/barter-rs/blob/9770b27a83f844472b93b593b08063affc974b0d/barter/src/engine/audit/state_replica.rs#L105-L114) refuses a skipped sequence. The [order state type](https://github.com/barter-rs/barter-rs/blob/9770b27a83f844472b93b593b08063affc974b0d/barter-execution/src/order/state.rs#L15-L109) separates in-flight open/cancel from confirmed open and terminal outcomes. The [audit test](https://github.com/barter-rs/barter-rs/blob/9770b27a83f844472b93b593b08063affc974b0d/barter/tests/test_engine_process_engine_event_with_audit.rs#L93-L124) asserts successive sequence numbers.

## Important limit

The visible replica loop stops successfully when its feed ends; the reviewed path does not itself prove recovery from a process restart or reconstruct missing exchange history. The tests cited here check event sequencing, not a live Hyperliquid trace. This is a pattern for state evidence, not a venue adapter recommendation.

## Questions to take into your own design

- Can a monitoring view name the exact snapshot and last contiguous event it reflects?
- Does it fail visibly on an audit gap before showing fresh state?
- Are local in-flight states kept distinct from venue-confirmed open or cancelled states?

## Why this score for a trading system

Sequenced audit replay and explicit in-flight order states address direct execution and monitoring risks, while restart and venue reconciliation remain outside the inspected path.

**Scope of this review:** We read the pinned overview, selected audit and order-state code, and a sequencing test. We did not run Barter or verify exchange integration.
