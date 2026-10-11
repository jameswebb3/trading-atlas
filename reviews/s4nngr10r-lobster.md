# lobster - Will replay stop at a missing or out-of-order event?

**Decision question:** Will replay stop at a missing or out-of-order event?

| Field | Review |
| --- | --- |
| Upstream | [s4nngr10r/lobster](https://github.com/s4nngr10r/lobster) |
| Primary area | Backtesting & Simulation |
| Source commit | [e4784fe0559d730c5f3a6f6a5e0d7d6a7599efb8](https://github.com/s4nngr10r/lobster/commit/e4784fe0559d730c5f3a6f6a5e0d7d6a7599efb8) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Replay rejects invalid, out-of-order, duplicate-live and noncontiguous sequence events. The check cannot recreate events absent before capture; sequence meaning is source-specific. |

## What this project does

A market-data capture and replay tool with explicit sequencing.

## Mechanism inspected

Replay rejects invalid, out-of-order, duplicate-live and noncontiguous sequence events.

## Limitation that matters

The check cannot recreate events absent before capture; sequence meaning is source-specific.

## Practical check for a trading system

Gate book decisions on contiguous source sequences and fail replay at the first unresolved gap.

## Why this score

4/5. A compact and testable replay invariant.

## Source trail

[README](https://github.com/s4nngr10r/lobster/blob/e4784fe0559d730c5f3a6f6a5e0d7d6a7599efb8/README.md#L1); [docs/data-format.md](https://github.com/s4nngr10r/lobster/blob/e4784fe0559d730c5f3a6f6a5e0d7d6a7599efb8/docs/data-format.md#L1); [src/replay/replay_engine.cpp](https://github.com/s4nngr10r/lobster/blob/e4784fe0559d730c5f3a6f6a5e0d7d6a7599efb8/src/replay/replay_engine.cpp#L42); [Root license](https://github.com/s4nngr10r/lobster/blob/e4784fe0559d730c5f3a6f6a5e0d7d6a7599efb8/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
