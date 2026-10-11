# Orloj - Webhook deduplication must precede the side effect

**Decision question:** Can a duplicate webhook create work before the idempotency claim is won?

| Field | Review |
| --- | --- |
| Upstream | [OrlojHQ/orloj](https://github.com/OrlojHQ/orloj) |
| Primary area | Research & Reproducibility |
| Source commit | [e6b723b3df582cc262d6876715d5877b4b61226e](https://github.com/OrlojHQ/orloj/commit/e6b723b3df582cc262d6876715d5877b4b61226e) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its store has an atomic endpoint-and-event deduplication operation and explicit duplicate responses. The webhook handler creates the task before the atomic insert, so concurrent duplicates can both create work despite a duplicate response. |

## What this project does

An agent orchestration platform with tasks, webhooks, schedules and an event-driven API. This review focuses on the webhook delivery and deduplication path.

## Mechanism inspected

The store offers an atomic TryInsert keyed by endpoint and event ID, with a bounded expiry and an existing task returned on duplicates. The handler rejects missing event IDs and uses a fast pre-check; source tests cover the in-memory store returning the first task on a second insert.

## Limitation that matters

The handler calls createTaskFromWebhook before TryInsert. Concurrent deliveries can both create tasks after passing the pre-check; the losing request is reported as duplicate only after its task was already created. The source test for the store does not establish end-to-end exactly-once task creation. This is a source review, not a runtime or security test.

## Practical check for a trading system

Claim the event ID in durable storage before creating any order, job or other side effect. Test simultaneous duplicate deliveries at the handler boundary and reconcile uncertain outcomes by the same idempotency key.

## Why this score

2/5 because the code exposes an important idempotency ordering hazard applicable to trading triggers, but the inspected workflow is a generic agent webhook.

## Source trail

[README](https://github.com/OrlojHQ/orloj/blob/e6b723b3df582cc262d6876715d5877b4b61226e/README.md#L1); [Atomic store](https://github.com/OrlojHQ/orloj/blob/e6b723b3df582cc262d6876715d5877b4b61226e/store/webhook_dedupe_store.go#L78); [Webhook handler](https://github.com/OrlojHQ/orloj/blob/e6b723b3df582cc262d6876715d5877b4b61226e/api/task_webhook_api.go#L219); [Store tests](https://github.com/OrlojHQ/orloj/blob/e6b723b3df582cc262d6876715d5877b4b61226e/store/webhook_dedupe_test.go#L50); [License](https://github.com/OrlojHQ/orloj/blob/e6b723b3df582cc262d6876715d5877b4b61226e/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
