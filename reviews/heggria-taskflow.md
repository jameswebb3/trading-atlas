# taskflow - Incomplete agent traces cannot support offline replay

**Decision question:** Can an old agent run be replayed when child and parent events are mixed?

| Field | Review |
| --- | --- |
| Upstream | [heggria/taskflow](https://github.com/heggria/taskflow) |
| Primary area | Agents & Decision Systems |
| Source commit | [f4e29406b78a1e16c9b69a50f62096fb6e4ae74c](https://github.com/heggria/taskflow/commit/f4e29406b78a1e16c9b69a50f62096fb6e4ae74c) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/heggria/taskflow/blob/f4e29406b78a1e16c9b69a50f62096fb6e4ae74c/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | selectOuterRun rejects append order as parent evidence, checks paired phase starts/ends, and marks unresolved mixed-run traces ambiguous; replay then requires a live rerun. Threshold and budget counterfactuals only reuse recorded evidence; model or argument changes require execution, and replay is not a trading backtest. |

## What this project does

A coding-agent workflow system records phase events and offers offline replay of a completed run. [README](https://github.com/heggria/taskflow/blob/f4e29406b78a1e16c9b69a50f62096fb6e4ae74c/README.md).

## Mechanism inspected

selectOuterRun rejects append order as parent evidence, checks paired phase starts/ends, and marks unresolved mixed-run traces ambiguous; replay then requires a live rerun. [Implementation](https://github.com/heggria/taskflow/blob/f4e29406b78a1e16c9b69a50f62096fb6e4ae74c/packages/taskflow-core/src/replay.ts#L91-L170).

## Limitation that matters

Threshold and budget counterfactuals only reuse recorded evidence; model or argument changes require execution, and replay is not a trading backtest. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

When reusing research-agent evidence, require run identity, complete lifecycle, recorded dependencies and explicit unreplayable status.

## Why this score

selectOuterRun rejects append order as parent evidence, checks paired phase starts/ends, and marks unresolved mixed-run traces ambiguous; replay then requires a live rerun. Threshold and budget counterfactuals only reuse recorded evidence; model or argument changes require execution, and replay is not a trading backtest.

## Source trail

[README](https://github.com/heggria/taskflow/blob/f4e29406b78a1e16c9b69a50f62096fb6e4ae74c/README.md) - [Implementation](https://github.com/heggria/taskflow/blob/f4e29406b78a1e16c9b69a50f62096fb6e4ae74c/packages/taskflow-core/src/replay.ts#L91-L170) - [License](https://github.com/heggria/taskflow/blob/f4e29406b78a1e16c9b69a50f62096fb6e4ae74c/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
