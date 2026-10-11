# kedro-viz — A run view can hide loader failure

**Decision question:** Can a visualization API return an empty run after an exception?

| Field | Review |
| --- | --- |
| Upstream | [kedro-viz](https://github.com/kedro-org/kedro-viz) |
| Primary area | Research & Reproducibility |
| Source commit | [3d3aca2d05328b82ba9dc7afe89e36cf475b9124](https://github.com/kedro-org/kedro-viz/commit/3d3aca2d05328b82ba9dc7afe89e36cf475b9124) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/kedro-org/kedro-viz/blob/3d3aca2d05328b82ba9dc7afe89e36cf475b9124/LICENSE.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The response builder maps node and dataset events into status objects, but its outer exception handler logs and returns an empty response. An empty response may look like no runs unless the caller checks an error channel; visualization is not trial admission. |

## What this project does

A visualization layer for Kedro pipelines with run-event responses. [README](https://github.com/kedro-org/kedro-viz/blob/3d3aca2d05328b82ba9dc7afe89e36cf475b9124/README.md).

## Mechanism inspected

The response builder maps node and dataset events into status objects, but its outer exception handler logs and returns an empty response. [Implementation](https://github.com/kedro-org/kedro-viz/blob/3d3aca2d05328b82ba9dc7afe89e36cf475b9124/package/kedro_viz/api/rest/responses/run_events.py#L463-L496).

## Limitation that matters

An empty response may look like no runs unless the caller checks an error channel; visualization is not trial admission. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Make an unreadable run log explicitly ERROR, never an empty successful research history.

## Why this score

Transferable engineering pattern: The response builder maps node and dataset events into status objects, but its outer exception handler logs and returns an empty response. An empty response may look like no runs unless the caller checks an error channel; visualization is not trial admission.

## Source trail

[README](https://github.com/kedro-org/kedro-viz/blob/3d3aca2d05328b82ba9dc7afe89e36cf475b9124/README.md) · [Documentation](https://github.com/kedro-org/kedro-viz/blob/3d3aca2d05328b82ba9dc7afe89e36cf475b9124/package/README.md) · [Implementation](https://github.com/kedro-org/kedro-viz/blob/3d3aca2d05328b82ba9dc7afe89e36cf475b9124/package/kedro_viz/api/rest/responses/run_events.py#L463-L496).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
