# SqlGraph - Carry status and provenance with every lineage metric

**Decision question:** Can an analysis distinguish an unavailable measure from a true zero?

| Field | Review |
| --- | --- |
| Upstream | [Liyurun/SqlGraph](https://github.com/Liyurun/SqlGraph) |
| Primary area | Data Quality & Lineage |
| Source commit | [ea03f730f4ea77532510c3df8c757852c54f1eb2](https://github.com/Liyurun/SqlGraph/commit/ea03f730f4ea77532510c3df8c757852c54f1eb2) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/Liyurun/SqlGraph/blob/ea03f730f4ea77532510c3df8c757852c54f1eb2/LICENSE)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | MetricResult requires a reason whenever status is not success and keeps algorithm, version and parameters; AnalysisManifest requires graph and configuration fingerprints and lists completed, degraded, skipped and failed metrics. Those fingerprints describe the graph and configuration. They do not establish event time, original source availability or the correctness of a parsed dynamic query. |

## What this project does

SqlGraph builds a graph of SQL assets, column dependencies and reusable transformations. [README](https://github.com/Liyurun/SqlGraph/blob/ea03f730f4ea77532510c3df8c757852c54f1eb2/README.md).

## Mechanism inspected

MetricResult requires a reason whenever status is not success and keeps algorithm, version and parameters; AnalysisManifest requires graph and configuration fingerprints and lists completed, degraded, skipped and failed metrics. [Implementation](https://github.com/Liyurun/SqlGraph/blob/ea03f730f4ea77532510c3df8c757852c54f1eb2/sqlgraph/analyze/contracts.py#L18-L57). [Related path](https://github.com/Liyurun/SqlGraph/blob/ea03f730f4ea77532510c3df8c757852c54f1eb2/sqlgraph/analyze/contracts.py#L60-L105).

## Limitation that matters

Those fingerprints describe the graph and configuration. They do not establish event time, original source availability or the correctness of a parsed dynamic query. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

For each lineage or coverage metric, record value, status, reason and input fingerprint; separately prove source time and runtime coverage.

## Why this score

A concrete answer envelope and manifest are transferable to data-driven decisions; the reviewed graph remains structural evidence only.

## Source trail

[README](https://github.com/Liyurun/SqlGraph/blob/ea03f730f4ea77532510c3df8c757852c54f1eb2/README.md) - [Implementation](https://github.com/Liyurun/SqlGraph/blob/ea03f730f4ea77532510c3df8c757852c54f1eb2/sqlgraph/analyze/contracts.py#L18-L57) - [Related path](https://github.com/Liyurun/SqlGraph/blob/ea03f730f4ea77532510c3df8c757852c54f1eb2/sqlgraph/analyze/contracts.py#L60-L105) - [License](https://github.com/Liyurun/SqlGraph/blob/ea03f730f4ea77532510c3df8c757852c54f1eb2/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
