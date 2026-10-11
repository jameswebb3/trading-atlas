# predmarket-arb - Will a control acknowledgement look like a missing order-book delta?

**Decision question:** Will a control acknowledgement look like a missing order-book delta?

| Field | Review |
| --- | --- |
| Upstream | [cyriljoby/predmarket-arb](https://github.com/cyriljoby/predmarket-arb) |
| Primary area | Market Data & Ingestion |
| Source commit | [9d344036941468e3578925fa3c344491adb343fe](https://github.com/cyriljoby/predmarket-arb/commit/9d344036941468e3578925fa3c344491adb343fe) |
| Reviewed | 2026-10-11 |
| Declared license | No root license file found at the reviewed commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Tracks Kalshi sequence numbers across control and book frames, then reconnects for a fresh snapshot on a true gap. A stream gap invalidates local book state; the replayed opportunity window still cannot prove two-leg fills. |

## What this project does

An event-driven Kalshi and Polymarket arbitrage research stack with live books, opportunity logs and replay analysis.

## Mechanism inspected

The Kalshi stream advances its subscription sequence on every frame that carries seq, including control acknowledgements, before filtering to book snapshots and deltas. A real sequence gap breaks the stream so reconnect can obtain fresh snapshots; the backtest labels survival windows without a later observation as censored.

## Limitation that matters

The sequence counter only protects messages on this subscription. A reconstructed local book still depends on a valid initial snapshot and the exchange transport; the opportunity-survival report is observational, not a two-leg execution fill study. The inspected root has no license file.

## Practical check for a trading system

For incremental books, account for all numbered control frames, invalidate local state on gaps, and keep unknown survival outcomes separate from failures.

## Why this score

4/5 because The code addresses a direct feed-integrity error and makes reconnection explicit, with clear boundaries around execution and licensing.

## Source trail

[README stream design](https://github.com/cyriljoby/predmarket-arb/blob/9d344036941468e3578925fa3c344491adb343fe/README.md#L52); [Control-frame sequence and gap](https://github.com/cyriljoby/predmarket-arb/blob/9d344036941468e3578925fa3c344491adb343fe/pmarb/feeds/kalshi.py#L574); [Snapshot replacement and delta](https://github.com/cyriljoby/predmarket-arb/blob/9d344036941468e3578925fa3c344491adb343fe/pmarb/feeds/kalshi.py#L603); [Censored survival](https://github.com/cyriljoby/predmarket-arb/blob/9d344036941468e3578925fa3c344491adb343fe/pmarb/backtest/survival.py#L100).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
