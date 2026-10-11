# Validate row identity before comparing a changed dataset

**Decision question:** Can a row-level data diff be trusted when the key is not unique?

| Field | Review |
| --- | --- |
| Upstream | [Recce](https://github.com/DataRecce/recce) |
| Primary area | Data Quality & Lineage |
| Source commit | [0cc4860a4a2138c9a69e58024c2d2129254116fb](https://github.com/DataRecce/recce/commit/0cc4860a4a2138c9a69e58024c2d2129254116fb) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/DataRecce/recce/blob/0cc4860a4a2138c9a69e58024c2d2129254116fb/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Recce checks primary-key uniqueness in both comparison environments before its value diff. That is a practical safeguard for reviewing revised market datasets: a join can produce convincing change counts from ambiguous row identities. The check does not establish historical availability or input vintage. |

## Mechanism worth inspecting

The [README](https://github.com/DataRecce/recce/blob/0cc4860a4a2138c9a69e58024c2d2129254116fb/README.md#L57-L69) requires two prepared comparison environments. The [architecture](https://github.com/DataRecce/recce/blob/0cc4860a4a2138c9a69e58024c2d2129254116fb/docs/architecture.md#L44-L49) stores results as explicit tasks. The [value-diff key validator](https://github.com/DataRecce/recce/blob/0cc4860a4a2138c9a69e58024c2d2129254116fb/recce/tasks/valuediff.py#L94-L143) generates uniqueness checks for each side and raises when the key is invalid or cannot be verified.

## Important limit

A valid key is only a prerequisite. The snapshots, SQL logic, schema, timing, and input data still need matching provenance. Comparing current tables does not reproduce what was available at a historical decision.

## Questions to take into your own design

- Is the timestamp/symbol key unique in both data revisions?
- Are both compared snapshots and their transformation code identified immutably?

## Why this score for a trading system

3/5: Key validation before a dataset diff is a concrete review gate for corrected trading data, with provenance and timing checks still required.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
