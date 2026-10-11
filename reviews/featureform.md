# Featureform: an as-of join needs more than one clock

**Decision question:** Which feature row is joined to a historical decision?

| Field | Review |
| --- | --- |
| Upstream | [Featureform](https://github.com/featureform/featureform) |
| Primary area | Data Quality & Lineage |
| Source commit | [dc8b9fcafb9c70e7803f5130d6c8438bc72344ba](https://github.com/featureform/featureform/commit/dc8b9fcafb9c70e7803f5130d6c8438bc72344ba) |
| Reviewed | 2026-09-25 |
| Declared license | [MPL-2.0](https://github.com/featureform/featureform/blob/dc8b9fcafb9c70e7803f5130d6c8438bc72344ba/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Builds a point-in-time training-set query only when the label table has a timestamp, joining feature time at or before label time. That comparison is useful, but it cannot infer when a feature value was published or corrected. |

## Mechanism worth inspecting

The [overview](https://github.com/featureform/featureform/blob/dc8b9fcafb9c70e7803f5130d6c8438bc72344ba/README.md#L32-L41) describes immutable features, labels, and training sets. The [query switch](https://github.com/featureform/featureform/blob/dc8b9fcafb9c70e7803f5130d6c8438bc72344ba/provider/tsquery/tsquery.go#L99-L129) selects a point-in-time builder only when the label has a timestamp column. The [ASOF predicate](https://github.com/featureform/featureform/blob/dc8b9fcafb9c70e7803f5130d6c8438bc72344ba/provider/tsquery/tsquery.go#L385-L405) requires equal entity keys and label time greater than or equal to feature time. This makes the matching rule inspectable instead of burying it in a model notebook.

## Important limit

Feature event time is not necessarily feature publication time. A value revised tomorrow but stamped with yesterday's event time can still satisfy the join. The fallback path without a label timestamp uses a different builder and must be treated as a separate evidence class.

## Questions to take into your own design

- Are event time, published-at time, and correction time represented separately?
- Is a point-in-time join refused when the decision timestamp is missing?

## Why this score for a trading system

The query builder gives a concrete as-of join boundary; publication lag and timestamp provenance remain outside the inspected rule.

**Scope of this review:** We read the pinned README, training-set notes, and SQL query builder. We did not execute a training-set query.
