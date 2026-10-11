# Celery — Does acknowledging a task after completion guarantee recovery after worker loss

**Decision question:** Does acknowledging a task after completion guarantee recovery after worker loss?

| Field | Review |
| --- | --- |
| Upstream | [Celery](https://github.com/celery/celery) |
| Primary area | Operations & Observability |
| Source commit | [31b6167d95294a4bda00013e44c399a3a62d3d9d](https://github.com/celery/celery/commit/31b6167d95294a4bda00013e44c399a3a62d3d9d) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/celery/celery/blob/31b6167d95294a4bda00013e44c399a3a62d3d9d/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Separates late acknowledgement from worker-loss redelivery policy. Useful for testing the crash interval after a result is written but before completion is acknowledged. |

## Project overview

A distributed Python task queue using messages to distribute work among workers. [Project documentation](https://github.com/celery/celery/blob/31b6167d95294a4bda00013e44c399a3a62d3d9d/README.rst#L91-L108).

## Mechanism worth inspecting

The request handler acknowledges successful late-ACK tasks, but failure handling separately consults reject_on_worker_lost and failure/timeout acknowledgement policy. It can requeue a lost-worker task or acknowledge a failure. [Success and failure policy](https://github.com/celery/celery/blob/31b6167d95294a4bda00013e44c399a3a62d3d9d/celery/worker/request.py#L624-L635), [lost-worker branch](https://github.com/celery/celery/blob/31b6167d95294a4bda00013e44c399a3a62d3d9d/celery/worker/request.py#L705-L721). The task guide explains that late acknowledgement alone does not imply every terminated task is redelivered. [Documented caveat](https://github.com/celery/celery/blob/31b6167d95294a4bda00013e44c399a3a62d3d9d/docs/userguide/tasks.rst#L21-L47).

## Important limit

Redelivery can repeat a side effect already committed before worker loss. Late ACK is a delivery policy, not proof of exactly-once application work or a valid output artefact.

## Questions to take into your own design

- What happens if the worker dies after writing its result but before acknowledging completion?
- Is recovery idempotent at the artefact and decision boundaries?

## Why this score for a trading system

3/5: a concrete transferable task-recovery boundary with direct consequences for experiment and artefact identity.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
