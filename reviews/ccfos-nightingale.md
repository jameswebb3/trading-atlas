# Nightingale - Can configuration normalization hide a change in alert meaning?

**Decision question:** Can configuration normalization hide a change in alert meaning?

| Field | Review |
| --- | --- |
| Upstream | [ccfos/nightingale](https://github.com/ccfos/nightingale) |
| Primary area | Operations & Observability |
| Source commit | [8c9e2a9c097d56ef27bca1c7cbff8c7f2b7a1183](https://github.com/ccfos/nightingale/commit/8c9e2a9c097d56ef27bca1c7cbff8c7f2b7a1183) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | AlertRule config normalization recursively converts selected null fields into empty arrays before downstream use. The conversion can erase a meaningful distinction between unset and explicitly empty alert targets. |

## What this project does

An open-source alerting platform with serialized alert-rule configuration.

## Mechanism inspected

AlertRule config normalization recursively converts selected null fields into empty arrays before downstream use.

## Limitation that matters

The conversion can erase a meaningful distinction between unset and explicitly empty alert targets.

## Practical check for a trading system

Preserve the original rule payload and record each normalization when validating alert coverage.

## Why this score

2/5. The defensive normalization is concrete, but it does not prove alert coverage after a semantic change.

## Source trail

[README](https://github.com/ccfos/nightingale/blob/8c9e2a9c097d56ef27bca1c7cbff8c7f2b7a1183/README.md#L1); [models/alert_rule.go](https://github.com/ccfos/nightingale/blob/8c9e2a9c097d56ef27bca1c7cbff8c7f2b7a1183/models/alert_rule.go#L177); [models/alert_rule.go](https://github.com/ccfos/nightingale/blob/8c9e2a9c097d56ef27bca1c7cbff8c7f2b7a1183/models/alert_rule.go#L200).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
