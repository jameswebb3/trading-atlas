# Coze Loop - Can an evaluation output preserve which field came from which source?

**Decision question:** Can an evaluation output preserve which field came from which source?

| Field | Review |
| --- | --- |
| Upstream | [coze-dev/coze-loop](https://github.com/coze-dev/coze-loop) |
| Primary area | Operations & Observability |
| Source commit | [a265e644cf7fcbcf9353edb360169a91aed19fc9](https://github.com/coze-dev/coze-loop/commit/a265e644cf7fcbcf9353edb360169a91aed19fc9) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It accepts prefixed and legacy result keys and recursively merges platform defaults with evaluator object fields. A conflicting evaluator value, including null, can override a default without retaining the origin of that value. |

## What this project does

An LLM evaluation platform with standard output conversion.

## Mechanism inspected

It accepts prefixed and legacy result keys and recursively merges platform defaults with evaluator object fields.

## Limitation that matters

A conflicting evaluator value, including null, can override a default without retaining the origin of that value.

## Practical check for a trading system

Persist the raw evaluator result and a field-level merge provenance for agent evaluations.

## Why this score

2/5. The merge path is clear and transferable; source attribution is still needed before trusting a score.

## Source trail

[README](https://github.com/coze-dev/coze-loop/blob/a265e644cf7fcbcf9353edb360169a91aed19fc9/README.md#L1); [backend/modules/evaluation/application/standard_eval_output.go](https://github.com/coze-dev/coze-loop/blob/a265e644cf7fcbcf9353edb360169a91aed19fc9/backend/modules/evaluation/application/standard_eval_output.go#L45); [backend/modules/evaluation/application/standard_eval_output.go](https://github.com/coze-dev/coze-loop/blob/a265e644cf7fcbcf9353edb360169a91aed19fc9/backend/modules/evaluation/application/standard_eval_output.go#L118).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
