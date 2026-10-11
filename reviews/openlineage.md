# OpenLineage: Separate design lineage from run evidence

**Decision question:** Does a lineage graph prove what actually ran, or only what was declared?

| Field | Review |
| --- | --- |
| Upstream | [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [d204b0e1be9040d3f39474fe257ae103842e811d](https://github.com/OpenLineage/OpenLineage/commit/d204b0e1be9040d3f39474fe257ae103842e811d) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/OpenLineage/OpenLineage/blob/d204b0e1be9040d3f39474fe257ae103842e811d/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Distinguishes runtime RunEvents from design-time JobEvents and DatasetEvents. A declared upstream relation is not proof that a particular run consumed the intended dataset bytes. |

## Project overview

Open standard for recording jobs, runs, and dataset relationships. Gives data pipelines a common way to report how inputs and outputs connect across tools.

[Project documentation](https://github.com/OpenLineage/OpenLineage/blob/d204b0e1be9040d3f39474fe257ae103842e811d/README.md#L12-L15).

## Mechanism worth inspecting

The object model separates run-state updates from static job and dataset metadata; design events are not attached to a run. The Python client accepts these event classes explicitly and adds event facets before emission. This split prevents an architecture map from masquerading as execution evidence.

**Source trail:** [project overview](https://github.com/OpenLineage/OpenLineage/blob/d204b0e1be9040d3f39474fe257ae103842e811d/README.md) · [documentation](https://github.com/OpenLineage/OpenLineage/blob/d204b0e1be9040d3f39474fe257ae103842e811d/website/docs/spec/object-model.md#L14-L29) · [implementation](https://github.com/OpenLineage/OpenLineage/blob/d204b0e1be9040d3f39474fe257ae103842e811d/client/python/src/openlineage/client/client.py#L185-L200).

## Important limit

An emitted event can still name an incomplete or incorrect dataset. For reproducibility, the run also needs an immutable input identity and the producer’s time constraints.

## Questions to take into your own design

- Can a result be walked back to the run event and exact input identity?
- Are declared dependencies labeled differently from observed consumption?

## Why this score for a trading system

Run events improve trading-experiment provenance, though declared and observed lineage still need exact input snapshot identity.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
