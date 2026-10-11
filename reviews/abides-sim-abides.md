# ABIDES — Does a simulated message arrive before the sender could have produced it

**Decision question:** Does a simulated message arrive before the sender could have produced it?

| Field | Review |
| --- | --- |
| Upstream | [ABIDES](https://github.com/abides-sim/abides) |
| Primary area | Backtesting & Simulation |
| Source commit | [c4bf157678928934417aba6073eb0651aeaf6d15](https://github.com/abides-sim/abides/commit/c4bf157678928934417aba6073eb0651aeaf6d15) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/abides-sim/abides/blob/c4bf157678928934417aba6073eb0651aeaf6d15/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Separates computation, pipeline and network delay before a message becomes visible to its recipient. Useful for checking replay causality without treating configured latency as measured market evidence. |

## Project overview

An agent-based discrete-event simulator designed for market research, with communication latency between simulated agents. [Project documentation](https://github.com/abides-sim/abides/blob/c4bf157678928934417aba6073eb0651aeaf6d15/README.md#L1-L11).

## Mechanism worth inspecting

The kernel supplies the send clock and schedules delivery after computation delay, accumulated agent delay, an optional pipeline delay and network latency. Agents cannot directly choose an earlier send timestamp through this method. [Message scheduling](https://github.com/abides-sim/abides/blob/c4bf157678928934417aba6073eb0651aeaf6d15/Kernel.py#L329-L387).

## Important limit

These are configured simulation assumptions. They do not establish the actual latency, exchange queue or fill behavior of a live venue; a faster configured path can still yield an optimistic simulation.

## Questions to take into your own design

- Which timestamp marks computation completion and which marks delivery?
- Can zero-delay settings bypass the latency assumption recorded for the experiment?

## Why this score for a trading system

3/5: a direct causal simulation reference whose market realism depends on independently justified delay assumptions.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
