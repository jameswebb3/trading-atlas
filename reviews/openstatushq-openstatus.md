# openstatus - Separate health-state evidence from notification delivery

**Decision question:** Can a multi-region health transition be explained and repaired after interruption?

| Field | Review |
| --- | --- |
| Upstream | [openstatusHQ/openstatus](https://github.com/openstatusHQ/openstatus) |
| Primary area | Operations & Observability |
| Source commit | [e36446dc7d6980c16959f07d683f6261bc9c37d0](https://github.com/openstatusHQ/openstatus/commit/e36446dc7d6980c16959f07d683f6261bc9c37d0) |
| Reviewed | 2026-10-10 |
| Declared license | AGPL-3.0 |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Records region quorum, global status transition and notification outbox evidence under guarded database updates. The region write and aggregate transition are separate transactions; interrupted evaluations require the explicit repair path. |

## What this project does

An uptime monitoring and incident-response platform with configurable monitors and multiple checking regions. The inspected path handles the regional-to-global status transition.

## Mechanism inspected

A SQL quorum guard counts configured regions reporting the target status and requires at least half. The transition path journals old and new status with quorum counts, writes an idempotent notification outbox, and changes monitor status through a guarded update. Source tests exercise quorum and transition behavior.

## Limitation that matters

Regional status is written in a separate transaction from global transition evaluation. A crash between them leaves a stale global status, and replaying the same check can take the unchanged fast path; the source explicitly provides evaluateTransition as a repair entry point. Operational repair must actually be scheduled and observed. This is a source review, not a runtime or security test.

## Practical check for a trading system

For redundant market-feed health, keep source-level observations, aggregate decision evidence and alert-delivery state separate. Add a drift sweep that recomputes aggregate health after a crash and verify that the outbox does not resend a settled alert.

## Why this score

3/5 because the source and tests show a transferable multi-source health and repair pattern, but trading-feed semantics and loss thresholds must be defined separately.

## Source trail

[README](https://github.com/openstatusHQ/openstatus/blob/e36446dc7d6980c16959f07d683f6261bc9c37d0/README.md#L27); [Quorum guard](https://github.com/openstatusHQ/openstatus/blob/e36446dc7d6980c16959f07d683f6261bc9c37d0/apps/workflows/src/checker/quorum.ts#L11); [Transition journal and outbox](https://github.com/openstatusHQ/openstatus/blob/e36446dc7d6980c16959f07d683f6261bc9c37d0/apps/workflows/src/checker/transition.ts#L92); [Repair boundary](https://github.com/openstatusHQ/openstatus/blob/e36446dc7d6980c16959f07d683f6261bc9c37d0/apps/workflows/src/checker/transition.ts#L209); [Transition tests](https://github.com/openstatusHQ/openstatus/blob/e36446dc7d6980c16959f07d683f6261bc9c37d0/apps/workflows/src/checker/transition.test.ts#L86); [License](https://github.com/openstatusHQ/openstatus/blob/e36446dc7d6980c16959f07d683f6261bc9c37d0/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
