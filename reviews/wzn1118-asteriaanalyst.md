# AsteriaAnalyst — Block claims that lack their required fields

**Decision question:** Can an analyst report claim ROI or a trend without the underlying fields?

| Field | Review |
| --- | --- |
| Upstream | [wzn1118/AsteriaAnalyst](https://github.com/wzn1118/AsteriaAnalyst) |
| Primary area | Agents & Decision Systems |
| Source commit | [b9b817053d6b40b6a4222efcd472cffe1345e5ea](https://github.com/wzn1118/AsteriaAnalyst/commit/b9b817053d6b40b6a4222efcd472cffe1345e5ea) |
| Reviewed | 2026-10-09 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The guard checks the available field types and attempted metric families, then flags profit/ROI claims without cost and growth claims without time. Much of the detection is keyword-based and tied to its business domains; the root license was not found, so this is a pattern only. |

## What this project does

Analytics report pipeline with a deterministic quality gate over generated management text and metric payloads. [README](https://github.com/wzn1118/AsteriaAnalyst/blob/b9b817053d6b40b6a4222efcd472cffe1345e5ea/README.md).

## Mechanism inspected

The guard checks the available field types and attempted metric families, then flags profit/ROI claims without cost and growth claims without time. [Implementation](https://github.com/wzn1118/AsteriaAnalyst/blob/b9b817053d6b40b6a4222efcd472cffe1345e5ea/backend/app/services/all_report_quality_gate_service.py#L109-L158).

## Limitation that matters

Much of the detection is keyword-based and tied to its business domains; the root license was not found, so this is a pattern only. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Before publishing a trading research conclusion, assert that every claim has the prerequisite fields and metric family, with unresolved gaps explicit.

## Why this score

The guard checks the available field types and attempted metric families, then flags profit/ROI claims without cost and growth claims without time. Much of the detection is keyword-based and tied to its business domains; the root license was not found, so this is a pattern only.

## Source trail

[README](https://github.com/wzn1118/AsteriaAnalyst/blob/b9b817053d6b40b6a4222efcd472cffe1345e5ea/README.md) · [Implementation](https://github.com/wzn1118/AsteriaAnalyst/blob/b9b817053d6b40b6a4222efcd472cffe1345e5ea/backend/app/services/all_report_quality_gate_service.py#L109-L158).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
