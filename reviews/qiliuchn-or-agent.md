# OR-Agent - Can an automated experiment search resume within a fixed budget?

**Decision question:** Can an automated experiment search resume within a fixed budget?

| Field | Review |
| --- | --- |
| Upstream | [qiliuchn/OR-Agent](https://github.com/qiliuchn/OR-Agent) |
| Primary area | Agents & Decision Systems |
| Source commit | [f64b92db5e66f312409b0c91b67ff8aa084b0777](https://github.com/qiliuchn/OR-Agent/commit/f64b92db5e66f312409b0c91b67ff8aa084b0777) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The agent loads checkpoint counters, enforces maximum repeats and persists search state as it proceeds. A bounded search does not protect an untouched holdout or validate the metric chosen by the agent. |

## What this project does

An operations-research agent with checkpointed experiment exploration.

## Mechanism inspected

The agent loads checkpoint counters, enforces maximum repeats and persists search state as it proceeds.

## Limitation that matters

A bounded search does not protect an untouched holdout or validate the metric chosen by the agent.

## Practical check for a trading system

Persist search budget and state while keeping final validation outside agent-controlled trials.

## Why this score

2/5. Checkpointing reduces duplicate trials; scientific separation still matters.

## Source trail

[README](https://github.com/qiliuchn/OR-Agent/blob/f64b92db5e66f312409b0c91b67ff8aa084b0777/README.md#L1); [src/oragent/experiment_agent.py](https://github.com/qiliuchn/OR-Agent/blob/f64b92db5e66f312409b0c91b67ff8aa084b0777/src/oragent/experiment_agent.py#L205); [src/oragent/experiment_agent.py](https://github.com/qiliuchn/OR-Agent/blob/f64b92db5e66f312409b0c91b67ff8aa084b0777/src/oragent/experiment_agent.py#L253).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
