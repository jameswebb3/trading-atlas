# Boomerang Flow - Can an expiring distributed lock still protect one writer?

**Decision question:** Can an expiring distributed lock still protect one writer?

| Field | Review |
| --- | --- |
| Upstream | [boomerang-io/flow](https://github.com/boomerang-io/flow) |
| Primary area | Research & Reproducibility |
| Source commit | [5efada949c3ce4fa94caf55d60d426735226ca74](https://github.com/boomerang-io/flow/commit/5efada949c3ce4fa94caf55d60d426735226ca74) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The manager obtains a token-bearing lock and later releases it for a workflow run. The inspected path does not show a monotonic fencing token passed to downstream writes; an expired owner may still act. |

## What this project does

A workflow service with a MongoDB lock manager.

## Mechanism inspected

The manager obtains a token-bearing lock and later releases it for a workflow run.

## Limitation that matters

The inspected path does not show a monotonic fencing token passed to downstream writes; an expired owner may still act.

## Practical check for a trading system

Use fencing or compare-and-swap at the protected write, not TTL alone.

## Why this score

2/5. A concrete concurrency caution for experiment and collector jobs.

## Source trail

[README](https://github.com/boomerang-io/flow/blob/5efada949c3ce4fa94caf55d60d426735226ca74/README.md#L1); [service-engine/src/main/java/io/boomerang/engine/LockManager.java](https://github.com/boomerang-io/flow/blob/5efada949c3ce4fa94caf55d60d426735226ca74/service-engine/src/main/java/io/boomerang/engine/LockManager.java#L137); [Root license](https://github.com/boomerang-io/flow/blob/5efada949c3ce4fa94caf55d60d426735226ca74/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
