# kalshi-poly-arb - Does a partial hedge retain its orphan state until resolved?

**Decision question:** Does a partial hedge retain its orphan state until resolved?

| Field | Review |
| --- | --- |
| Upstream | [juanjo1997/kalshi-poly-arb](https://github.com/juanjo1997/kalshi-poly-arb) |
| Primary area | Execution & Exchange Integration |
| Source commit | [a1d27c6f6e620edbfacc2fcef7dc33da16529f86](https://github.com/juanjo1997/kalshi-poly-arb/commit/a1d27c6f6e620edbfacc2fcef7dc33da16529f86) |
| Reviewed | 2026-10-11 |
| Declared license | No root license file found at the reviewed commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Calculates a remaining hedge after partial fills, but one no-hedge branch overwrites Orphan with Idle immediately. Verify durable account reconciliation before treating the local Idle state as proof of a closed hedge. |

## What this project does

A Rust cross-venue Kalshi and Polymarket arbitrage engine with IOC and maker paths, hedging retries, cooldowns and risk limits.

## Mechanism inspected

After immediate execution feedback, the engine computes remaining hedge quantity from requested minus reported filled size and starts a persistent hedge only when the first leg has a transaction hash and quantity remains. The maker path separately records matched size as the minimum of both legs.

## Limitation that matters

On the branch where persistent hedging does not start after a Kalshi failure or partial fill, the code inserts an Orphan state and then immediately overwrites it with Idle. This inspected in-memory transition cannot itself preserve an orphan marker; persistence and later recovery elsewhere were not established. No root license file was found.

## Practical check for a trading system

Treat every one-leg or partial-fill result as unresolved until account-side evidence closes it; test the no-hedge transition and restart recovery before copying this design.

## Why this score

2/5 because Remaining-quantity arithmetic is directly relevant, but the visible orphan-to-idle overwrite is a consequential control-path concern and licensing is unclear.

## Source trail

[README partial-fill claims](https://github.com/juanjo1997/kalshi-poly-arb/blob/a1d27c6f6e620edbfacc2fcef7dc33da16529f86/README.md#L46); [Remaining quantity and orphan transition](https://github.com/juanjo1997/kalshi-poly-arb/blob/a1d27c6f6e620edbfacc2fcef7dc33da16529f86/src/engine.rs#L887); [Maker matched quantity](https://github.com/juanjo1997/kalshi-poly-arb/blob/a1d27c6f6e620edbfacc2fcef7dc33da16529f86/src/maker_engine.rs#L1652).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
