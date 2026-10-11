# RecClaw — Validate an agent’s proposed search step before running it

**Decision question:** Can a research agent spend a run on an invalid or already tried candidate?

| Field | Review |
| --- | --- |
| Upstream | [DynamisG210/RecClaw](https://github.com/DynamisG210/RecClaw) |
| Primary area | Agents & Decision Systems |
| Source commit | [2d8c881354e1b536a6c66d7dfbb977e0c5090e50](https://github.com/DynamisG210/RecClaw/commit/2d8c881354e1b536a6c66d7dfbb977e0c5090e50) |
| Reviewed | 2026-10-09 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The validator checks action and model compatibility, parent candidate, duplicate IDs and parameter signatures, implementation path boundaries, then returns reject, review or accept before execution. The allowed changes and model families are RecClaw-specific; its validator cannot establish scientific novelty or out-of-sample value. No root license was found at the inspected commit. |

## What this project does

Recommender-model research loop with a declared candidate action space and proposal validator. [README](https://github.com/DynamisG210/RecClaw/blob/2d8c881354e1b536a6c66d7dfbb977e0c5090e50/README.md).

## Mechanism inspected

The validator checks action and model compatibility, parent candidate, duplicate IDs and parameter signatures, implementation path boundaries, then returns reject, review or accept before execution. [Implementation](https://github.com/DynamisG210/RecClaw/blob/2d8c881354e1b536a6c66d7dfbb977e0c5090e50/scripts/validate_candidate_proposal.py#L320-L549).

## Limitation that matters

The allowed changes and model families are RecClaw-specific; its validator cannot establish scientific novelty or out-of-sample value. No root license was found at the inspected commit. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Translate research-lane constraints into a typed pre-run proposal contract: parent, observable, allowed data, duplicate signature, planned seeds and outcome gate.

## Why this score

The validator checks action and model compatibility, parent candidate, duplicate IDs and parameter signatures, implementation path boundaries, then returns reject, review or accept before execution. The allowed changes and model families are RecClaw-specific; its validator cannot establish scientific novelty or out-of-sample value. No root license was found at the inspected commit.

## Source trail

[README](https://github.com/DynamisG210/RecClaw/blob/2d8c881354e1b536a6c66d7dfbb977e0c5090e50/README.md) · [Implementation](https://github.com/DynamisG210/RecClaw/blob/2d8c881354e1b536a6c66d7dfbb977e0c5090e50/scripts/validate_candidate_proposal.py#L320-L549).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
