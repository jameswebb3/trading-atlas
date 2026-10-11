# pbt - Shrink a stateful failure without invalidating it

**Decision question:** Can a generated order sequence be reduced to a valid minimal failure?

| Field | Review |
| --- | --- |
| Upstream | [ohbarye/pbt](https://github.com/ohbarye/pbt) |
| Primary area | Testing & Verification |
| Source commit | [8f7f0a92d868cd93577d6f18240597e343c16a43](https://github.com/ohbarye/pbt/commit/8f7f0a92d868cd93577d6f18240597e343c16a43) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/ohbarye/pbt/blob/8f7f0a92d868cd93577d6f18240597e343c16a43/LICENSE.txt)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The stateful generator selects applicable commands; its shrinker tries shorter prefixes and smaller arguments, retaining only valid sequences. The code is Ruby-specific and explicitly disallows parallel Ractor execution for stateful properties; timing races still need targeted tests. |

## What this project does

A Ruby property-testing library models commands over evolving state and executes them against a fresh system under test. [README](https://github.com/ohbarye/pbt/blob/8f7f0a92d868cd93577d6f18240597e343c16a43/README.md).

## Mechanism inspected

The stateful generator selects applicable commands; its shrinker tries shorter prefixes and smaller arguments, retaining only valid sequences. [Implementation](https://github.com/ohbarye/pbt/blob/8f7f0a92d868cd93577d6f18240597e343c16a43/lib/pbt/stateful/property.rb#L49-L97).

## Limitation that matters

The code is Ruby-specific and explicitly disallows parallel Ractor execution for stateful properties; timing races still need targeted tests. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

Use the model-state idea to generate ACK, fill, cancel, restart and replace sequences; keep preconditions valid while minimizing a failing case.

## Why this score

The stateful generator selects applicable commands; its shrinker tries shorter prefixes and smaller arguments, retaining only valid sequences. The code is Ruby-specific and explicitly disallows parallel Ractor execution for stateful properties; timing races still need targeted tests.

## Source trail

[README](https://github.com/ohbarye/pbt/blob/8f7f0a92d868cd93577d6f18240597e343c16a43/README.md) - [Implementation](https://github.com/ohbarye/pbt/blob/8f7f0a92d868cd93577d6f18240597e343c16a43/lib/pbt/stateful/property.rb#L49-L97) - [License](https://github.com/ohbarye/pbt/blob/8f7f0a92d868cd93577d6f18240597e343c16a43/LICENSE.txt).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
