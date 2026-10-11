# Clamp Core - Does a step status carry enough information for safe retries?

**Decision question:** Does a step status carry enough information for safe retries?

| Field | Review |
| --- | --- |
| Upstream | [clamp-orchestrator/clamp-core](https://github.com/clamp-orchestrator/clamp-core) |
| Primary area | Research & Reproducibility |
| Source commit | [b7b5e44547a2c4f4a855b55e2d8da02ef8652e8c](https://github.com/clamp-orchestrator/clamp-core/commit/b7b5e44547a2c4f4a855b55e2d8da02ef8652e8c) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its status model records step name, state, elapsed time and creation time. Those fields do not define whether a failed step performed an external side effect or can be retried safely. |

## What this project does

A Go workflow orchestration core.

## Mechanism inspected

Its status model records step name, state, elapsed time and creation time.

## Limitation that matters

Those fields do not define whether a failed step performed an external side effect or can be retried safely.

## Practical check for a trading system

Record idempotency key, side-effect receipt and retry policy with status.

## Why this score

1/5. Status visibility alone is not an execution contract.

## Source trail

[README](https://github.com/clamp-orchestrator/clamp-core/blob/b7b5e44547a2c4f4a855b55e2d8da02ef8652e8c/README.md#L1); [models/step_status.go](https://github.com/clamp-orchestrator/clamp-core/blob/b7b5e44547a2c4f4a855b55e2d8da02ef8652e8c/models/step_status.go#L16); [Root license](https://github.com/clamp-orchestrator/clamp-core/blob/b7b5e44547a2c4f4a855b55e2d8da02ef8652e8c/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
