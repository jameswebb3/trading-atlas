# scholar-loop - Freeze the scorer and account for failed seeds

**Decision question:** Can a training run alter the code that decides whether it passed?

| Field | Review |
| --- | --- |
| Upstream | [tenorleibniz832/scholar-loop](https://github.com/tenorleibniz832/scholar-loop) |
| Primary area | Testing & Verification |
| Source commit | [daa05ee3b071ecdd2f48b03465d8a2e4add70de8](https://github.com/tenorleibniz832/scholar-loop/commit/daa05ee3b071ecdd2f48b03465d8a2e4add70de8) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/tenorleibniz832/scholar-loop/blob/daa05ee3b071ecdd2f48b03465d8a2e4add70de8/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | It hashes the frozen scorer, refuses scoring if the file changes or vanishes, restricts source edits to the train entrypoint and records per-seed results and failures. A fully failed seed set becomes a killed run. When any seed succeeds, aggregate and verdict use only survivors, which can favor fragile candidates. Hash comparison detects tampering but does not isolate the process. |

## What this project does

scholar-loop runs automated model experiments against a fixed scoring module and records an experiment ledger. [README](https://github.com/tenorleibniz832/scholar-loop/blob/daa05ee3b071ecdd2f48b03465d8a2e4add70de8/README.md).

## Mechanism inspected

It hashes the frozen scorer, refuses scoring if the file changes or vanishes, restricts source edits to the train entrypoint and records per-seed results and failures. A fully failed seed set becomes a killed run. [Implementation](https://github.com/tenorleibniz832/scholar-loop/blob/daa05ee3b071ecdd2f48b03465d8a2e4add70de8/scholarloop/runner.py#L140-L168). [Related path](https://github.com/tenorleibniz832/scholar-loop/blob/daa05ee3b071ecdd2f48b03465d8a2e4add70de8/scholarloop/runner.py#L179-L245).

## Limitation that matters

When any seed succeeds, aggregate and verdict use only survivors, which can favor fragile candidates. Hash comparison detects tampering but does not isolate the process. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Keep the evaluator outside candidate-controlled edits, pin its hash, and require a predeclared successful-seed count before any candidate can advance.

## Why this score

Evaluator integrity and partial-run accounting are directly useful to research verification, although the upstream acceptance rule is too permissive for a trading gate.

## Source trail

[README](https://github.com/tenorleibniz832/scholar-loop/blob/daa05ee3b071ecdd2f48b03465d8a2e4add70de8/README.md) - [Implementation](https://github.com/tenorleibniz832/scholar-loop/blob/daa05ee3b071ecdd2f48b03465d8a2e4add70de8/scholarloop/runner.py#L140-L168) - [Related path](https://github.com/tenorleibniz832/scholar-loop/blob/daa05ee3b071ecdd2f48b03465d8a2e4add70de8/scholarloop/runner.py#L179-L245) - [License](https://github.com/tenorleibniz832/scholar-loop/blob/daa05ee3b071ecdd2f48b03465d8a2e4add70de8/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
