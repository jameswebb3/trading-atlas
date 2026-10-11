# DataWorkers Claw - Is an agent confidence score an adequate execution gate?

**Decision question:** Is an agent confidence score an adequate execution gate?

| Field | Review |
| --- | --- |
| Upstream | [DataWorkersProject/dataworkers-claw-community](https://github.com/DataWorkersProject/dataworkers-claw-community) |
| Primary area | Agents & Decision Systems |
| Source commit | [7bfa6d21d1ae6fc9e05a2e9ca3b3d7f94879e6e5](https://github.com/DataWorkersProject/dataworkers-claw-community/commit/7bfa6d21d1ae6fc9e05a2e9ca3b3d7f94879e6e5) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It requires a numeric confidence threshold before moving from planning to execution. The score comes from the caller; this guard does not independently verify data provenance, tool effects or risk. |

## What this project does

An agent lifecycle state machine.

## Mechanism inspected

It requires a numeric confidence threshold before moving from planning to execution.

## Limitation that matters

The score comes from the caller; this guard does not independently verify data provenance, tool effects or risk.

## Practical check for a trading system

Require external evidence checks and bounded permissions before agent execution.

## Why this score

2/5. The state transition is explicit, but self-rated confidence is weak evidence.

## Source trail

[README](https://github.com/DataWorkersProject/dataworkers-claw-community/blob/7bfa6d21d1ae6fc9e05a2e9ca3b3d7f94879e6e5/README.md#L1); [core/agent-lifecycle/src/state-machine.ts](https://github.com/DataWorkersProject/dataworkers-claw-community/blob/7bfa6d21d1ae6fc9e05a2e9ca3b3d7f94879e6e5/core/agent-lifecycle/src/state-machine.ts#L60); [core/agent-lifecycle/src/state-machine.ts](https://github.com/DataWorkersProject/dataworkers-claw-community/blob/7bfa6d21d1ae6fc9e05a2e9ca3b3d7f94879e6e5/core/agent-lifecycle/src/state-machine.ts#L82); [Root license](https://github.com/DataWorkersProject/dataworkers-claw-community/blob/7bfa6d21d1ae6fc9e05a2e9ca3b3d7f94879e6e5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
