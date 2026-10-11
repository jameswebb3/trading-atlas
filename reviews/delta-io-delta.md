# Delta Lake — What makes retrying an ingestion batch idempotent

**Decision question:** What makes retrying an ingestion batch idempotent?

| Field | Review |
| --- | --- |
| Upstream | [Delta Lake](https://github.com/delta-io/delta) |
| Primary area | Data Quality & Lineage |
| Source commit | [ca2e1952187f05936045dd7c5d6f2c8c97926ca7](https://github.com/delta-io/delta/commit/ca2e1952187f05936045dd7c5d6f2c8c97926ca7) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/delta-io/delta/blob/ca2e1952187f05936045dd7c5d6f2c8c97926ca7/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful ingestion reference for committing batch identity with data. Idempotency still depends on stable producer identity, version meaning and content; a transaction marker is not a universal exactly-once guarantee. |

## Project overview

Delta Lake records table changes and transaction identifiers in a transaction log for analytical storage. [Project documentation](https://github.com/delta-io/delta/blob/ca2e1952187f05936045dd7c5d6f2c8c97926ca7/README.md#L8-L26).

## Mechanism worth inspecting

The protocol commits application ID and version atomically with table changes, while leaving version semantics to the producer. The Scala transaction builder removes identical SetTransaction duplicates and rejects conflicting versions for one application. [Protocol](https://github.com/delta-io/delta/blob/ca2e1952187f05936045dd7c5d6f2c8c97926ca7/PROTOCOL.md#L697-L712), [conflict gate](https://github.com/delta-io/delta/blob/ca2e1952187f05936045dd7c5d6f2c8c97926ca7/spark/src/main/scala/org/apache/spark/sql/delta/OptimisticTransaction.scala#L1627-L1647).

## Important limit

The protocol does not require monotonically increasing application versions. A producer that reuses identity for different content can defeat its own deduplication meaning; cross-system effects are not made atomic by a table commit.

## Questions to take into your own design

- What makes retrying an ingestion batch idempotent?
- Does a reused batch identity prove identical content as well as identical application version?

## Why this score for a trading system

3/5: concrete transferable atomic-ingestion boundary, with a large platform whose adoption is unnecessary to implement a small equivalent contract.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
