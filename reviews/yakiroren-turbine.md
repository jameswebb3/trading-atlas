# Turbine: Does a durable step replay guarantee an external side effect happened once?

**Decision question:** Does a durable step replay guarantee an external side effect happened once?

| Field | Review |
| --- | --- |
| Upstream | [YakirOren/turbine](https://github.com/YakirOren/turbine) |
| Primary area | Agents & Decision Systems |
| Source commit | [abb3c012b80cf2e62015cb2e1e706fa5b118f3f8](https://github.com/YakirOren/turbine/commit/abb3c012b80cf2e62015cb2e1e706fa5b118f3f8) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/YakirOren/turbine/blob/abb3c012b80cf2e62015cb2e1e706fa5b118f3f8/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | On recovery, Do checks for a recorded result and returns it without rerunning the step. Otherwise it records start, executes with retries, serializes the output and records completion. WithoutCheckpoint explicitly forces re-execution; runtime startup recovers pending workflows before opening its queue. The checkpoint follows the function call; it cannot atomically commit an external exchange action and local SQLite state. A successful exchange request followed by a local crash may be sent again on recovery. No exchange adapter or exact-once effect is supplied. |

## What this project does

Stores step results in SQLite and replays completed steps on recovery. It executes a new step before recording the result; a crash between an external effect and that record can repeat the effect, so order actions still need idempotency and reconciliation.

## Mechanism inspected

On recovery, Do checks for a recorded result and returns it without rerunning the step. Otherwise it records start, executes with retries, serializes the output and records completion. WithoutCheckpoint explicitly forces re-execution; runtime startup recovers pending workflows before opening its queue.

## Limitation that matters

The checkpoint follows the function call; it cannot atomically commit an external exchange action and local SQLite state. A successful exchange request followed by a local crash may be sent again on recovery. No exchange adapter or exact-once effect is supplied.

## Practical check for a trading system

Crash after request accepted but before local completion write. Resume using the same client order ID, query venue order/fill/position state, and suppress duplicate submission if the effect already occurred.

## Why this score

3/5 transferable: durable replay clarifies an important boundary for execution and agent side effects, but it is a general Go workflow engine and cannot replace venue reconciliation.

## Source trail

[README.md](https://github.com/YakirOren/turbine/blob/abb3c012b80cf2e62015cb2e1e706fa5b118f3f8/README.md#L9); [docs/getting-started.md](https://github.com/YakirOren/turbine/blob/abb3c012b80cf2e62015cb2e1e706fa5b118f3f8/docs/getting-started.md#L23); [runtime.go](https://github.com/YakirOren/turbine/blob/abb3c012b80cf2e62015cb2e1e706fa5b118f3f8/runtime.go#L135); [workflow.go](https://github.com/YakirOren/turbine/blob/abb3c012b80cf2e62015cb2e1e706fa5b118f3f8/workflow.go#L773); [workflow.go](https://github.com/YakirOren/turbine/blob/abb3c012b80cf2e62015cb2e1e706fa5b118f3f8/workflow.go#L812); [workflow.go](https://github.com/YakirOren/turbine/blob/abb3c012b80cf2e62015cb2e1e706fa5b118f3f8/workflow.go#L895)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
