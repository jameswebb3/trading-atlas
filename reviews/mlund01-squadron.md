# Squadron - Acknowledged buffering is not persisted event evidence

**Decision question:** Can an agent event disappear after StoreEvent reports success?

| Field | Review |
| --- | --- |
| Upstream | [mlund01/squadron](https://github.com/mlund01/squadron) |
| Primary area | Research & Reproducibility |
| Source commit | [151734bc23150fe4c901811c8c62889d12a81ad5](https://github.com/mlund01/squadron/commit/151734bc23150fe4c901811c8c62889d12a81ad5) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Batches agent events by time or size and flushes on reads or shutdown to reduce underlying store writes. It acknowledges StoreEvent before persistence and discards a failed flush batch after logging, so the stream can have silent gaps. |

## What this project does

A multi-agent workflow system with an event-store wrapper that batches mission events before writing to the underlying store.

## Mechanism inspected

StoreEvent appends to an in-memory buffer and returns nil immediately. A timer or size threshold triggers a background flush, while reads and Close also request a flush. Source tests check time, size, read and close paths.

## Limitation that matters

flush clears the buffer before calling the underlying StoreEvents. If that write fails, it only logs the error and does not restore the batch or surface the failure to the original caller. A crash before flush also loses buffered events. A successful StoreEvent return is therefore not a durability acknowledgement. This is a source review, not a runtime or security test.

## Practical check for a trading system

For agent research evidence, label buffered events as pending until durable storage confirms them. For orders and fills, never use this acknowledgement as the ledger commit; enforce a write-ahead or transactional receipt before the side effect.

## Why this score

2/5 because the source and tests expose a precise event-durability trap relevant to research provenance, but the mechanism is a generic agent store.

## Source trail

[README](https://github.com/mlund01/squadron/blob/151734bc23150fe4c901811c8c62889d12a81ad5/README.md#L1); [Buffer and acknowledgement](https://github.com/mlund01/squadron/blob/151734bc23150fe4c901811c8c62889d12a81ad5/store/batching_event_store.go#L50); [Flush failure](https://github.com/mlund01/squadron/blob/151734bc23150fe4c901811c8c62889d12a81ad5/store/batching_event_store.go#L126); [Batch tests](https://github.com/mlund01/squadron/blob/151734bc23150fe4c901811c8c62889d12a81ad5/store/batching_event_store_test.go#L60); [License](https://github.com/mlund01/squadron/blob/151734bc23150fe4c901811c8c62889d12a81ad5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
