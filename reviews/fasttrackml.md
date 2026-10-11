# A metric-history export can stop before the history does

**Decision question:** Did a bulk metric response include every observation used to compare trials?

| Field | Review |
| --- | --- |
| Upstream | [FastTrackML](https://github.com/G-Research/fasttrackml) |
| Primary area | Research & Reproducibility |
| Source commit | [4d6f286e70f5f636c7e3b8c47a6d54c010a9d256](https://github.com/G-Research/fasttrackml/commit/4d6f286e70f5f636c7e3b8c47a6d54c010a9d256) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/G-Research/fasttrackml/blob/4d6f286e70f5f636c7e3b8c47a6d54c010a9d256/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its bulk metric-history query applies a default 25,000-row limit, and the API caps bulk requests at 200 run IDs. Useful reminders for experiment-ledger exports: a successful response is not a completeness certificate. The README points ongoing development toward a successor backend. |

## Mechanism worth inspecting

The [overview](https://github.com/G-Research/fasttrackml/blob/4d6f286e70f5f636c7e3b8c47a6d54c010a9d256/README.md#L5-L16) describes MLflow-compatible tracking and the successor project. The [quickstart](https://github.com/G-Research/fasttrackml/blob/4d6f286e70f5f636c7e3b8c47a6d54c010a9d256/docs/quickstart.md#L34-L42) identifies the local server. The [repository query](https://github.com/G-Research/fasttrackml/blob/4d6f286e70f5f636c7e3b8c47a6d54c010a9d256/pkg/api/mlflow/dao/repositories/metric.go#L304-L336) applies MetricHistoryBulkDefaultLimit when no limit is supplied; the [API validator](https://github.com/G-Research/fasttrackml/blob/4d6f286e70f5f636c7e3b8c47a6d54c010a9d256/pkg/api/mlflow/services/metric/validators.go#L34-L49) rejects more than 200 runs.

## Important limit

This review covers bulk retrieval, not proof that metrics are dropped during logging. Client batching, explicit limits, and completeness checks remain caller responsibilities. Faster tracking does not supply a complete trial registry or a multiple-testing denominator.

## Questions to take into your own design

- Can every requested trial and metric be accounted for after export?
- Will a response at its configured limit be treated as possibly truncated?

## Why this score for a trading system

2/5: The retrieval limit exposes a concrete experiment-export risk, but offers a narrow reference rather than a complete trading research ledger.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
