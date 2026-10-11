# zipkin — Collector acknowledgement precedes durable storage

**Decision question:** What does a successful ingest callback actually acknowledge?

| Field | Review |
| --- | --- |
| Upstream | [openzipkin/zipkin](https://github.com/openzipkin/zipkin) |
| Primary area | Operations & Observability |
| Source commit | [878ce2a1fad54ca941d17fdcf2e1d924b148eb1f](https://github.com/openzipkin/zipkin/commit/878ce2a1fad54ca941d17fdcf2e1d924b148eb1f) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/openzipkin/zipkin/blob/878ce2a1fad54ca941d17fdcf2e1d924b148eb1f/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Collector.accept queues sampled spans for asynchronous storage and calls the caller's success callback immediately after enqueue. The callback explicitly does not propagate storage failure; an ingest success cannot prove durable evidence. |

## What this project does

Distributed tracing server with collection and storage stages. [README](https://github.com/openzipkin/zipkin/blob/878ce2a1fad54ca941d17fdcf2e1d924b148eb1f/README.md).

## Mechanism inspected

Collector.accept queues sampled spans for asynchronous storage and calls the caller's success callback immediately after enqueue. [Implementation](https://github.com/openzipkin/zipkin/blob/878ce2a1fad54ca941d17fdcf2e1d924b148eb1f/zipkin-collector/core/src/main/java/zipkin2/collector/Collector.java#L24-L30). [Related implementation](https://github.com/openzipkin/zipkin/blob/878ce2a1fad54ca941d17fdcf2e1d924b148eb1f/zipkin-collector/core/src/test/java/zipkin2/collector/CollectorTest.java#L117-L130).

## Limitation that matters

The callback explicitly does not propagate storage failure; an ingest success cannot prove durable evidence. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Label ACK stages separately for feed capture, fill events and research artifacts; reconcile enqueue IDs with persisted IDs.

## Why this score

Collector.accept queues sampled spans for asynchronous storage and calls the caller's success callback immediately after enqueue. The callback explicitly does not propagate storage failure; an ingest success cannot prove durable evidence.

## Source trail

[README](https://github.com/openzipkin/zipkin/blob/878ce2a1fad54ca941d17fdcf2e1d924b148eb1f/README.md) · [Implementation](https://github.com/openzipkin/zipkin/blob/878ce2a1fad54ca941d17fdcf2e1d924b148eb1f/zipkin-collector/core/src/main/java/zipkin2/collector/Collector.java#L24-L30) · [Related implementation](https://github.com/openzipkin/zipkin/blob/878ce2a1fad54ca941d17fdcf2e1d924b148eb1f/zipkin-collector/core/src/test/java/zipkin2/collector/CollectorTest.java#L117-L130) · [License](https://github.com/openzipkin/zipkin/blob/878ce2a1fad54ca941d17fdcf2e1d924b148eb1f/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
