# Marquez: an accepted lineage event may not be recorded

**Decision question:** Does HTTP success mean a lineage event entered the graph?

| Field | Review |
| --- | --- |
| Upstream | [Marquez](https://github.com/MarquezProject/marquez) |
| Primary area | Data Quality & Lineage |
| Source commit | [180f37b22387146187af1ef0279e3ee1d1ccd789](https://github.com/MarquezProject/marquez/commit/180f37b22387146187af1ef0279e3ee1d1ccd789) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/MarquezProject/marquez/blob/180f37b22387146187af1ef0279e3ee1d1ccd789/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Collects OpenLineage dataset, job, and run events. The inspected endpoint persists supported event classes, but responds HTTP 200 to an unsupported event class after logging that it was skipped. Callers need an ingestion acknowledgement stronger than generic HTTP success. |

## Mechanism worth inspecting

The [overview](https://github.com/MarquezProject/marquez/blob/180f37b22387146187af1ef0279e3ee1d1ccd789/README.md#L41-L43) describes collection of dataset, job, and run metadata through OpenLineage. The [API resource](https://github.com/MarquezProject/marquez/blob/180f37b22387146187af1ef0279e3ee1d1ccd789/api/src/main/java/marquez/api/OpenLineageResource.java#L64-L100) dispatches supported lineage, dataset, and job events to asynchronous creation. Its unsupported-type branch logs a warning, skips storage, and returns HTTP 200 with the event. The same endpoint returns 201 after successful supported-event processing.

## Important limit

This source-level finding does not establish how often unsupported classes reach that branch or whether clients validate event types before submission. Even a stored lineage edge records declared dependencies; it cannot certify that values were correct or available before the decision.

## Questions to take into your own design

- Does the producer distinguish accepted-for-processing from persisted?
- Can a declared lineage edge be reconciled to a real artifact hash and run result?

## Why this score for a trading system

Its event-ingestion branch exposes a concrete lineage acknowledgement trap, while a full service is excessive for a small trading research stack.

**Scope of this review:** We read the pinned README, compatibility notes, and HTTP event resource. We did not run the server or test client behavior.
