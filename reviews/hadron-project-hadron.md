# hadron - Advance a durable stream only after ACK

**Decision question:** What state should a subscriber retain when processing a delivered batch fails?

| Field | Review |
| --- | --- |
| Upstream | [hadron-project/hadron](https://github.com/hadron-project/hadron) |
| Primary area | Market Data & Ingestion |
| Source commit | [b36aaa37b20b5f8569417fae913687622b74b262](https://github.com/hadron-project/hadron/commit/b36aaa37b20b5f8569417fae913687622b74b262) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/hadron-project/hadron/blob/b36aaa37b20b5f8569417fae913687622b74b262/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The subscriber caches an outgoing batch, leaves it ready for redelivery on NACK or malformed response, and advances the group offset on ACK; durable groups write the new offset to storage. This is at-least-once delivery plumbing. It cannot make a downstream trading side effect and offset update atomic, so the consumer still needs idempotency and gap checks. |

## What this project does

Hadron provides append-only streams and consumer groups with per-group delivery offsets. [README](https://github.com/hadron-project/hadron/blob/b36aaa37b20b5f8569417fae913687622b74b262/README.md).

## Mechanism inspected

The subscriber caches an outgoing batch, leaves it ready for redelivery on NACK or malformed response, and advances the group offset on ACK; durable groups write the new offset to storage. [Implementation](https://github.com/hadron-project/hadron/blob/b36aaa37b20b5f8569417fae913687622b74b262/hadron-stream/src/stream/subscriber.rs#L292-L337). [Related path](https://github.com/hadron-project/hadron/blob/b36aaa37b20b5f8569417fae913687622b74b262/hadron-stream/src/stream/subscriber.rs#L502-L518).

## Limitation that matters

This is at-least-once delivery plumbing. It cannot make a downstream trading side effect and offset update atomic, so the consumer still needs idempotency and gap checks. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

For collector replay, track delivered, acknowledged and durable offsets separately and reconcile an interrupted batch before declaring its partition complete.

## Why this score

The subscriber caches an outgoing batch, leaves it ready for redelivery on NACK or malformed response, and advances the group offset on ACK; durable groups write the new offset to storage. This is at-least-once delivery plumbing. It cannot make a downstream trading side effect and offset update atomic, so the consumer still needs idempotency and gap checks.

## Source trail

[README](https://github.com/hadron-project/hadron/blob/b36aaa37b20b5f8569417fae913687622b74b262/README.md) - [Implementation](https://github.com/hadron-project/hadron/blob/b36aaa37b20b5f8569417fae913687622b74b262/hadron-stream/src/stream/subscriber.rs#L292-L337) - [Related path](https://github.com/hadron-project/hadron/blob/b36aaa37b20b5f8569417fae913687622b74b262/hadron-stream/src/stream/subscriber.rs#L502-L518) - [License](https://github.com/hadron-project/hadron/blob/b36aaa37b20b5f8569417fae913687622b74b262/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
