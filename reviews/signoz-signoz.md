# SigNoz - Can alert configuration drift be detected without masking partial sync failure?

**Decision question:** Can alert configuration drift be detected without masking partial sync failure?

| Field | Review |
| --- | --- |
| Upstream | [SigNoz/signoz](https://github.com/SigNoz/signoz) |
| Primary area | Operations & Observability |
| Source commit | [6b137947280595ecabea354b54076356b78d8433](https://github.com/SigNoz/signoz/commit/6b137947280595ecabea354b54076356b78d8433) |
| Reviewed | 2026-10-11 |
| Declared license | MIT Expat for inspected path; enterprise directories separately licensed |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | SyncServers compares a running server hash with the stored configuration hash and skips unchanged organizations. Errors for individual organizations are logged and the loop continues, then returns nil; a caller cannot infer that every organization synced. |

## What this project does

An open-source observability platform with per-organization alertmanager instances.

## Mechanism inspected

SyncServers compares a running server hash with the stored configuration hash and skips unchanged organizations.

## Limitation that matters

Errors for individual organizations are logged and the loop continues, then returns nil; a caller cannot infer that every organization synced.

## Practical check for a trading system

Report per-source alert configuration hashes and a completeness status, not just a successful overall run.

## Why this score

2/5. The hash-based sync is useful while the partial-failure return is a caution.

## Source trail

[README](https://github.com/SigNoz/signoz/blob/6b137947280595ecabea354b54076356b78d8433/README.md#L1); [pkg/alertmanager/service.go](https://github.com/SigNoz/signoz/blob/6b137947280595ecabea354b54076356b78d8433/pkg/alertmanager/service.go#L70); [pkg/alertmanager/service.go](https://github.com/SigNoz/signoz/blob/6b137947280595ecabea354b54076356b78d8433/pkg/alertmanager/service.go#L96).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
