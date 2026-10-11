# voltagent - Keep skipped and failed scorers out of zero scores

**Decision question:** What does a missing agent-evaluation score mean?

| Field | Review |
| --- | --- |
| Upstream | [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent) |
| Primary area | Agents & Decision Systems |
| Source commit | [72a46c76b4507e1f98b41d5050a92bd30587eb70](https://github.com/VoltAgent/voltagent/commit/72a46c76b4507e1f98b41d5050a92bd30587eb70) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/VoltAgent/voltagent/blob/72a46c76b4507e1f98b41d5050a92bd30587eb70/LICENCE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The scorer runtime records success, error or skipped separately from a nullable score, sampled/not-sampled metadata, duration and an input/parameter snapshot. A well-formed result does not validate the scorer, case selection or reference answer; sampling and scorer version must be pinned for reproducible comparisons. |

## What this project does

VoltAgent provides agent execution primitives and local scorer hooks. [README](https://github.com/VoltAgent/voltagent/blob/72a46c76b4507e1f98b41d5050a92bd30587eb70/README.md).

## Mechanism inspected

The scorer runtime records success, error or skipped separately from a nullable score, sampled/not-sampled metadata, duration and an input/parameter snapshot. [Implementation](https://github.com/VoltAgent/voltagent/blob/72a46c76b4507e1f98b41d5050a92bd30587eb70/packages/core/src/eval/runtime/runtime.ts#L125-L230).

## Limitation that matters

A well-formed result does not validate the scorer, case selection or reference answer; sampling and scorer version must be pinned for reproducible comparisons. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

Store evaluator status and sampling separately from numeric score; block aggregated agent scores when the required scorer did not run.

## Why this score

The scorer runtime records success, error or skipped separately from a nullable score, sampled/not-sampled metadata, duration and an input/parameter snapshot. A well-formed result does not validate the scorer, case selection or reference answer; sampling and scorer version must be pinned for reproducible comparisons.

## Source trail

[README](https://github.com/VoltAgent/voltagent/blob/72a46c76b4507e1f98b41d5050a92bd30587eb70/README.md) - [Implementation](https://github.com/VoltAgent/voltagent/blob/72a46c76b4507e1f98b41d5050a92bd30587eb70/packages/core/src/eval/runtime/runtime.ts#L125-L230) - [License](https://github.com/VoltAgent/voltagent/blob/72a46c76b4507e1f98b41d5050a92bd30587eb70/LICENCE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
