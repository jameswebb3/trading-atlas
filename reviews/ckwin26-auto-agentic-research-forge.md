# Auto-Agentic-Research-Forge — Keep independent replay approval outside the agent receipt

**Decision question:** Can a self-reported third-party replay prove its own independence?

| Field | Review |
| --- | --- |
| Upstream | [CKwin26/Auto-Agentic-Research-Forge](https://github.com/CKwin26/Auto-Agentic-Research-Forge) |
| Primary area | Agents & Decision Systems |
| Source commit | [8c3a379b0ee152ec9007f84c740c0f4b25c35730](https://github.com/CKwin26/Auto-Agentic-Research-Forge/commit/8c3a379b0ee152ec9007f84c740c0f4b25c35730) |
| Reviewed | 2026-10-09 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Verification compares package digest, frozen numerical expectations and verdict; validates an Ed25519 signature against a trusted key; and still requires explicit human approval of operator independence. No root license was found at the inspected commit. The signature proves possession of a trusted key, while the operational-independence fields are declarations; the human approval remains essential. |

## What this project does

Research workflow with a signed external replay receipt and a separate identity-approval decision. [README](https://github.com/CKwin26/Auto-Agentic-Research-Forge/blob/8c3a379b0ee152ec9007f84c740c0f4b25c35730/README.md).

## Mechanism inspected

Verification compares package digest, frozen numerical expectations and verdict; validates an Ed25519 signature against a trusted key; and still requires explicit human approval of operator independence. [Implementation](https://github.com/CKwin26/Auto-Agentic-Research-Forge/blob/8c3a379b0ee152ec9007f84c740c0f4b25c35730/research_forge/independent_replay_receipt.py#L107-L215).

## Limitation that matters

No root license was found at the inspected commit. The signature proves possession of a trusted key, while the operational-independence fields are declarations; the human approval remains essential. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For high-stakes agent findings, separate reproducible package checks from independent-operator authorization and never let the replay receipt grant its own independence.

## Why this score

Verification compares package digest, frozen numerical expectations and verdict; validates an Ed25519 signature against a trusted key; and still requires explicit human approval of operator independence. No root license was found at the inspected commit. The signature proves possession of a trusted key, while the operational-independence fields are declarations; the human approval remains essential.

## Source trail

[README](https://github.com/CKwin26/Auto-Agentic-Research-Forge/blob/8c3a379b0ee152ec9007f84c740c0f4b25c35730/README.md) · [Implementation](https://github.com/CKwin26/Auto-Agentic-Research-Forge/blob/8c3a379b0ee152ec9007f84c740c0f4b25c35730/research_forge/independent_replay_receipt.py#L107-L215).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
