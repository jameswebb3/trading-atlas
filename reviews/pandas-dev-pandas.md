# pandas — an as-of match only knows the clock you give it

**Decision question:** Does a backward feature join use publication time or merely observation time?

| Field | Review |
| --- | --- |
| Upstream | [pandas](https://github.com/pandas-dev/pandas) |
| Primary area | Data Quality & Lineage |
| Source commit | [7aac4015369fe20bde6641276fc2fd1b11ca554b](https://github.com/pandas-dev/pandas/commit/7aac4015369fe20bde6641276fc2fd1b11ca554b) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/pandas-dev/pandas/blob/7aac4015369fe20bde6641276fc2fd1b11ca554b/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Backward matching, age limits and exact-match rules are explicit. A causal trading join still needs a publication-time key: matching an earlier observation alone does not establish that it was available. |

## Project overview

pandas supplies labeled data structures and time-aware joins, including backward, forward and nearest as-of matching. [Project documentation](https://github.com/pandas-dev/pandas/blob/7aac4015369fe20bde6641276fc2fd1b11ca554b/pandas/core/reshape/merge.py#L647-L724).

## Mechanism worth inspecting

`merge_asof` defaults to backward matching and accepts both a tolerance and an exact-match policy. Its implementation rejects unsorted join keys. These controls define matching on the selected key; they are useful building blocks for explicit age and boundary rules. [API](https://github.com/pandas-dev/pandas/blob/7aac4015369fe20bde6641276fc2fd1b11ca554b/pandas/core/reshape/merge.py#L647-L662); [sorted-key enforcement](https://github.com/pandas-dev/pandas/blob/7aac4015369fe20bde6641276fc2fd1b11ca554b/pandas/core/reshape/merge.py#L2636-L2660).

## Important limit

Backward matching on event time cannot prove that the matched record was published before the decision. The default tolerance is unrestricted, and equal timestamps are permitted. Publication time, maximum age and within-timestamp event ordering need their own contract.

## Questions to take into your own design

- Which timestamp certifies that the feature was usable, and is it the actual join key?
- What rejects stale values or unresolved same-timestamp ordering?

## Why this score for a trading system

3/5: an explicit temporal-join reference, with publication-time semantics and staleness policy still outside the library.

**Scope of this review:** merge_asof key validation and API boundaries; no audit of every pandas join.
