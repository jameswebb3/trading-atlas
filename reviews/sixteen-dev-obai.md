# OBaI - Will an asynchronous backtest remain traceable after a restart?

**Decision question:** Will an asynchronous backtest remain traceable after a restart?

| Field | Review |
| --- | --- |
| Upstream | [sixteen-dev/obai](https://github.com/sixteen-dev/obai) |
| Primary area | Research & Reproducibility |
| Source commit | [69b478152d4489bc0a1be00cd17f7e8bc610c5df](https://github.com/sixteen-dev/obai/commit/69b478152d4489bc0a1be00cd17f7e8bc610c5df) |
| Reviewed | 2026-10-11 |
| Declared license | Commons Clause condition on upstream license; inspect before reuse |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | JobStore assigns IDs and explicit queued, running, completed and failed states. Terminal results are written as JSON sidecars; the loader can label a persisted running job orphaned. Submission and transition to running modify only memory; _persist is called in the task's finally block. A process crash before that block leaves no sidecar for an in-flight job, so the documented orphan marker cannot cover the ordinary crash path. Persistence write errors are logged and ignored. |

## What this project does

Async backtests have explicit job IDs and terminal sidecars, but an in-flight job is not durably recorded before execution.

## Mechanism inspected

JobStore assigns IDs and explicit queued, running, completed and failed states. Terminal results are written as JSON sidecars; the loader can label a persisted running job orphaned.

## Limitation that matters

Submission and transition to running modify only memory; _persist is called in the task's finally block. A process crash before that block leaves no sidecar for an in-flight job, so the documented orphan marker cannot cover the ordinary crash path. Persistence write errors are logged and ignored.

## Practical check for a trading system

Persist acceptance before dispatch, persist state transitions durably, and make restart reconciliation return a definitive result for every accepted job ID.

## Why this score

3/5. The job contract and its crash gap are a transferable reference for research infrastructure; the upstream license also limits reuse.

## Source trail

[README.md](https://github.com/sixteen-dev/obai/blob/69b478152d4489bc0a1be00cd17f7e8bc610c5df/README.md#L1); [src/backtest-server/README.md](https://github.com/sixteen-dev/obai/blob/69b478152d4489bc0a1be00cd17f7e8bc610c5df/src/backtest-server/README.md#L1); [src/backtest-server/src/jobs.py](https://github.com/sixteen-dev/obai/blob/69b478152d4489bc0a1be00cd17f7e8bc610c5df/src/backtest-server/src/jobs.py#L66); [src/backtest-server/src/jobs.py](https://github.com/sixteen-dev/obai/blob/69b478152d4489bc0a1be00cd17f7e8bc610c5df/src/backtest-server/src/jobs.py#L96); [src/backtest-server/src/jobs.py](https://github.com/sixteen-dev/obai/blob/69b478152d4489bc0a1be00cd17f7e8bc610c5df/src/backtest-server/src/jobs.py#L153); [src/backtest-server/src/jobs.py](https://github.com/sixteen-dev/obai/blob/69b478152d4489bc0a1be00cd17f7e8bc610c5df/src/backtest-server/src/jobs.py#L175); [src/backtest-server/src/jobs.py](https://github.com/sixteen-dev/obai/blob/69b478152d4489bc0a1be00cd17f7e8bc610c5df/src/backtest-server/src/jobs.py#L189); [LICENSE](https://github.com/sixteen-dev/obai/blob/69b478152d4489bc0a1be00cd17f7e8bc610c5df/LICENSE#L1)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
