# paper-machine - Which paper checks should block an automated report?

**Decision question:** Which paper checks should block an automated report?

| Field | Review |
| --- | --- |
| Upstream | [JihaoXin/paper-machine](https://github.com/JihaoXin/paper-machine) |
| Primary area | Agents & Decision Systems |
| Source commit | [f3b874b9d21b5f61da56aa2c4c89c5b6f5a5c176](https://github.com/JihaoXin/paper-machine/commit/f3b874b9d21b5f61da56aa2c4c89c5b6f5a5c176) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its verifier distinguishes PASS, FAIL, WARN and SKIP for PDF, references and numeric evidence tags. Unresolved references or missing optional checks can degrade to warnings or skips, leaving report credibility to a later reviewer. |

## What this project does

An agent-assisted scientific writing workflow.

## Mechanism inspected

Its verifier distinguishes PASS, FAIL, WARN and SKIP for PDF, references and numeric evidence tags.

## Limitation that matters

Unresolved references or missing optional checks can degrade to warnings or skips, leaving report credibility to a later reviewer.

## Practical check for a trading system

Make missing source evidence a blocking failure for trading-study conclusions.

## Why this score

2/5. The check taxonomy is useful, but warning policy must match decision risk.

## Source trail

[README](https://github.com/JihaoXin/paper-machine/blob/f3b874b9d21b5f61da56aa2c4c89c5b6f5a5c176/README.md#L1); [scripts/verify_paper.py](https://github.com/JihaoXin/paper-machine/blob/f3b874b9d21b5f61da56aa2c4c89c5b6f5a5c176/scripts/verify_paper.py#L184); [Root license](https://github.com/JihaoXin/paper-machine/blob/f3b874b9d21b5f61da56aa2c4c89c5b6f5a5c176/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
