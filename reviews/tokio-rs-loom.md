# Loom — Did a concurrency test exhaust its schedules or its budget

**Decision question:** Did a concurrency test exhaust its schedules or its budget?

| Field | Review |
| --- | --- |
| Upstream | [Loom](https://github.com/tokio-rs/loom) |
| Primary area | Testing & Verification |
| Source commit | [948c8cc78b178ede6eeff3afc7d97f2f4ea08559](https://github.com/tokio-rs/loom/commit/948c8cc78b178ede6eeff3afc7d97f2f4ea08559) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/tokio-rs/loom/blob/948c8cc78b178ede6eeff3afc7d97f2f4ea08559/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A strong concurrency-testing reference for controlled interleavings. Record the exploration bounds and termination reason: reaching a schedule or time budget cannot support the same claim as exhausting the modeled state space. |

## Project overview

Loom explores interleavings and memory behavior of concurrent Rust code through instrumented concurrency primitives. [Project documentation](https://github.com/tokio-rs/loom/blob/948c8cc78b178ede6eeff3afc7d97f2f4ea08559/src/lib.rs#L4-L20).

## Mechanism worth inspecting

The model builder exposes thread, branch and preemption limits. Its exploration loop returns when configured permutation or duration limits are reached. [Bounds](https://github.com/tokio-rs/loom/blob/948c8cc78b178ede6eeff3afc7d97f2f4ea08559/src/model.rs#L11-L42), [termination](https://github.com/tokio-rs/loom/blob/948c8cc78b178ede6eeff3afc7d97f2f4ea08559/src/model.rs#L165-L188). The usage contract substitutes Loom primitives for the operations under study. [Instrumentation](https://github.com/tokio-rs/loom/blob/948c8cc78b178ede6eeff3afc7d97f2f4ea08559/src/lib.rs#L63-L88).

## Important limit

A bounded pass does not prove exhaustive exploration, and uninstrumented I/O remains outside the model. The README also records incomplete C11 coverage for load-buffering behavior, so even full exploration is not a proof for all hardware executions. [Documented limitation](https://github.com/tokio-rs/loom/blob/948c8cc78b178ede6eeff3afc7d97f2f4ea08559/README.md#L69-L80).

## Questions to take into your own design

- Did a concurrency test exhaust its schedules or its budget?
- Does the test report its explored bounds, termination reason and excluded memory behaviors?

## Why this score for a trading system

3/5: precise transferable bounded exploration; instrumented Rust concurrency and real exchange chronology remain different test domains.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
