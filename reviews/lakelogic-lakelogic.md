# LakeLogic — Keep model advice below deterministic gates

**Decision question:** Can an LLM’s contract review block a dataset by itself?

| Field | Review |
| --- | --- |
| Upstream | [LakeLogic/LakeLogic](https://github.com/LakeLogic/LakeLogic) |
| Primary area | Agents & Decision Systems |
| Source commit | [c9ee01e035a31a2b71936064ae10592bf9f79d70](https://github.com/LakeLogic/LakeLogic/commit/c9ee01e035a31a2b71936064ae10592bf9f79d70) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/LakeLogic/LakeLogic/blob/c9ee01e035a31a2b71936064ae10592bf9f79d70/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The reviewer clamps model findings to info or warning, marks their source as LLM, and returns no findings on missing credentials or provider failure; rule-based lint remains separate. Skipping the advisory layer can hide useful warnings, and the source does not prove the model’s semantic findings are accurate; it must not be treated as a data-quality verdict. |

## What this project does

Data-contract platform with deterministic lint and an optional LLM reviewer for semantic gaps. [README](https://github.com/LakeLogic/LakeLogic/blob/c9ee01e035a31a2b71936064ae10592bf9f79d70/README.md).

## Mechanism inspected

The reviewer clamps model findings to info or warning, marks their source as LLM, and returns no findings on missing credentials or provider failure; rule-based lint remains separate. [Implementation](https://github.com/LakeLogic/LakeLogic/blob/c9ee01e035a31a2b71936064ae10592bf9f79d70/lakelogic/ai/contract_judge.py#L100-L160).

## Limitation that matters

Skipping the advisory layer can hide useful warnings, and the source does not prove the model’s semantic findings are accurate; it must not be treated as a data-quality verdict. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Let research agents suggest missing checks, but require deterministic validation and a human-reviewed promotion step before any suggestion blocks or approves a trading dataset.

## Why this score

The reviewer clamps model findings to info or warning, marks their source as LLM, and returns no findings on missing credentials or provider failure; rule-based lint remains separate. Skipping the advisory layer can hide useful warnings, and the source does not prove the model’s semantic findings are accurate; it must not be treated as a data-quality verdict.

## Source trail

[README](https://github.com/LakeLogic/LakeLogic/blob/c9ee01e035a31a2b71936064ae10592bf9f79d70/README.md) · [Implementation](https://github.com/LakeLogic/LakeLogic/blob/c9ee01e035a31a2b71936064ae10592bf9f79d70/lakelogic/ai/contract_judge.py#L100-L160) · [License](https://github.com/LakeLogic/LakeLogic/blob/c9ee01e035a31a2b71936064ae10592bf9f79d70/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
