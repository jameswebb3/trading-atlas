# BoundFlow: Will a safety rule still fire if its telemetry disappears?

**Decision question:** Will a safety rule still fire if its telemetry disappears?

| Field | Review |
| --- | --- |
| Upstream | [boundflow/boundflow](https://github.com/boundflow/boundflow) |
| Primary area | Agents & Decision Systems |
| Source commit | [92212dc7dbb11d593c3c8418754df48428b90845](https://github.com/boundflow/boundflow/commit/92212dc7dbb11d593c3c8418754df48428b90845) |
| Reviewed | 2026-10-11 |
| Declared license | [Apache-2.0](https://github.com/boundflow/boundflow/blob/92212dc7dbb11d593c3c8418754df48428b90845/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Lifecycle rules consume rolling or version metrics and return the winning action, matched rule and observed value. Pause outranks cooldown and set-version. MetricEmitted distinguishes absent scalar pointers or tool keys from values, but ResolvePolicy skips rules if the latest run omitted the metric. Public preview and pre-1.0 API; README says no external production operation yet. The code's skip-on-absence behavior could leave a safety rule inactive exactly when monitoring fails; that is an observed design tradeoff, not proof of a live failure. |

## What this project does

Separates run-time limits from post-run lifecycle rules and selects a winning pause, cooldown or version action. The policy engine skips a rule when its metric is absent in the last run, so missing safety telemetry needs its own stop condition.

## Mechanism inspected

Lifecycle rules consume rolling or version metrics and return the winning action, matched rule and observed value. Pause outranks cooldown and set-version. MetricEmitted distinguishes absent scalar pointers or tool keys from values, but ResolvePolicy skips rules if the latest run omitted the metric.

## Limitation that matters

Public preview and pre-1.0 API; README says no external production operation yet. The code's skip-on-absence behavior could leave a safety rule inactive exactly when monitoring fails; that is an observed design tradeoff, not proof of a live failure.

## Practical check for a trading system

Inject missing cost, failure and tool metrics into an agent-run lifecycle test. Define an explicit fail-closed policy for required telemetry, with a separate reason code and operator visibility.

## Why this score

2/5 transferable: the two-level safety policy and rule provenance are useful, but the large control plane is unnecessary here and its missing-metric semantics are unsafe to copy blindly.

## Source trail

[README.md](https://github.com/boundflow/boundflow/blob/92212dc7dbb11d593c3c8418754df48428b90845/README.md#L9); [docs/concepts.md](https://github.com/boundflow/boundflow/blob/92212dc7dbb11d593c3c8418754df48428b90845/docs/concepts.md#L10); [internal/lifecyclepolicy/engine.go](https://github.com/boundflow/boundflow/blob/92212dc7dbb11d593c3c8418754df48428b90845/internal/lifecyclepolicy/engine.go#L14); [internal/lifecyclepolicy/engine.go](https://github.com/boundflow/boundflow/blob/92212dc7dbb11d593c3c8418754df48428b90845/internal/lifecyclepolicy/engine.go#L33); [internal/lifecyclepolicy/engine.go](https://github.com/boundflow/boundflow/blob/92212dc7dbb11d593c3c8418754df48428b90845/internal/lifecyclepolicy/engine.go#L178)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
