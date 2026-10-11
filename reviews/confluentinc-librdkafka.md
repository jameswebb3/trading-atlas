# librdkafka — Should a timeout be represented as a definite failure or an uncertain outcome

**Decision question:** Should a timeout be represented as a definite failure or an uncertain outcome?

| Field | Review |
| --- | --- |
| Upstream | [librdkafka](https://github.com/confluentinc/librdkafka) |
| Primary area | Execution & Exchange Integration |
| Source commit | [644e97a67d9585c7ab63c249f043932e25239ddb](https://github.com/confluentinc/librdkafka/commit/644e97a67d9585c7ab63c249f043932e25239ddb) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-2-Clause; bundled components have separate notices](https://github.com/confluentinc/librdkafka/blob/644e97a67d9585c7ab63c249f043932e25239ddb/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Preserves the distinction between definite non-delivery and possible delivery after an acknowledgement timeout. A strong conceptual reference for uncertain order outcomes and reconciliation before retry. |

## Project overview

A C and C++ Kafka client with producer, consumer, idempotent-producer and transactional interfaces. [Project documentation](https://github.com/confluentinc/librdkafka/blob/644e97a67d9585c7ab63c249f043932e25239ddb/README.md#L9-L24).

## Mechanism worth inspecting

The message status distinguishes never persisted, possibly persisted without acknowledgement, and acknowledged persistence. Its documentation states different duplication risks for application retries. The implementation refuses to downgrade a previously persisted or possibly persisted message to not persisted. [Status contract](https://github.com/confluentinc/librdkafka/blob/644e97a67d9585c7ab63c249f043932e25239ddb/src/rdkafka.h#L1727-L1742); [monotonic evidence](https://github.com/confluentinc/librdkafka/blob/644e97a67d9585c7ab63c249f043932e25239ddb/src/rdkafka_msg.c#L1011-L1020).

## Important limit

These states describe Kafka log delivery, not an exchange order. The useful transfer is the uncertainty model: a trading system needs venue-specific evidence to resolve an unacknowledged action, and the Kafka persistence note depends on acks=all.

## Questions to take into your own design

- Does a timeout preserve possible execution rather than turn it into zero execution?
- Can later weaker evidence overwrite a previously confirmed outcome?

## Why this score for a trading system

3/5: a precise transferable evidence model, requiring exchange-specific action identities and reconciliation.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
