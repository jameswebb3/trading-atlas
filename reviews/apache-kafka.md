# Apache Kafka — Does a committed consumer position mean the corresponding data was durably processed

**Decision question:** Does a committed consumer position mean the corresponding data was durably processed?

| Field | Review |
| --- | --- |
| Upstream | [Apache Kafka](https://github.com/apache/kafka) |
| Primary area | Data Quality & Lineage |
| Source commit | [2a3d4a6b80507edefb1f969b3de6378235a5c34f](https://github.com/apache/kafka/commit/2a3d4a6b80507edefb1f969b3de6378235a5c34f) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/apache/kafka/blob/2a3d4a6b80507edefb1f969b3de6378235a5c34f/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Separates fetch progress from durable processing and documents the replay window between database insertion and offset commit. Useful for collector checkpoints that must not skip unfinished data. |

## Project overview

A distributed event-streaming platform supporting data pipelines, streaming analytics and integration. [Project documentation](https://github.com/apache/kafka/blob/2a3d4a6b80507edefb1f969b3de6378235a5c34f/README.md#L12-L12).

## Mechanism worth inspecting

The consumer documentation separates fetched position from committed position and describes committing only after database insertion. It also specifies that the committed offset is the next record to read. The classic consumer's no-argument commit uses allConsumed, while the explicit map path forwards the supplied offsets. [Processing boundary](https://github.com/apache/kafka/blob/2a3d4a6b80507edefb1f969b3de6378235a5c34f/clients/src/main/java/org/apache/kafka/clients/consumer/KafkaConsumer.java#L249-L289); [commit implementation](https://github.com/apache/kafka/blob/2a3d4a6b80507edefb1f969b3de6378235a5c34f/clients/src/main/java/org/apache/kafka/clients/consumer/internals/ClassicKafkaConsumer.java#L756-L780).

## Important limit

Inserting data before committing leaves a crash interval that can cause replayed inserts. Committing before processing can lose work. A broker checkpoint alone does not make an external database write atomic.

## Questions to take into your own design

- Does the checkpoint advance only through durably processed input?
- Can a crash after insertion replay the batch without duplicating its effects?

## Why this score for a trading system

3/5: a concrete transferable recovery contract, with external-database atomicity still belonging to the application.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
