# OmniScientist — Interrupted research is not completed research

**Decision question:** When can an agent run be marked complete?

| Field | Review |
| --- | --- |
| Upstream | [OmniScientist](https://github.com/Omni-Scientist/OmniScientist) |
| Primary area | Agents & Decision Systems |
| Source commit | [4f3b5635397ac5420831430625d6f0e4713117d2](https://github.com/Omni-Scientist/OmniScientist/commit/4f3b5635397ac5420831430625d6f0e4713117d2) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/Omni-Scientist/OmniScientist/blob/4f3b5635397ac5420831430625d6f0e4713117d2/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and a relevant test read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its outcome function distinguishes user stop, truncation and normal end; tests assert a round limit is not completion. The classification relies on the provided stoppedBecause string and does not prove scientific correctness or complete artifacts. |

## What this project does

A local-first research agent with desktop and engine components. [README](https://github.com/Omni-Scientist/OmniScientist/blob/4f3b5635397ac5420831430625d6f0e4713117d2/README.md).

## Mechanism inspected

Its outcome function distinguishes user stop, truncation and normal end; tests assert a round limit is not completion. [Implementation](https://github.com/Omni-Scientist/OmniScientist/blob/4f3b5635397ac5420831430625d6f0e4713117d2/desktop/gateway/run-outcome.ts#L32-L62).

## Limitation that matters

The classification relies on the provided stoppedBecause string and does not prove scientific correctness or complete artifacts. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Require explicit DONE, STOPPED and TRUNCATED outcomes in research receipts and gate result admission on artifacts.

## Why this score

Transferable engineering pattern: Its outcome function distinguishes user stop, truncation and normal end; tests assert a round limit is not completion. The classification relies on the provided stoppedBecause string and does not prove scientific correctness or complete artifacts.

## Source trail

[README](https://github.com/Omni-Scientist/OmniScientist/blob/4f3b5635397ac5420831430625d6f0e4713117d2/README.md) · [Documentation](https://github.com/Omni-Scientist/OmniScientist/blob/4f3b5635397ac5420831430625d6f0e4713117d2/docs/USAGE.md) · [Implementation](https://github.com/Omni-Scientist/OmniScientist/blob/4f3b5635397ac5420831430625d6f0e4713117d2/desktop/gateway/run-outcome.ts#L32-L62) · [Relevant test](https://github.com/Omni-Scientist/OmniScientist/blob/4f3b5635397ac5420831430625d6f0e4713117d2/desktop/gateway/run-outcome.test.ts).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
