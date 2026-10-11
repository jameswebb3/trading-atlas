# Seldon Core - Is a model artifact reproducible when its initializer image floats?

**Decision question:** Is a model artifact reproducible when its initializer image floats?

| Field | Review |
| --- | --- |
| Upstream | [SeldonIO/seldon-core](https://github.com/SeldonIO/seldon-core) |
| Primary area | Research & Reproducibility |
| Source commit | [6c363b18d03a8701fed66464cfffc439477dcce4](https://github.com/SeldonIO/seldon-core/commit/6c363b18d03a8701fed66464cfffc439477dcce4) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The controller injects an initializer container to stage a model artifact from a configured URI. The inspected default image version is latest, so an unpinned initializer can change the loading environment across deployments. |

## What this project does

A Kubernetes model-serving controller.

## Mechanism inspected

The controller injects an initializer container to stage a model artifact from a configured URI.

## Limitation that matters

The inspected default image version is latest, so an unpinned initializer can change the loading environment across deployments.

## Practical check for a trading system

Pin image digest and artifact hash in model and experiment provenance.

## Why this score

2/5. A concrete reproducibility trap rather than a dependency recommendation.

## Source trail

[README](https://github.com/SeldonIO/seldon-core/blob/6c363b18d03a8701fed66464cfffc439477dcce4/README.md#L1); [operator/controllers/model_initializer_injector.go](https://github.com/SeldonIO/seldon-core/blob/6c363b18d03a8701fed66464cfffc439477dcce4/operator/controllers/model_initializer_injector.go#L37); [Root license](https://github.com/SeldonIO/seldon-core/blob/6c363b18d03a8701fed66464cfffc439477dcce4/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
