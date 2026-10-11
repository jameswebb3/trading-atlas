# Evidently: A dataset-wide drift pass can hide one critical column

**Decision question:** Could one broken field be green because most columns are stable?

| Field | Review |
| --- | --- |
| Upstream | [evidentlyai/evidently](https://github.com/evidentlyai/evidently) |
| Primary area | Operations & Observability |
| Source commit | [34771fe41c08ca074d96a52aaf4a45cd640cbaf5](https://github.com/evidentlyai/evidently/commit/34771fe41c08ca074d96a52aaf4a45cd640cbaf5) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Computes per-column drift and aggregates it into a dataset-wide drift share. The default 50% share can pass while a single decision-critical field has drifted. |

## Mechanism worth inspecting

DataDriftPreset selects methods and thresholds per column, then applies a default dataset drift_share of 0.5. The code makes it easy to see how an aggregate status can disagree with a critical field’s status.

**Source trail:** [project overview](https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/README.md) · [documentation](https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/README.md#L151-L166) · [implementation](https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/src/evidently/presets/drift.py#L24-L62).

## Important limit

Drift is a comparison with reference data, not proof of bad market data or a causal error. Thresholds must be tied to field impact and enough observations, not accepted from defaults.

## Questions to take into your own design

- Are critical fields evaluated individually before the aggregate verdict?
- Does an alert distinguish missing data from distribution shift?

## Why this score for a trading system

Drift dashboards are useful context, but a dataset-wide default can hide one critical market field and drift is not decision validity.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
