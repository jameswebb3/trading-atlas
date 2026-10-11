# SGI-Bench — Exact checks and model judges are different evidence

**Decision question:** Can an agent benchmark tell deterministic correctness from judge opinion?

| Field | Review |
| --- | --- |
| Upstream | [SGI-Bench](https://github.com/InternScience/SGI-Bench) |
| Primary area | Agents & Decision Systems |
| Source commit | [271270efe9f7594694cddb01e630a609542a8619](https://github.com/InternScience/SGI-Bench/commit/271270efe9f7594694cddb01e630a609542a8619) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/InternScience/SGI-Bench/blob/271270efe9f7594694cddb01e630a609542a8619/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its scorer first checks exact output and execution errors, then asks an LLM judge to adjudicate remaining cases. A judge decision can be wrong or unstable; a passing explanation is not a replicated numerical result. |

## What this project does

A benchmark for scientist-style agent workflows and dry experiments. [README](https://github.com/InternScience/SGI-Bench/blob/271270efe9f7594694cddb01e630a609542a8619/README.md).

## Mechanism inspected

Its scorer first checks exact output and execution errors, then asks an LLM judge to adjudicate remaining cases. [Implementation](https://github.com/InternScience/SGI-Bench/blob/271270efe9f7594694cddb01e630a609542a8619/evaluation/task_3_dry_experiment/step_4_score.py#L27-L83).

## Limitation that matters

A judge decision can be wrong or unstable; a passing explanation is not a replicated numerical result. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Separate deterministic checks, judge assessments and unresolved cases in agent evidence receipts.

## Why this score

Transferable engineering pattern: Its scorer first checks exact output and execution errors, then asks an LLM judge to adjudicate remaining cases. A judge decision can be wrong or unstable; a passing explanation is not a replicated numerical result.

## Source trail

[README](https://github.com/InternScience/SGI-Bench/blob/271270efe9f7594694cddb01e630a609542a8619/README.md) · [Implementation](https://github.com/InternScience/SGI-Bench/blob/271270efe9f7594694cddb01e630a609542a8619/evaluation/task_3_dry_experiment/step_4_score.py#L27-L83).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
