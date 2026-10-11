# symphlo - Bind write permission to the inputs and effects

**Decision question:** Does an earlier approval still apply after an agent changes its plan?

| Field | Review |
| --- | --- |
| Upstream | [huisezhiyin/symphlo](https://github.com/huisezhiyin/symphlo) |
| Primary area | Agents & Decision Systems |
| Source commit | [47c4975f1689c18334ad99252a0eb575e05c7958](https://github.com/huisezhiyin/symphlo/commit/47c4975f1689c18334ad99252a0eb575e05c7958) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It hashes flow version, semantic definition, input, execution scope and required effects into a challenge; admission rejects an authorization that does not match the current challenge. The challenge is an exactness check, not independent proof of the approver's identity or that a downstream provider obeyed it. |

## What this project does

Symphlo is a durable workflow engine with explicit authorization of write effects. [README](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/README.md).

## Mechanism inspected

It hashes flow version, semantic definition, input, execution scope and required effects into a challenge; admission rejects an authorization that does not match the current challenge. [Implementation](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/effect_authorization.py#L45-L112). [Related path](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/effect_authorization.py#L116-L140).

## Limitation that matters

The challenge is an exactness check, not independent proof of the approver's identity or that a downstream provider obeyed it. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Recompute authorization after any changed plan or input and keep the approval bound to exact effects and scope.

## Why this score

A precise way to prevent stale approval reuse for agent actions, subject to separate identity and external-effect controls.

## Source trail

[README](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/README.md) - [Implementation](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/effect_authorization.py#L45-L112) - [Related path](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/src/symphlo/effect_authorization.py#L116-L140) - [License](https://github.com/huisezhiyin/symphlo/blob/47c4975f1689c18334ad99252a0eb575e05c7958/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
