# Aim: Track run context separately from artifacts

**Decision question:** Can a result be tied to its run, step, and saved artifact?

| Field | Review |
| --- | --- |
| Upstream | [aimhubio/aim](https://github.com/aimhubio/aim) |
| Primary area | Research & Reproducibility |
| Source commit | [6e098e38065364c76b2bb7c028f266e53b647642](https://github.com/aimhubio/aim/commit/6e098e38065364c76b2bb7c028f266e53b647642) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/aimhubio/aim/blob/6e098e38065364c76b2bb7c028f266e53b647642/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Tracks values by run, step, epoch, and context, and stores artifacts under a run-specific URI. A logged step is not an exchange event time; artifact upload and causal input identity require separate checks. |

## Mechanism worth inspecting

Aim’s run API appends homogeneous values to sequences indexed by name and context, with optional step and epoch. Artifact methods place files under a run URI keyed by run hash. This is a useful separation of scalar metric history from the files needed to inspect a result.

**Source trail:** [project overview](https://github.com/aimhubio/aim/blob/6e098e38065364c76b2bb7c028f266e53b647642/README.md) · [documentation](https://github.com/aimhubio/aim/blob/6e098e38065364c76b2bb7c028f266e53b647642/docs/source/using/artifacts.md#L1-L47) · [implementation](https://github.com/aimhubio/aim/blob/6e098e38065364c76b2bb7c028f266e53b647642/aim/sdk/run.py#L394-L456).

## Important limit

The source path does not enforce publication time or market chronology. Artifact upload may be non-blocking, so a tracking call is not itself evidence of durable retention.

## Questions to take into your own design

- Are metrics, code, and dataset snapshots attached to the same run receipt?
- When is an uploaded artifact considered durable?

## Why this score for a trading system

Run and artifact organization is useful background infrastructure, but step logging does not enforce market time or durable evidence.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
