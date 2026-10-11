# Kubeflow Pipelines - Must a worker wait for its informer cache before handling queued work?

**Decision question:** Must a worker wait for its informer cache before handling queued work?

| Field | Review |
| --- | --- |
| Upstream | [kubeflow/pipelines](https://github.com/kubeflow/pipelines) |
| Primary area | Research & Reproducibility |
| Source commit | [a866763fca06c6d9506ace2080c2b5ac38ddb55b](https://github.com/kubeflow/pipelines/commit/a866763fca06c6d9506ace2080c2b5ac38ddb55b) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The persistence agent waits for the informer cache to synchronize before it consumes work queues. Cache synchronization is not equivalent to durable completion of a pipeline or experiment artifact. |

## What this project does

A Kubernetes-backed machine-learning pipeline system.

## Mechanism inspected

The persistence agent waits for the informer cache to synchronize before it consumes work queues.

## Limitation that matters

Cache synchronization is not equivalent to durable completion of a pipeline or experiment artifact.

## Practical check for a trading system

Gate job handling on initialized metadata, then require separate durable result receipts.

## Why this score

2/5. The startup gate is concrete, while experiment completion needs stronger evidence.

## Source trail

[README](https://github.com/kubeflow/pipelines/blob/a866763fca06c6d9506ace2080c2b5ac38ddb55b/README.md#L1); [backend/src/agent/persistence/persistence_agent.go](https://github.com/kubeflow/pipelines/blob/a866763fca06c6d9506ace2080c2b5ac38ddb55b/backend/src/agent/persistence/persistence_agent.go#L86); [backend/src/agent/persistence/persistence_agent.go](https://github.com/kubeflow/pipelines/blob/a866763fca06c6d9506ace2080c2b5ac38ddb55b/backend/src/agent/persistence/persistence_agent.go#L105).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
