# SwanLab — Metric definitions freeze when first logged

**Decision question:** Can a late chart definition change an already logged metric?

| Field | Review |
| --- | --- |
| Upstream | [SwanLab](https://github.com/SwanHubX/SwanLab) |
| Primary area | Research & Reproducibility |
| Source commit | [e2b749193b5b0f697029a576baf8d0ab2fafdd98](https://github.com/SwanHubX/SwanLab/commit/e2b749193b5b0f697029a576baf8d0ab2fafdd98) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/SwanHubX/SwanLab/blob/e2b749193b5b0f697029a576baf8d0ab2fafdd98/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation, and relevant test code read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The resolver chooses an exact rule, longest-prefix rule or automatic default at first materialization and caches the resulting definition. Late redefinition is not retroactive in this path. |

## Project overview

Experiment tracking and training-analysis toolkit with metric definitions and visualizations. [Documentation](https://github.com/SwanHubX/SwanLab/blob/e2b749193b5b0f697029a576baf8d0ab2fafdd98/README_EN.md).

## Mechanism worth inspecting

The resolver chooses an exact rule, longest-prefix rule or automatic default at first materialization and caches the resulting definition. Tests verify that later rules do not change existing concrete metrics. [Source](https://github.com/SwanHubX/SwanLab/blob/e2b749193b5b0f697029a576baf8d0ab2fafdd98/swanlab/sdk/internal/run/components/consumer/resolver/__init__.py#L135-L183).

## Important limit

Late redefinition is not retroactive in this path. A chart can therefore retain earlier axis semantics even after configuration changes; metric display identity is not proof of reproducible data or scientific validity. [Evidence 1](https://github.com/SwanHubX/SwanLab/blob/e2b749193b5b0f697029a576baf8d0ab2fafdd98/swanlab/sdk/internal/run/components/consumer/resolver/__init__.py#L135-L183). [Evidence 2](https://github.com/SwanHubX/SwanLab/blob/e2b749193b5b0f697029a576baf8d0ab2fafdd98/tests/unit/sdk/internal/run/components/consumer/resolver/test_resolver.py#L61-L84).

## Questions to take into your own design

- Are metric units and x-axis definitions fixed before the first log?
- Does a changed definition create a new metric identity or an explicit revision?

## Why this score for a trading system

A useful immutable-definition mechanism and focused tests; another tracking UI adds less than recording the contract in an existing ledger.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. Relevant tests were read, not executed.
