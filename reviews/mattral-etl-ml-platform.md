# ETL ML Platform - Can scaling before a split inflate a model evaluation?

**Decision question:** Can scaling before a split inflate a model evaluation?

| Field | Review |
| --- | --- |
| Upstream | [Mattral/etl-ml-platform](https://github.com/Mattral/etl-ml-platform) |
| Primary area | Research & Reproducibility |
| Source commit | [b29f9c2a55933995485b8e92051ddac34f930342](https://github.com/Mattral/etl-ml-platform/commit/b29f9c2a55933995485b8e92051ddac34f930342) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The training route fits StandardScaler on all feature rows and only then splits train and test arrays. Test-set feature distribution influences the scaler, and the split is random rather than chronological. |

## What this project does

A small ETL and model-training web application.

## Mechanism inspected

The training route fits StandardScaler on all feature rows and only then splits train and test arrays.

## Limitation that matters

Test-set feature distribution influences the scaler, and the split is random rather than chronological.

## Practical check for a trading system

Fit preprocessing inside each training fold and preserve time order for market studies.

## Why this score

2/5. A direct leakage anti-pattern, not a model platform to integrate.

## Source trail

[README](https://github.com/Mattral/etl-ml-platform/blob/b29f9c2a55933995485b8e92051ddac34f930342/README.md#L1); [backend/server.py](https://github.com/Mattral/etl-ml-platform/blob/b29f9c2a55933995485b8e92051ddac34f930342/backend/server.py#L520); [backend/server.py](https://github.com/Mattral/etl-ml-platform/blob/b29f9c2a55933995485b8e92051ddac34f930342/backend/server.py#L534).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
