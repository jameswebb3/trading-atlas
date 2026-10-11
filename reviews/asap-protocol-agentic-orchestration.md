# Agentic Orchestration - Can an agent workflow resume after process loss?

**Decision question:** Can an agent workflow resume after process loss?

| Field | Review |
| --- | --- |
| Upstream | [asap-protocol/agentic-orchestration](https://github.com/asap-protocol/agentic-orchestration) |
| Primary area | Research & Reproducibility |
| Source commit | [6b207363fdb0b411c08656c88090e8da314b23f8](https://github.com/asap-protocol/agentic-orchestration/commit/6b207363fdb0b411c08656c88090e8da314b23f8) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | The executor walks nodes and stores outputs in an execution context variable map. The inspected route keeps progress in memory and provides no durable step journal for restart. |

## What this project does

An in-process agent workflow executor.

## Mechanism inspected

The executor walks nodes and stores outputs in an execution context variable map.

## Limitation that matters

The inspected route keeps progress in memory and provides no durable step journal for restart.

## Practical check for a trading system

Persist step-level input, output and approval state before resuming agents.

## Why this score

1/5. A simple control-flow reference with weak evidence durability.

## Source trail

[README](https://github.com/asap-protocol/agentic-orchestration/blob/6b207363fdb0b411c08656c88090e8da314b23f8/README.md#L1); [src/lib/workflow-executor.ts](https://github.com/asap-protocol/agentic-orchestration/blob/6b207363fdb0b411c08656c88090e8da314b23f8/src/lib/workflow-executor.ts#L63).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
