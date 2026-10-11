# skypilot - Fence job recovery when leadership is uncertain

**Decision question:** Can a restarted controller launch work while another leader is still recovering it?

| Field | Review |
| --- | --- |
| Upstream | [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) |
| Primary area | Operations & Observability |
| Source commit | [f616a2fe11056e5779920feab3b87e86f8c78975](https://github.com/skypilot-org/skypilot/commit/f616a2fe11056e5779920feab3b87e86f8c78975) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/skypilot-org/skypilot/blob/f616a2fe11056e5779920feab3b87e86f8c78975/LICENSE)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The refresh daemon gates controller starts before lock acquisition, checks the lock again before recovery, and steps down on loss of its backing session; the old controller is terminated to avoid a second active leader. This is a multi-instance job-control path. It does not make a trading side effect idempotent or reconcile an external fill after a split-brain interval. |

## What this project does

SkyPilot manages distributed AI jobs and their controller state. [README](https://github.com/skypilot-org/skypilot/blob/f616a2fe11056e5779920feab3b87e86f8c78975/README.md).

## Mechanism inspected

The refresh daemon gates controller starts before lock acquisition, checks the lock again before recovery, and steps down on loss of its backing session; the old controller is terminated to avoid a second active leader. [Implementation](https://github.com/skypilot-org/skypilot/blob/f616a2fe11056e5779920feab3b87e86f8c78975/sky/jobs/managed_job_refresh_thread.py#L85-L151). [Related path](https://github.com/skypilot-org/skypilot/blob/f616a2fe11056e5779920feab3b87e86f8c78975/sky/jobs/managed_job_refresh_thread.py#L161-L191).

## Limitation that matters

This is a multi-instance job-control path. It does not make a trading side effect idempotent or reconcile an external fill after a split-brain interval. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

If multiple workers may own one job, require a recovery gate plus a durable leader token; reconcile external side effects before resuming.

## Why this score

The fencing sequence is directly useful for HA orchestration, but the trading side effect still needs its own journal and reconciliation.

## Source trail

[README](https://github.com/skypilot-org/skypilot/blob/f616a2fe11056e5779920feab3b87e86f8c78975/README.md) - [Implementation](https://github.com/skypilot-org/skypilot/blob/f616a2fe11056e5779920feab3b87e86f8c78975/sky/jobs/managed_job_refresh_thread.py#L85-L151) - [Related path](https://github.com/skypilot-org/skypilot/blob/f616a2fe11056e5779920feab3b87e86f8c78975/sky/jobs/managed_job_refresh_thread.py#L161-L191) - [License](https://github.com/skypilot-org/skypilot/blob/f616a2fe11056e5779920feab3b87e86f8c78975/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
