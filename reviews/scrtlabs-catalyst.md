# Catalyst — Check the clock before reusing a backtester

**Decision question:** Does a session-based crypto backtester model a 24/7 perpetual market?

| Field | Review |
| --- | --- |
| Upstream | [scrtlabs/catalyst](https://github.com/scrtlabs/catalyst) |
| Primary area | Signals & Models |
| Source commit | [2e8029780f2381da7a0729f7b52505e5db5f535b](https://github.com/scrtlabs/catalyst/commit/2e8029780f2381da7a0729f7b52505e5db5f535b) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/scrtlabs/catalyst/blob/2e8029780f2381da7a0729f7b52505e5db5f535b/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The algorithm constructs its event clock from a trading calendar, opens, and closes; daily mode emits one bar at the session close. A session calendar and legacy exchange adapters do not by themselves model continuous perps, funding, exchange-specific order states, or realistic queue fills. |

## What this project does

A Zipline-derived Python framework for crypto backtests at daily or minute frequency. [Project README](https://github.com/scrtlabs/catalyst/blob/2e8029780f2381da7a0729f7b52505e5db5f535b/README.rst#L26).

## Mechanism inspected

The algorithm constructs its event clock from a trading calendar, opens, and closes; daily mode emits one bar at the session close. [Implementation](https://github.com/scrtlabs/catalyst/blob/2e8029780f2381da7a0729f7b52505e5db5f535b/catalyst/algorithm.py#L514). [Related source 1](https://github.com/scrtlabs/catalyst/blob/2e8029780f2381da7a0729f7b52505e5db5f535b/README.rst#L54).

## Limitation that matters

A session calendar and legacy exchange adapters do not by themselves model continuous perps, funding, exchange-specific order states, or realistic queue fills. This is a source review, not a runtime or security test.

## Practical check for a trading system

Verify the market clock, funding events, and fill model before adapting a backtest to a perpetual venue.

## Why this score

Its clock construction is a useful reference, but the venue and product assumptions are materially different from modern perpetual execution.

## Source trail

[README](https://github.com/scrtlabs/catalyst/blob/2e8029780f2381da7a0729f7b52505e5db5f535b/README.rst#L26); [Implementation](https://github.com/scrtlabs/catalyst/blob/2e8029780f2381da7a0729f7b52505e5db5f535b/catalyst/algorithm.py#L514); [Related source 1](https://github.com/scrtlabs/catalyst/blob/2e8029780f2381da7a0729f7b52505e5db5f535b/README.rst#L54) - [License](https://github.com/scrtlabs/catalyst/blob/2e8029780f2381da7a0729f7b52505e5db5f535b/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
