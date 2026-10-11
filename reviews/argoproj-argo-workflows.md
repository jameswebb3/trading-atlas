# Argo Workflows — A cache hit is not a new experiment

**Decision question:** Does a memoized step count as a fresh observation?

| Field | Review |
| --- | --- |
| Upstream | [Argo Workflows](https://github.com/argoproj/argo-workflows) |
| Primary area | Research & Reproducibility |
| Source commit | [d0cfa58f52793353ace714c9b792d3dc903093ee](https://github.com/argoproj/argo-workflows/commit/d0cfa58f52793353ace714c9b792d3dc903093ee) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/argoproj/argo-workflows/blob/d0cfa58f52793353ace714c9b792d3dc903093ee/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The controller loads a memoization entry by key and can initialize a node directly from a valid cache hit. Memoization can reuse results without re-execution and cannot itself validate external side effects or statistical independence. |

## Project overview

Kubernetes workflow engine for container-based tasks and DAGs. [Documentation](https://github.com/argoproj/argo-workflows/blob/d0cfa58f52793353ace714c9b792d3dc903093ee/README.md).

## Mechanism worth inspecting

The controller loads a memoization entry by key and can initialize a node directly from a valid cache hit. Documentation allows a maximum age and explains that pure computation is an assumption, not an enforced property. [Source](https://github.com/argoproj/argo-workflows/blob/d0cfa58f52793353ace714c9b792d3dc903093ee/workflow/controller/operator.go#L2397-L2450).

## Important limit

Memoization can reuse results without re-execution and cannot itself validate external side effects or statistical independence. A user-supplied key may omit relevant data identity. [Evidence 1](https://github.com/argoproj/argo-workflows/blob/d0cfa58f52793353ace714c9b792d3dc903093ee/workflow/controller/operator.go#L2397-L2450). [Evidence 2](https://github.com/argoproj/argo-workflows/blob/d0cfa58f52793353ace714c9b792d3dc903093ee/docs/memoization.md#L7-L27).

## Questions to take into your own design

- Does the receipt point to the original computation behind a cache hit?
- Do reused artifacts avoid increasing the count of independent trials?

## Why this score for a trading system

A practical experiment-bookkeeping mechanism, not a reason to introduce a Kubernetes control plane.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
