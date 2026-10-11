# Kiali — Preserve Not Ready and NA apart from failure

**Decision question:** How should component health be summarized without flattening unknown states?

| Field | Review |
| --- | --- |
| Upstream | [kiali/kiali](https://github.com/kiali/kiali) |
| Primary area | Operations & Observability |
| Source commit | [af2b3ef943f4dc14c429f5984c98826708717f23](https://github.com/kiali/kiali/commit/af2b3ef943f4dc14c429f5984c98826708717f23) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/kiali/kiali/blob/af2b3ef943f4dc14c429f5984c98826708717f23/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its health priority orders Failure, Degraded, Not Ready, Healthy, and NA separately. An NA value is given lowest priority; a naive aggregate could hide missing evaluation behind healthy components. |

## What this project does

A service-mesh observability project with explicit health states. [Project README](https://github.com/kiali/kiali/blob/af2b3ef943f4dc14c429f5984c98826708717f23/README.adoc#L1).

## Mechanism inspected

Its health priority orders Failure, Degraded, Not Ready, Healthy, and NA separately. [Implementation](https://github.com/kiali/kiali/blob/af2b3ef943f4dc14c429f5984c98826708717f23/models/health_status.go#L14).

## Limitation that matters

An NA value is given lowest priority; a naive aggregate could hide missing evaluation behind healthy components. This is a source review, not a runtime or security test.

## Practical check for a trading system

Keep Not Ready and Not Evaluated visible when gating a market-data feed, even if other components are healthy.

## Why this score

A useful status vocabulary, with aggregation policy needing domain-specific adjustment.

## Source trail

[README](https://github.com/kiali/kiali/blob/af2b3ef943f4dc14c429f5984c98826708717f23/README.adoc#L1); [Implementation](https://github.com/kiali/kiali/blob/af2b3ef943f4dc14c429f5984c98826708717f23/models/health_status.go#L14) - [License](https://github.com/kiali/kiali/blob/af2b3ef943f4dc14c429f5984c98826708717f23/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
