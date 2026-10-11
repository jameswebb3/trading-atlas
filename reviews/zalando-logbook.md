# Logbook - How can logs exclude secrets without losing all incident context?

**Decision question:** How can logs exclude secrets without losing all incident context?

| Field | Review |
| --- | --- |
| Upstream | [zalando/logbook](https://github.com/zalando/logbook) |
| Primary area | Operations & Observability |
| Source commit | [f4f1e6372f449c193e5eb2a21478d07ef766c2a3](https://github.com/zalando/logbook/commit/f4f1e6372f449c193e5eb2a21478d07ef766c2a3) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The security strategy discards request and response bodies before logging. Dropping entire bodies protects secrets but can remove the fields needed to reconstruct an order incident. |

## What this project does

An HTTP request and response logging library with a security strategy.

## Mechanism inspected

The security strategy discards request and response bodies before logging.

## Limitation that matters

Dropping entire bodies protects secrets but can remove the fields needed to reconstruct an order incident.

## Practical check for a trading system

Redact sensitive fields while retaining safe request IDs, status and timing.

## Why this score

2/5. The privacy boundary is valuable, but wholesale body removal is too coarse for trade reconciliation.

## Source trail

[README](https://github.com/zalando/logbook/blob/f4f1e6372f449c193e5eb2a21478d07ef766c2a3/README.md#L1); [logbook-core/src/main/java/org/zalando/logbook/core/SecurityStrategy.java](https://github.com/zalando/logbook/blob/f4f1e6372f449c193e5eb2a21478d07ef766c2a3/logbook-core/src/main/java/org/zalando/logbook/core/SecurityStrategy.java#L15); [logbook-core/src/main/java/org/zalando/logbook/core/SecurityStrategy.java](https://github.com/zalando/logbook/blob/f4f1e6372f449c193e5eb2a21478d07ef766c2a3/logbook-core/src/main/java/org/zalando/logbook/core/SecurityStrategy.java#L30).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
