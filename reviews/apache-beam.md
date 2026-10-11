# Apache Beam — Can a window accept late data after its on-time result has fired

**Decision question:** Can a window accept late data after its on-time result has fired?

| Field | Review |
| --- | --- |
| Upstream | [Apache Beam](https://github.com/apache/beam) |
| Primary area | Data Quality & Lineage |
| Source commit | [6f0047c13a7e1e82b903313c45cdc0a0f9c22dc3](https://github.com/apache/beam/commit/6f0047c13a7e1e82b903313c45cdc0a0f9c22dc3) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/apache/beam/blob/6f0047c13a7e1e82b903313c45cdc0a0f9c22dc3/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Distinguishes early, on-time and late window results, and flags a configuration that can finish before allowed late data is handled. A useful pattern for versioned aggregates and honest decision-time reconstruction. |

## Project overview

A unified programming model for batch and stream processing, with SDKs and runners for several execution backends. [Project documentation](https://github.com/apache/beam/blob/6f0047c13a7e1e82b903313c45cdc0a0f9c22dc3/README.md#L22-L25).

## Mechanism worth inspecting

AfterWatermark can wrap early and late triggers, mark the transition into the late phase and keep the window active when a late trigger exists. Its data-loss check explicitly warns about finishing when lateness is allowed but no late trigger is configured. [Trigger phases](https://github.com/apache/beam/blob/6f0047c13a7e1e82b903313c45cdc0a0f9c22dc3/sdks/python/apache_beam/transforms/trigger.py#L547-L630); [loss check](https://github.com/apache/beam/blob/6f0047c13a7e1e82b903313c45cdc0a0f9c22dc3/sdks/python/apache_beam/transforms/trigger.py#L640-L646).

## Important limit

Allowing lateness does not by itself establish a correction policy. Consumers must distinguish versions or panes so that a later aggregate does not silently overwrite the data that an earlier decision actually saw.

## Questions to take into your own design

- Which aggregate version was available when a decision was made?
- Can a late correction change the stored observation without changing its original availability?

## Why this score for a trading system

3/5: a precise transferable window-lifecycle pattern; adopting the distributed framework is not necessary to use it.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
