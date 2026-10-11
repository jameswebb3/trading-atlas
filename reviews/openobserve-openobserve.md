# OpenObserve - Does persisting an incident event prove its downstream workflow was triggered?

**Decision question:** Does persisting an incident event prove its downstream workflow was triggered?

| Field | Review |
| --- | --- |
| Upstream | [openobserve/openobserve](https://github.com/openobserve/openobserve) |
| Primary area | Operations Observability |
| Source commit | [f87d7402e295fbf59ed4503bbec27487a9a27ad0](https://github.com/openobserve/openobserve/commit/f87d7402e295fbf59ed4503bbec27487a9a27ad0) |
| Reviewed | 2026-10-10 |
| Declared license | AGPL-3.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Appends an incident event before attempting associated workflow triggers; trigger lookup, metadata and send failures are logged but return success. An event can be durably recorded while its downstream workflow never starts, so the two outcomes require separate status evidence. |

## What this project does

A self-hosted observability platform for logs, metrics, traces and incidents. The inspected function maps incident events to associated workflows.

## Mechanism inspected

append_event writes the incident event to storage, then calls send_incident_event_trigger. That helper looks up associated workflows, constructs event metadata and sends each trigger with a trace ID.

## Limitation that matters

Lookup and metadata failures log and return Ok(()). Individual trigger-send failures are also logged and the helper returns Ok(()). Thus append_event can return success for a stored event even though no workflow was started. The design may intentionally keep incident storage independent of notifications; consumers must not equate the outcomes. This is a source review, not a delivery test.

## Practical check for a trading system

Keep incident persistence, downstream action dispatch and confirmed delivery as distinct states. Reconcile failed or missing dispatches by incident and workflow ID before relying on an alert as an operational gate.

## Why this score

2/5 because the separation of persisted event and dispatched workflow is a useful caution, but the inspected platform is broad and its incident semantics need a trading-specific policy.

## Source trail

[README](https://github.com/openobserve/openobserve/blob/f87d7402e295fbf59ed4503bbec27487a9a27ad0/README.md#L1); [Incident event metadata](https://github.com/openobserve/openobserve/blob/f87d7402e295fbf59ed4503bbec27487a9a27ad0/src/core/src/incidents.rs#L25); [Trigger error handling](https://github.com/openobserve/openobserve/blob/f87d7402e295fbf59ed4503bbec27487a9a27ad0/src/core/src/incidents.rs#L181); [Event append sequence](https://github.com/openobserve/openobserve/blob/f87d7402e295fbf59ed4503bbec27487a9a27ad0/src/core/src/incidents.rs#L233); [License](https://github.com/openobserve/openobserve/blob/f87d7402e295fbf59ed4503bbec27487a9a27ad0/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
