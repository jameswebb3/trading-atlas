# seglearn — window count is not independent sample count

**Decision question:** Can overlapping segments cross a train/test boundary?

| Field | Review |
| --- | --- |
| Upstream | [seglearn](https://github.com/dmbee/seglearn) |
| Primary area | Signals & Models |
| Source commit | [b93b670fd62d4ff22bd44d15023422f20789fd23](https://github.com/dmbee/seglearn/commit/b93b670fd62d4ff22bd44d15023422f20789fd23) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/dmbee/seglearn/blob/b93b670fd62d4ff22bd44d15023422f20789fd23/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | A clear example of how sliding windows multiply samples without multiplying independent evidence. Preserve interval provenance and assign temporal splits before treating segments as evaluation cases. |

## Project overview

seglearn turns time series into segment samples for machine-learning pipelines, aligning targets and weights with the transformed sample count. [Project documentation](https://github.com/dmbee/seglearn/blob/b93b670fd62d4ff22bd44d15023422f20789fd23/seglearn/transform.py#L189-L224).

## Mechanism worth inspecting

Segment width and overlap determine a step size; the implementation creates sliding windows and may shuffle the resulting segments. One source series becomes many samples. [Step calculation](https://github.com/dmbee/seglearn/blob/b93b670fd62d4ff22bd44d15023422f20789fd23/seglearn/transform.py#L137-L165); [segmentation and shuffle](https://github.com/dmbee/seglearn/blob/b93b670fd62d4ff22bd44d15023422f20789fd23/seglearn/transform.py#L214-L240).

## Important limit

Adjacent segments can share raw observations. Randomly splitting the expanded samples can put substantially the same input on both sides of evaluation. Segmentation is a representation operation, not a temporal split or an independence guarantee.

## Questions to take into your own design

- Are source-time boundaries and purge gaps established before overlapping windows are allocated?
- Does every segment retain source ID, start, end and label horizon?

## Why this score for a trading system

2/5: a narrow window-provenance reference; a trading research system can implement the relevant boundary contract without adopting the broader pipeline.

**Scope of this review:** Segment transformation and overlap/shuffle behavior; not the project's complete estimator integration.
