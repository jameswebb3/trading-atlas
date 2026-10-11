# A simulated feature delay is only as honest as its configuration

**Decision question:** Does a point-in-time join account for publication lag or only event time?

| Field | Review |
| --- | --- |
| Upstream | [Feathr](https://github.com/feathr-ai/feathr) |
| Primary area | Data Quality & Lineage |
| Source commit | [45e44afc1ebd3abc0fa8313aac21db7b1f05580a](https://github.com/feathr-ai/feathr/commit/45e44afc1ebd3abc0fa8313aac21db7b1f05580a) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/feathr-ai/feathr/blob/45e44afc1ebd3abc0fa8313aac21db7b1f05580a/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Feathr passes a configured delay into each sliding-window feature; absent a feature or default delay, it uses zero. This can represent known publication lag, but a point-in-time join is not evidence that the configured delay matches real delivery or later corrections. |

## Mechanism worth inspecting

The [overview](https://github.com/feathr-ai/feathr/blob/45e44afc1ebd3abc0fa8313aac21db7b1f05580a/docs/README.md#L28-L40) describes time-aware feature joins, while the [point-in-time guide](https://github.com/feathr-ai/feathr/blob/45e44afc1ebd3abc0fa8313aac21db7b1f05580a/docs/concepts/point-in-time-join.md#L11-L23) explains future leakage. The [feature builder](https://github.com/feathr-ai/feathr/blob/45e44afc1ebd3abc0fa8313aac21db7b1f05580a/feathr-impl/src/main/scala/com/linkedin/feathr/offline/swa/SlidingWindowFeatureUtils.scala#L119-L139) chooses a per-feature delay, a default, or Duration.ZERO and [constructs the window](https://github.com/feathr-ai/feathr/blob/45e44afc1ebd3abc0fa8313aac21db7b1f05580a/feathr-impl/src/main/scala/com/linkedin/feathr/offline/swa/SlidingWindowFeatureUtils.scala#L169-L176) with that delay.

## Important limit

A fixed lag cannot by itself model variable delivery, revisions, or outage backfills. The inspected path applies the configured value; it does not verify availability timestamps against the source.

## Questions to take into your own design

- What evidence supports each feature's delay?
- How are delayed corrections prevented from entering earlier decisions?

## Why this score for a trading system

3/5: Explicit feature-delay selection is a valuable causal-data pattern, but the application must supply and validate real availability semantics.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
