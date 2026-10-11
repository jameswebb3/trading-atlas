# FinSight AI — A lease fallback can create two leaders

**Decision question:** Should a workflow continue locally when its shared lease store fails?

| Field | Review |
| --- | --- |
| Upstream | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) |
| Primary area | Research & Reproducibility |
| Source commit | [5cdf91aa756e1c08239103af4e8d9f61b7541529](https://github.com/juanjuandog/FinSight-AI/commit/5cdf91aa756e1c08239103af4e8d9f61b7541529) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/juanjuandog/FinSight-AI/blob/5cdf91aa756e1c08239103af4e8d9f61b7541529/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The lease service uses a shared Redis script and fencing token; when Redis fails, local fallback is allowed only by explicit configuration. If local fallback is enabled across multiple workers, each may believe it owns the same workflow; a lease cannot make an exchange side effect idempotent. |

## What this project does

A financial-analysis workflow system with Redis-backed leases. [Project README](https://github.com/juanjuandog/FinSight-AI/blob/5cdf91aa756e1c08239103af4e8d9f61b7541529/README.md#L1).

## Mechanism inspected

The lease service uses a shared Redis script and fencing token; when Redis fails, local fallback is allowed only by explicit configuration. [Implementation](https://github.com/juanjuandog/FinSight-AI/blob/5cdf91aa756e1c08239103af4e8d9f61b7541529/backend/src/main/java/com/finsight/workflow/RedisBackedWorkflowLeaseService.java#L75).

## Limitation that matters

If local fallback is enabled across multiple workers, each may believe it owns the same workflow; a lease cannot make an exchange side effect idempotent. This is a source review, not a runtime or security test.

## Practical check for a trading system

Disable local fallback for singleton trading jobs and fence external effects with durable intent identity.

## Why this score

A concrete split-brain control, but external order reconciliation remains necessary.

## Source trail

[README](https://github.com/juanjuandog/FinSight-AI/blob/5cdf91aa756e1c08239103af4e8d9f61b7541529/README.md#L1); [Implementation](https://github.com/juanjuandog/FinSight-AI/blob/5cdf91aa756e1c08239103af4e8d9f61b7541529/backend/src/main/java/com/finsight/workflow/RedisBackedWorkflowLeaseService.java#L75) - [License](https://github.com/juanjuandog/FinSight-AI/blob/5cdf91aa756e1c08239103af4e8d9f61b7541529/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
