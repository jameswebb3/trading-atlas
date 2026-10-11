# autopredict - Can a release audit refuse live mode before touching an exchange?

**Decision question:** Can a release audit refuse live mode before touching an exchange?

| Field | Review |
| --- | --- |
| Upstream | [howdymary/autopredict](https://github.com/howdymary/autopredict) |
| Primary area | Testing & Verification |
| Source commit | [faab11f664c99bf339f766974eae18c2cb8c8d93](https://github.com/howdymary/autopredict/commit/faab11f664c99bf339f766974eae18c2cb8c8d93) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The audit resolves live-mode configuration, missing credentials and default neutral models without making venue calls. When no config path is supplied it reports credentials present, so the audit result needs an explicit mode and invocation contract. |

## What this project does

A prediction-market research package with a local safety audit.

## Mechanism inspected

The audit resolves live-mode configuration, missing credentials and default neutral models without making venue calls.

## Limitation that matters

When no config path is supplied it reports credentials present, so the audit result needs an explicit mode and invocation contract.

## Practical check for a trading system

Use a preflight that proves deployment mode, config identity and disabled live capability before enabling execution.

## Why this score

3/5. A read-only release gate is a useful pattern; passing must be tied to the real configuration.

## Source trail

[README](https://github.com/howdymary/autopredict/blob/faab11f664c99bf339f766974eae18c2cb8c8d93/README.md#L1); [docs/README.md](https://github.com/howdymary/autopredict/blob/faab11f664c99bf339f766974eae18c2cb8c8d93/docs/README.md#L1); [autopredict/live/safety_audit.py](https://github.com/howdymary/autopredict/blob/faab11f664c99bf339f766974eae18c2cb8c8d93/autopredict/live/safety_audit.py#L50); [Root license](https://github.com/howdymary/autopredict/blob/faab11f664c99bf339f766974eae18c2cb8c8d93/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
