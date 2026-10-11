# FedML - What is lost when many job failures become one status?

**Decision question:** What is lost when many job failures become one status?

| Field | Review |
| --- | --- |
| Upstream | [FedML-AI/FedML](https://github.com/FedML-AI/FedML) |
| Primary area | Research & Reproducibility |
| Source commit | [03e11dfee69a458a9820ec4e05b531a5f935eb2b](https://github.com/FedML-AI/FedML/commit/03e11dfee69a458a9820ec4e05b531a5f935eb2b) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | The job adapter maps STOPPING, KILLED, BLOCKED, INVALID and other states into FAILED. The normalized state loses the causal reason needed to decide retry, repair or quarantine. |

## What this project does

A distributed and federated ML workflow framework.

## Mechanism inspected

The job adapter maps STOPPING, KILLED, BLOCKED, INVALID and other states into FAILED.

## Limitation that matters

The normalized state loses the causal reason needed to decide retry, repair or quarantine.

## Practical check for a trading system

Keep original failure code alongside aggregate status in research runs.

## Why this score

1/5. The failure-taxonomy lesson is transferable; the framework is distant from this trading stack.

## Source trail

[README](https://github.com/FedML-AI/FedML/blob/03e11dfee69a458a9820ec4e05b531a5f935eb2b/README.md#L1); [python/fedml/workflow/jobs.py](https://github.com/FedML-AI/FedML/blob/03e11dfee69a458a9820ec4e05b531a5f935eb2b/python/fedml/workflow/jobs.py#L28); [Root license](https://github.com/FedML-AI/FedML/blob/03e11dfee69a458a9820ec4e05b531a5f935eb2b/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
