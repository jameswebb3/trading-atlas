# Trade-Bot-Hyperliquid - Can public fills alone verify a trader equity curve?

**Decision question:** Can public fills alone verify a trader equity curve?

| Field | Review |
| --- | --- |
| Upstream | [sonicmountain/Trade-Bot-Hyperliquid](https://github.com/sonicmountain/Trade-Bot-Hyperliquid) |
| Primary area | Portfolio & Risk |
| Source commit | [db92e28020726748819e2bced158546aa5c57471](https://github.com/sonicmountain/Trade-Bot-Hyperliquid/commit/db92e28020726748819e2bced158546aa5c57471) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Replays Hyperliquid fills into risk diagnostics. Funding direction and fee-adjusted win-rate semantics are not faithfully reconstructed. |

## What this project does

A read-only Hyperliquid account analysis tool that replays fills and reports drawdown, return and concentration diagnostics.

## Mechanism inspected

Its verifier walks fills, closes exposure against stored legs, subtracts fees, and derives drawdown and outlier concentration from a normalized equity curve.

## Limitation that matters

The replay uses weighted-average additions but FIFO reductions. Funding is estimated from the absolute average historical rate at each fill, which cannot reproduce signed funding cash flows. Its fee-adjusted win-rate field is identical to the already fee-net win rate.

## Practical check for a trading system

Use the checks as a prompt to reconcile actual position, fee and funding ledgers before calling an account return verified.

## Why this score

2/5. Direct account-risk questions are covered, but several accounting approximations make the reported verification weaker than its label.

## Source trail

[README](https://github.com/sonicmountain/Trade-Bot-Hyperliquid/blob/db92e28020726748819e2bced158546aa5c57471/README.md#L22); [hl_trade_bot/core/verifier.py](https://github.com/sonicmountain/Trade-Bot-Hyperliquid/blob/db92e28020726748819e2bced158546aa5c57471/hl_trade_bot/core/verifier.py#L136); [hl_trade_bot/core/verifier.py](https://github.com/sonicmountain/Trade-Bot-Hyperliquid/blob/db92e28020726748819e2bced158546aa5c57471/hl_trade_bot/core/verifier.py#L185); [hl_trade_bot/core/verifier.py](https://github.com/sonicmountain/Trade-Bot-Hyperliquid/blob/db92e28020726748819e2bced158546aa5c57471/hl_trade_bot/core/verifier.py#L220); [License text](https://github.com/sonicmountain/Trade-Bot-Hyperliquid/blob/db92e28020726748819e2bced158546aa5c57471/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
