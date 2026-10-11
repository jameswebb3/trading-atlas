# Katib — Finished jobs can lack observations

**Decision question:** Is a successful training job enough to complete a trial?

| Field | Review |
| --- | --- |
| Upstream | [Katib](https://github.com/kubeflow/katib) |
| Primary area | Research & Reproducibility |
| Source commit | [dae0fc5c2f7af60ca15e96e1066ef0f49d709e33](https://github.com/kubeflow/katib/commit/dae0fc5c2f7af60ca15e96e1066ef0f49d709e33) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/kubeflow/katib/blob/dae0fc5c2f7af60ca15e96e1066ef0f49d709e33/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | For successful jobs using a non-push collector, the controller requeues when the trial observation is nil rather than marking the trial complete immediately. The condition has an explicit PushCollector exception, and non-nil observations are not proof that required metrics are valid, finite or comparable. |

## Project overview

Kubernetes-native hyperparameter tuning, early stopping and experiment management. [Documentation](https://github.com/kubeflow/katib/blob/dae0fc5c2f7af60ca15e96e1066ef0f49d709e33/README.md).

## Mechanism worth inspecting

For successful jobs using a non-push collector, the controller requeues when the trial observation is nil rather than marking the trial complete immediately. [Source](https://github.com/kubeflow/katib/blob/dae0fc5c2f7af60ca15e96e1066ef0f49d709e33/pkg/controller.v1beta1/trial/trial_controller.go#L250-L272).

## Important limit

The condition has an explicit PushCollector exception, and non-nil observations are not proof that required metrics are valid, finite or comparable. Hyperparameter search does not provide a statistical research gate. [Evidence 1](https://github.com/kubeflow/katib/blob/dae0fc5c2f7af60ca15e96e1066ef0f49d709e33/pkg/controller.v1beta1/trial/trial_controller.go#L250-L272).

## Questions to take into your own design

- Are process success, observation presence and metric validity separate states?
- Does the push-collector path meet the same evidence requirement?

## Why this score for a trading system

A precise workflow/evidence separation relevant to research admission; the tuning infrastructure is outside the useful mechanism.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
