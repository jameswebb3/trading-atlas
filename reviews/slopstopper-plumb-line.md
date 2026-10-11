# plumb-line — Catch confidence laundering through derived data

**Decision question:** Can a conclusion claim stronger evidence than any of its inputs?

| Field | Review |
| --- | --- |
| Upstream | [slopstopper/plumb-line](https://github.com/slopstopper/plumb-line) |
| Primary area | Agents & Decision Systems |
| Source commit | [2b61a7b5f2522ab37ce95b24e6099a3d3b3a8af6](https://github.com/slopstopper/plumb-line/commit/2b61a7b5f2522ab37ce95b24e6099a3d3b3a8af6) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/slopstopper/plumb-line/blob/2b61a7b5f2522ab37ce95b24e6099a3d3b3a8af6/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The audit flags a clean source derived from mock data, output confidence above its weakest lineage input, a missing taint flag and a derived value with no lineage. Its ordinal source ladder is domain-specific; numeric confidence is not calibrated for trading and lineage declarations can omit a real dependency. |

## What this project does

Provenance contract and auditor for source classes, confidence and mock-derived taint. [README](https://github.com/slopstopper/plumb-line/blob/2b61a7b5f2522ab37ce95b24e6099a3d3b3a8af6/README.md).

## Mechanism inspected

The audit flags a clean source derived from mock data, output confidence above its weakest lineage input, a missing taint flag and a derived value with no lineage. [Implementation](https://github.com/slopstopper/plumb-line/blob/2b61a7b5f2522ab37ce95b24e6099a3d3b3a8af6/primitives/python/audit.py#L123-L165).

## Limitation that matters

Its ordinal source ladder is domain-specific; numeric confidence is not calibrated for trading and lineage declarations can omit a real dependency. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

In research artifacts, reject evidence-class or confidence upgrades across derivations unless a stronger independently verified source is added and recorded.

## Why this score

The audit flags a clean source derived from mock data, output confidence above its weakest lineage input, a missing taint flag and a derived value with no lineage. Its ordinal source ladder is domain-specific; numeric confidence is not calibrated for trading and lineage declarations can omit a real dependency.

## Source trail

[README](https://github.com/slopstopper/plumb-line/blob/2b61a7b5f2522ab37ce95b24e6099a3d3b3a8af6/README.md) · [Implementation](https://github.com/slopstopper/plumb-line/blob/2b61a7b5f2522ab37ce95b24e6099a3d3b3a8af6/primitives/python/audit.py#L123-L165) · [License](https://github.com/slopstopper/plumb-line/blob/2b61a7b5f2522ab37ce95b24e6099a3d3b3a8af6/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
