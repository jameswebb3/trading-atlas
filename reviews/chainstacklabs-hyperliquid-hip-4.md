# hyperliquid-hip-4 - A quote loop must reconcile cancel failures and timer expiry

**Decision question:** Can a sample market maker keep quoting after a missed timer and a failed cancel?

| Field | Review |
| --- | --- |
| Upstream | [chainstacklabs/hyperliquid-hip-4](https://github.com/chainstacklabs/hyperliquid-hip-4) |
| Primary area | Execution & Exchange Integration |
| Source commit | [8eb01fc8fb147c65f3eecf141095488259ad4ef8](https://github.com/chainstacklabs/hyperliquid-hip-4/commit/8eb01fc8fb147c65f3eecf141095488259ad4ef8) |
| Reviewed | 2026-10-10 |
| Declared license | No root license file found at the reviewed commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Shows inventory-capped quoting and cancel-replace mechanics for Hyperliquid HIP-4 outcome books. Cancel errors are swallowed before the tracked order is cleared, and the first normal timer timeout appears to exit the entire quote loop. |

## What this project does

Learning examples for Hyperliquid HIP-4 outcome contracts, including a passive market-maker bot. The inspected bot uses outcome books and spot-clearinghouse balances; it is not a perpetuals strategy.

## Mechanism inspected

The bot derives fair values from book midpoints, limits new buying at a side inventory cap, and replaces a resting quote when the target changes. It tracks the latest resting order ID in memory and calls cancel before submitting a replacement.

## Limitation that matters

safe_cancel catches exceptions without signaling failure, yet replace_quote clears the tracked order ID after calling it; an old live order could remain while a replacement is sent. Also, asyncio.wait_for(stop.wait(), timeout=...) is inside the loop but TimeoutError is caught outside it, so the first normal tick timeout exits the loop and triggers final cancellation. Neither path supports the continuous quoting claimed by the README. This is a source review, not a runtime or security test.

## Practical check for a trading system

For any venue, treat cancel success as an observed exchange state, reconcile open orders before replacement, and keep timer expiry inside the loop. Separate outcome-contract examples from Hyperliquid perpetuals research.

## Why this score

1/5 because its directly trading-related code exposes two consequential control-flow hazards and concerns outcome contracts rather than the perpetuals path.

## Source trail

[README](https://github.com/chainstacklabs/hyperliquid-hip-4/blob/8eb01fc8fb147c65f3eecf141095488259ad4ef8/README.md#L50); [Cancel and replace](https://github.com/chainstacklabs/hyperliquid-hip-4/blob/8eb01fc8fb147c65f3eecf141095488259ad4ef8/bot/market_maker.py#L93); [Quote loop](https://github.com/chainstacklabs/hyperliquid-hip-4/blob/8eb01fc8fb147c65f3eecf141095488259ad4ef8/bot/market_maker.py#L217); [Outcome balance](https://github.com/chainstacklabs/hyperliquid-hip-4/blob/8eb01fc8fb147c65f3eecf141095488259ad4ef8/bot/market_maker.py#L79).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
