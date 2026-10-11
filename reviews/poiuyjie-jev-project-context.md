# Project Context V2: Can an invalidated experiment remain the current research conclusion?

**Decision question:** Can an invalidated experiment remain the current research conclusion?

| Field | Review |
| --- | --- |
| Upstream | [poiuyjie/jev_project_context](https://github.com/poiuyjie/jev_project_context) |
| Primary area | Research & Reproducibility |
| Source commit | [52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359](https://github.com/poiuyjie/jev_project_context/commit/52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/poiuyjie/jev_project_context/blob/52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The experiment scaffold records question, hypotheses, protocol, seeds, configuration, checkpoint lineage, artifacts and validity. Its read-only doctor checks headings and provenance terms, flags retired evidence without a visible replacement, and errors if invalidated records exist but the current summary is absent. The doctor relies on text patterns and presence of terms, so a false or stale provenance line can pass. Optional semantic judgments in the project remain advisory. The workflow is for general ML and does not implement a trading gauntlet or holdout policy. |

## What this project does

Scaffolds experiment records with provenance and validity threats, then audits missing fields and warns when invalidated evidence lacks a replacement link. The checks are structural and cannot establish that the linked evidence is sound.

## Mechanism inspected

The experiment scaffold records question, hypotheses, protocol, seeds, configuration, checkpoint lineage, artifacts and validity. Its read-only doctor checks headings and provenance terms, flags retired evidence without a visible replacement, and errors if invalidated records exist but the current summary is absent.

## Limitation that matters

The doctor relies on text patterns and presence of terms, so a false or stale provenance line can pass. Optional semantic judgments in the project remain advisory. The workflow is for general ML and does not implement a trading gauntlet or holdout policy.

## Practical check for a trading system

For a research ledger, invalidate a previously accepted run and verify the current summary points to the correction. Test missing dataset split, code revision and artifact index, then independently verify the referenced source data.

## Why this score

3/5 transferable: stale conclusions are a real research hazard and the status-to-current-view gate is concrete, but structural lint cannot replace data or statistical verification.

## Source trail

[README.md](https://github.com/poiuyjie/jev_project_context/blob/52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359/README.md#L5); [scripts/new_experiment.py](https://github.com/poiuyjie/jev_project_context/blob/52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359/scripts/new_experiment.py#L2); [scripts/doctor.py](https://github.com/poiuyjie/jev_project_context/blob/52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359/scripts/doctor.py#L65); [scripts/doctor.py](https://github.com/poiuyjie/jev_project_context/blob/52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359/scripts/doctor.py#L115); [scripts/doctor.py](https://github.com/poiuyjie/jev_project_context/blob/52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359/scripts/doctor.py#L145)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
