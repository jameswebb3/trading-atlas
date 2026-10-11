# trpc-agent-go - Inspect the denominator of repeated evaluations

**Decision question:** Can an aggregate pass while some evaluations did not run?

| Field | Review |
| --- | --- |
| Upstream | [trpc-group/trpc-agent-go](https://github.com/trpc-group/trpc-agent-go) |
| Primary area | Agents & Decision Systems |
| Source commit | [5344490e80af8cc26310ef633ec0916e10a7cb81](https://github.com/trpc-group/trpc-agent-go/commit/5344490e80af8cc26310ef633ec0916e10a7cb81) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/trpc-group/trpc-agent-go/blob/5344490e80af8cc26310ef633ec0916e10a7cb81/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its aggregator skips metrics marked NotEvaluated when averaging scores and stores the run statuses alongside aggregate metrics. The average is computed over evaluated runs. On repeated cases, a missing metric can shrink the denominator; a run error is forced to failure only when the aggregate stays NotEvaluated. |

## What this project does

trpc-agent-go supplies an agent evaluation runner with repeated case results and metric thresholds. [README](https://github.com/trpc-group/trpc-agent-go/blob/5344490e80af8cc26310ef633ec0916e10a7cb81/README.md).

## Mechanism inspected

Its aggregator skips metrics marked NotEvaluated when averaging scores and stores the run statuses alongside aggregate metrics. [Implementation](https://github.com/trpc-group/trpc-agent-go/blob/5344490e80af8cc26310ef633ec0916e10a7cb81/evaluation/evaluation.go#L606-L684). [Related path](https://github.com/trpc-group/trpc-agent-go/blob/5344490e80af8cc26310ef633ec0916e10a7cb81/evaluation/pass.go#L97-L128).

## Limitation that matters

The average is computed over evaluated runs. On repeated cases, a missing metric can shrink the denominator; a run error is forced to failure only when the aggregate stays NotEvaluated. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Require the planned run count and a policy for failed or missing evaluations before treating an aggregate score as evidence.

## Why this score

Useful evaluation accounting, but the observed acceptance logic is too permissive for a trading research gate.

## Source trail

[README](https://github.com/trpc-group/trpc-agent-go/blob/5344490e80af8cc26310ef633ec0916e10a7cb81/README.md) - [Implementation](https://github.com/trpc-group/trpc-agent-go/blob/5344490e80af8cc26310ef633ec0916e10a7cb81/evaluation/evaluation.go#L606-L684) - [Related path](https://github.com/trpc-group/trpc-agent-go/blob/5344490e80af8cc26310ef633ec0916e10a7cb81/evaluation/pass.go#L97-L128) - [License](https://github.com/trpc-group/trpc-agent-go/blob/5344490e80af8cc26310ef633ec0916e10a7cb81/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
