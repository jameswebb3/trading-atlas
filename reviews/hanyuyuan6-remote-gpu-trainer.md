# remote-gpu-trainer — Keep reported numbers tied to one result artifact

**Decision question:** Can a corrected experiment number remain wrong in a report or README?

| Field | Review |
| --- | --- |
| Upstream | [Hanyuyuan6/remote-gpu-trainer](https://github.com/Hanyuyuan6/remote-gpu-trainer) |
| Primary area | Research & Reproducibility |
| Source commit | [9cd83978217bd92b1e7534efa440889d994096fc](https://github.com/Hanyuyuan6/remote-gpu-trainer/commit/9cd83978217bd92b1e7534efa440889d994096fc) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/Hanyuyuan6/remote-gpu-trainer/blob/9cd83978217bd92b1e7534efa440889d994096fc/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its reconciler loads scalar claims from an EVIDENCE.json file, scans report lines after configured anchor phrases, and records numeric drift against the authoritative value; a source test covers a stale number and a correct one. The scanner inspects only the first standalone number near each anchor, so aliases, tables and contextual numbers can escape or misfire; the manifest itself still needs derivation from raw results. |

## What this project does

Agent-oriented remote-training workflow with scripts for artifact verification, independent acceptance and cross-document claim reconciliation. [README](https://github.com/Hanyuyuan6/remote-gpu-trainer/blob/9cd83978217bd92b1e7534efa440889d994096fc/README.md).

## Mechanism inspected

Its reconciler loads scalar claims from an EVIDENCE.json file, scans report lines after configured anchor phrases, and records numeric drift against the authoritative value; a source test covers a stale number and a correct one. [Implementation](https://github.com/Hanyuyuan6/remote-gpu-trainer/blob/9cd83978217bd92b1e7534efa440889d994096fc/scripts/reconcile.py#L161-L216). [Related implementation](https://github.com/Hanyuyuan6/remote-gpu-trainer/blob/9cd83978217bd92b1e7534efa440889d994096fc/scripts/test_reconcile.py#L72-L99).

## Limitation that matters

The scanner inspects only the first standalone number near each anchor, so aliases, tables and contextual numbers can escape or misfire; the manifest itself still needs derivation from raw results. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Give every reported research metric one machine result identifier, then compare the value across generated reports, README and editorial summaries before publication.

## Why this score

Its reconciler loads scalar claims from an EVIDENCE.json file, scans report lines after configured anchor phrases, and records numeric drift against the authoritative value; a source test covers a stale number and a correct one. The scanner inspects only the first standalone number near each anchor, so aliases, tables and contextual numbers can escape or misfire; the manifest itself still needs derivation from raw results.

## Source trail

[README](https://github.com/Hanyuyuan6/remote-gpu-trainer/blob/9cd83978217bd92b1e7534efa440889d994096fc/README.md) · [Implementation](https://github.com/Hanyuyuan6/remote-gpu-trainer/blob/9cd83978217bd92b1e7534efa440889d994096fc/scripts/reconcile.py#L161-L216) · [Related implementation](https://github.com/Hanyuyuan6/remote-gpu-trainer/blob/9cd83978217bd92b1e7534efa440889d994096fc/scripts/test_reconcile.py#L72-L99) · [License](https://github.com/Hanyuyuan6/remote-gpu-trainer/blob/9cd83978217bd92b1e7534efa440889d994096fc/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
