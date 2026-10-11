# Robusta - When a playbook action fails, is the whole run visibly incomplete?

**Decision question:** When a playbook action fails, is the whole run visibly incomplete?

| Field | Review |
| --- | --- |
| Upstream | [robusta-dev/robusta](https://github.com/robusta-dev/robusta) |
| Primary area | Operations & Observability |
| Source commit | [db2c4f0b10e0d8edaac0deaf81cbb708c5bf504b](https://github.com/robusta-dev/robusta/commit/db2c4f0b10e0d8edaac0deaf81cbb708c5bf504b) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The action handler counts missing actions, unsupported event types and parameter errors with action labels before continuing. The loop can complete some actions while others fail, so a run-level success needs a separate completeness check. |

## What this project does

An event-driven automation framework for operations playbooks.

## Mechanism inspected

The action handler counts missing actions, unsupported event types and parameter errors with action labels before continuing.

## Limitation that matters

The loop can complete some actions while others fail, so a run-level success needs a separate completeness check.

## Practical check for a trading system

Emit per-action outcomes and an explicit partial-run status in automated research or operations workflows.

## Why this score

2/5. Its labelled failures help diagnosis, but continuation alone is insufficient proof of a complete response.

## Source trail

[README](https://github.com/robusta-dev/robusta/blob/db2c4f0b10e0d8edaac0deaf81cbb708c5bf504b/README.md#L1); [src/robusta/core/playbooks/playbooks_event_handler_impl.py](https://github.com/robusta-dev/robusta/blob/db2c4f0b10e0d8edaac0deaf81cbb708c5bf504b/src/robusta/core/playbooks/playbooks_event_handler_impl.py#L205); [src/robusta/core/playbooks/playbooks_event_handler_impl.py](https://github.com/robusta-dev/robusta/blob/db2c4f0b10e0d8edaac0deaf81cbb708c5bf504b/src/robusta/core/playbooks/playbooks_event_handler_impl.py#L242).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
