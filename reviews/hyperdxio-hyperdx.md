# hyperdx - Score the evidence an agent actually requested

**Decision question:** Did a research agent inspect the metric it cites?

| Field | Review |
| --- | --- |
| Upstream | [hyperdxio/hyperdx](https://github.com/hyperdxio/hyperdx) |
| Primary area | Agents & Decision Systems |
| Source commit | [0b9153d5e3ff9c71d4cc9f2ab0086ca93208cb59](https://github.com/hyperdxio/hyperdx/commit/0b9153d5e3ff9c71d4cc9f2ab0086ca93208cb59) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/hyperdxio/hyperdx/blob/0b9153d5e3ff9c71d4cc9f2ab0086ca93208cb59/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | runAdoptionChecks scores named metric keys found in input arguments of individual tool calls, separating informational checks from weighted scoring. A named metric in a query is only an evidence-use proxy; it does not prove that the returned series was correct or that the conclusion followed. |

## What this project does

An observability platform includes an evaluation harness for agent investigations. [README](https://github.com/hyperdxio/hyperdx/blob/0b9153d5e3ff9c71d4cc9f2ab0086ca93208cb59/README.md).

## Mechanism inspected

runAdoptionChecks scores named metric keys found in input arguments of individual tool calls, separating informational checks from weighted scoring. [Implementation](https://github.com/hyperdxio/hyperdx/blob/0b9153d5e3ff9c71d4cc9f2ab0086ca93208cb59/packages/hdx-eval/src/grading/programmatic.ts#L17-L113).

## Limitation that matters

A named metric in a query is only an evidence-use proxy; it does not prove that the returned series was correct or that the conclusion followed. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

In agent reviews, log the actual source/query invocation and distinguish source adoption from inference validity.

## Why this score

runAdoptionChecks scores named metric keys found in input arguments of individual tool calls, separating informational checks from weighted scoring. A named metric in a query is only an evidence-use proxy; it does not prove that the returned series was correct or that the conclusion followed.

## Source trail

[README](https://github.com/hyperdxio/hyperdx/blob/0b9153d5e3ff9c71d4cc9f2ab0086ca93208cb59/README.md) - [Implementation](https://github.com/hyperdxio/hyperdx/blob/0b9153d5e3ff9c71d4cc9f2ab0086ca93208cb59/packages/hdx-eval/src/grading/programmatic.ts#L17-L113) - [License](https://github.com/hyperdxio/hyperdx/blob/0b9153d5e3ff9c71d4cc9f2ab0086ca93208cb59/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
