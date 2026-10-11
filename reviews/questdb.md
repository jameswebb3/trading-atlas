# QuestDB: An omitted timestamp can become server time

**Decision question:** What timestamp is stored when an ingestion event omits one?

| Field | Review |
| --- | --- |
| Upstream | [questdb/questdb](https://github.com/questdb/questdb) |
| Primary area | Market Data & Ingestion |
| Source commit | [f96b1179b7ce26ceefe4326471785f09aa1476e7](https://github.com/questdb/questdb/commit/f96b1179b7ce26ceefe4326471785f09aa1476e7) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/questdb/questdb/blob/f96b1179b7ce26ceefe4326471785f09aa1476e7/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Its line-protocol writer appends rows under an explicit table timestamp, with a server-clock fallback when the input timestamp is missing. That fallback cannot be treated as an exchange event timestamp in a trading dataset. |

## Mechanism worth inspecting

QuestDB describes ordered and out-of-order event ingestion. In the line TCP measurement event, a NULL input timestamp is replaced by the writer timestamp driver before the row is appended. The branch makes a common ingestion ambiguity visible in code.

**Source trail:** [project overview](https://github.com/questdb/questdb/blob/f96b1179b7ce26ceefe4326471785f09aa1476e7/README.md) · [documentation](https://github.com/questdb/questdb/blob/f96b1179b7ce26ceefe4326471785f09aa1476e7/README.md#L115-L134) · [implementation](https://github.com/questdb/questdb/blob/f96b1179b7ce26ceefe4326471785f09aa1476e7/core/src/main/java/io/questdb/cutlass/line/tcp/LineTcpMeasurementEvent.java#L125-L143).

## Important limit

Server receipt or write time is not the same as market event time. The inspected branch does not establish that gaps, duplicate trade IDs, or exchange clock errors are rejected for trading use.

## Questions to take into your own design

- Can an ingestion schema reject a missing source event timestamp instead of silently substituting local time?
- Are source time and receipt time stored as separate fields?

## Why this score for a trading system

Its server-time fallback exposes a direct timestamp hazard in market data, while storage alone cannot certify feed completeness.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
