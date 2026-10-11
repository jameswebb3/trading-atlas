# MATS — Guard the verdict, distrust the retrospective uplift

**Decision question:** When should an experiment engine refuse to declare a winner?

| Field | Review |
| --- | --- |
| Upstream | [wyc-dev/MATS](https://github.com/wyc-dev/MATS) |
| Primary area | Execution & Exchange Integration |
| Source commit | [d76d63399e7086235cf7297afc897be7da80beb4](https://github.com/wyc-dev/MATS/commit/d76d63399e7086235cf7297afc897be7da80beb4) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/wyc-dev/MATS/blob/d76d63399e7086235cf7297afc897be7da80beb4/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The verdict function returns INSUFFICIENT for non-finite metrics, absent thresholds, or inadequate samples. Its separate retrospective report selects changes on the same observed 455 trades; that uplift is not independent out-of-sample evidence for the proposed strategy. |

## What this project does

A Hyperliquid trading agent with experiment records and automated verdict logic. [Project README](https://github.com/wyc-dev/MATS/blob/d76d63399e7086235cf7297afc897be7da80beb4/README.md#L17).

## Mechanism inspected

The verdict function returns INSUFFICIENT for non-finite metrics, absent thresholds, or inadequate samples. [Implementation](https://github.com/wyc-dev/MATS/blob/d76d63399e7086235cf7297afc897be7da80beb4/src/research/verdict-engine.ts#L42). [Related source 1](https://github.com/wyc-dev/MATS/blob/d76d63399e7086235cf7297afc897be7da80beb4/docs/P70-VERIFICATION-REPORT.md#L10).

## Limitation that matters

Its separate retrospective report selects changes on the same observed 455 trades; that uplift is not independent out-of-sample evidence for the proposed strategy. This is a source review, not a runtime or security test.

## Practical check for a trading system

Keep pre-registered gates and reject non-finite inputs; require untouched future data for any claimed improvement.

## Why this score

The verdict guard is useful, but the trading performance claims need stronger causal evidence.

## Source trail

[README](https://github.com/wyc-dev/MATS/blob/d76d63399e7086235cf7297afc897be7da80beb4/README.md#L17); [Implementation](https://github.com/wyc-dev/MATS/blob/d76d63399e7086235cf7297afc897be7da80beb4/src/research/verdict-engine.ts#L42); [Related source 1](https://github.com/wyc-dev/MATS/blob/d76d63399e7086235cf7297afc897be7da80beb4/docs/P70-VERIFICATION-REPORT.md#L10) - [License](https://github.com/wyc-dev/MATS/blob/d76d63399e7086235cf7297afc897be7da80beb4/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
