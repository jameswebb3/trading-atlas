# nv-sflow - Can multiple consumers share one source collector without losing scope?

**Decision question:** Can multiple consumers share one source collector without losing scope?

| Field | Review |
| --- | --- |
| Upstream | [NVIDIA/nv-sflow](https://github.com/NVIDIA/nv-sflow) |
| Primary area | Operations & Observability |
| Source commit | [1b9e0cdb1389ae60c612f9cf5219648b1b9759b9](https://github.com/NVIDIA/nv-sflow/commit/1b9e0cdb1389ae60c612f9cf5219648b1b9759b9) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The planner groups consumers for a backend and node into one passive collector with the union of requested scopes. Deduplication reduces collector work but does not verify that every expected observation was produced. |

## What this project does

A network telemetry collector that plans backend and node monitors.

## Mechanism inspected

The planner groups consumers for a backend and node into one passive collector with the union of requested scopes.

## Limitation that matters

Deduplication reduces collector work but does not verify that every expected observation was produced.

## Practical check for a trading system

Deduplicate compatible collectors and retain per-consumer scope and coverage receipts.

## Why this score

2/5. The planner pattern can reduce duplicated ingest, provided coverage remains explicit.

## Source trail

[README](https://github.com/NVIDIA/nv-sflow/blob/1b9e0cdb1389ae60c612f9cf5219648b1b9759b9/README.md#L1); [src/sflow/app/monitor_planner.py](https://github.com/NVIDIA/nv-sflow/blob/1b9e0cdb1389ae60c612f9cf5219648b1b9759b9/src/sflow/app/monitor_planner.py#L4); [src/sflow/app/monitor_planner.py](https://github.com/NVIDIA/nv-sflow/blob/1b9e0cdb1389ae60c612f9cf5219648b1b9759b9/src/sflow/app/monitor_planner.py#L16); [src/sflow/app/monitor_planner.py](https://github.com/NVIDIA/nv-sflow/blob/1b9e0cdb1389ae60c612f9cf5219648b1b9759b9/src/sflow/app/monitor_planner.py#L8); [src/sflow/app/monitor_planner.py](https://github.com/NVIDIA/nv-sflow/blob/1b9e0cdb1389ae60c612f9cf5219648b1b9759b9/src/sflow/app/monitor_planner.py#L331).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
