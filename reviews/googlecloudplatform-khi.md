# KHI - Can a lineage planner prevent a cyclic dependency graph?

**Decision question:** Can a lineage planner prevent a cyclic dependency graph?

| Field | Review |
| --- | --- |
| Upstream | [GoogleCloudPlatform/khi](https://github.com/GoogleCloudPlatform/khi) |
| Primary area | Operations & Observability |
| Source commit | [de410cb35eb05522b4e590a9827e9bb9503baa4e](https://github.com/GoogleCloudPlatform/khi/commit/de410cb35eb05522b4e590a9827e9bb9503baa4e) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The graph resolver validates fixed dependencies and prunes candidate fan-in edges that would create cycles. Acyclicity is necessary for ordered tasks but does not establish causal timestamps or complete data. |

## What this project does

A Kubernetes historical inspector with task graph resolution.

## Mechanism inspected

The graph resolver validates fixed dependencies and prunes candidate fan-in edges that would create cycles.

## Limitation that matters

Acyclicity is necessary for ordered tasks but does not establish causal timestamps or complete data.

## Practical check for a trading system

Validate research lineage as a DAG and reject cycle-producing dependencies.

## Why this score

3/5. The cycle guard is a concrete general-purpose integrity check for data pipelines.

## Source trail

[README](https://github.com/GoogleCloudPlatform/khi/blob/de410cb35eb05522b4e590a9827e9bb9503baa4e/README.md#L1); [pkg/core/task/graphresolver_cycle.go](https://github.com/GoogleCloudPlatform/khi/blob/de410cb35eb05522b4e590a9827e9bb9503baa4e/pkg/core/task/graphresolver_cycle.go#L29); [pkg/core/task/graphresolver_cycle.go](https://github.com/GoogleCloudPlatform/khi/blob/de410cb35eb05522b4e590a9827e9bb9503baa4e/pkg/core/task/graphresolver_cycle.go#L184).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
