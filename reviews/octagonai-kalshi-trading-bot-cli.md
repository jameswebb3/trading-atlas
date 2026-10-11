# kalshi-trading-bot-cli - Does a missing drawdown snapshot fail closed?

**Decision question:** Does a missing drawdown snapshot fail closed?

| Field | Review |
| --- | --- |
| Upstream | [OctagonAI/kalshi-trading-bot-cli](https://github.com/OctagonAI/kalshi-trading-bot-cli) |
| Primary area | Portfolio & Risk |
| Source commit | [fcba2ff115de7cf736b51a0b5611ee7ef709142e](https://github.com/OctagonAI/kalshi-trading-bot-cli/commit/fcba2ff115de7cf736b51a0b5611ee7ef709142e) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The gate compares the latest drawdown snapshot with the configured maximum and records a reason for each check. A null drawdown snapshot passes and the code explicitly labels first trade allowed; absence of risk evidence is treated as permission. |

## What this project does

A Kalshi trading CLI with a configurable pre-trade risk gate.

## Mechanism inspected

The gate compares the latest drawdown snapshot with the configured maximum and records a reason for each check.

## Limitation that matters

A null drawdown snapshot passes and the code explicitly labels first trade allowed; absence of risk evidence is treated as permission.

## Practical check for a trading system

Require a valid initial equity anchor or mark drawdown unknown and block live risk.

## Why this score

2/5. Its observable fail-open case is a useful negative test, not a recommended policy.

## Source trail

[README](https://github.com/OctagonAI/kalshi-trading-bot-cli/blob/fcba2ff115de7cf736b51a0b5611ee7ef709142e/README.md#L1); [src/risk/gate.ts](https://github.com/OctagonAI/kalshi-trading-bot-cli/blob/fcba2ff115de7cf736b51a0b5611ee7ef709142e/src/risk/gate.ts#L110); [Root license](https://github.com/OctagonAI/kalshi-trading-bot-cli/blob/fcba2ff115de7cf736b51a0b5611ee7ef709142e/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
