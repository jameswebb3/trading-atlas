# algotrading — An accepted order can be reported as failure

**Decision question:** Can a buy function distinguish an unfilled order from a failed submission?

| Field | Review |
| --- | --- |
| Upstream | [ivopetiz/algotrading](https://github.com/ivopetiz/algotrading) |
| Primary area | Execution & Exchange Integration |
| Source commit | [73ce60420bd1266c61ab4d25ae260100bd20e0c7](https://github.com/ivopetiz/algotrading/commit/73ce60420bd1266c61ab4d25ae260100bd20e0c7) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/ivopetiz/algotrading/blob/73ce60420bd1266c61ab4d25ae260100bd20e0c7/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | The buy path sizes from available plus pending balance, then returns success only when the immediate response status is `FILLED`. An accepted open or partly filled order returns false in this path; the example is spot-oriented and cannot establish HL perpetual reconciliation. |

## What this project does

Python crypto bot framework with live, tick and backtest modes. [README](https://github.com/ivopetiz/algotrading/blob/73ce60420bd1266c61ab4d25ae260100bd20e0c7/README.md).

## Mechanism inspected

The buy path sizes from available plus pending balance, then returns success only when the immediate response status is `FILLED`. [Implementation](https://github.com/ivopetiz/algotrading/blob/73ce60420bd1266c61ab4d25ae260100bd20e0c7/cryptoalgotrading/riskmanagement.py#L153-L194).

## Limitation that matters

An accepted open or partly filled order returns false in this path; the example is spot-oriented and cannot establish HL perpetual reconciliation. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep submission, acceptance, partial fill and final status as separate states; never retry solely because a helper returned false.

## Why this score

The buy path sizes from available plus pending balance, then returns success only when the immediate response status is `FILLED`. An accepted open or partly filled order returns false in this path; the example is spot-oriented and cannot establish HL perpetual reconciliation.

## Source trail

[README](https://github.com/ivopetiz/algotrading/blob/73ce60420bd1266c61ab4d25ae260100bd20e0c7/README.md) · [Implementation](https://github.com/ivopetiz/algotrading/blob/73ce60420bd1266c61ab4d25ae260100bd20e0c7/cryptoalgotrading/riskmanagement.py#L153-L194) · [License](https://github.com/ivopetiz/algotrading/blob/73ce60420bd1266c61ab4d25ae260100bd20e0c7/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
