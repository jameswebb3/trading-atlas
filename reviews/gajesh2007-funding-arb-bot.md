# funding-arb-bot - Does cross-venue risk require margin evidence on both legs?

**Decision question:** Does cross-venue risk require margin evidence on both legs?

| Field | Review |
| --- | --- |
| Upstream | [Gajesh2007/funding-arb-bot](https://github.com/Gajesh2007/funding-arb-bot) |
| Primary area | Portfolio & Risk |
| Source commit | [9b016c5aa004ea8e2824d28e3c9cc1197f3e2ae7](https://github.com/Gajesh2007/funding-arb-bot/commit/9b016c5aa004ea8e2824d28e3c9cc1197f3e2ae7) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | It checks free margin on each venue with a safety factor and rejects on exchange-state errors. The hedge adds another venue and basis risk; this is not a single-venue perpetual strategy. |

## What this project does

A funding-arbitrage bot spanning Hyperliquid and Lighter.

## Mechanism inspected

It checks free margin on each venue with a safety factor and rejects on exchange-state errors.

## Limitation that matters

The hedge adds another venue and basis risk; this is not a single-venue perpetual strategy.

## Practical check for a trading system

Apply fail-closed account-state checks to each live order, even without a hedge.

## Why this score

3/5. Relevant live-money gate, with different strategy scope.

## Source trail

[README](https://github.com/Gajesh2007/funding-arb-bot/blob/9b016c5aa004ea8e2824d28e3c9cc1197f3e2ae7/README.md#L1); [src/execution/risk.ts](https://github.com/Gajesh2007/funding-arb-bot/blob/9b016c5aa004ea8e2824d28e3c9cc1197f3e2ae7/src/execution/risk.ts#L368).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
