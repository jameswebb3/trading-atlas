# Freqtrade Ultimate — Wallet netting needs order ownership

**Decision question:** How do several bots avoid cancelling one another’s Hyperliquid orders?

| Field | Review |
| --- | --- |
| Upstream | [titouannwtt/freqtrade-ultimate](https://github.com/titouannwtt/freqtrade-ultimate) |
| Primary area | Execution & Exchange Integration |
| Source commit | [4dc76a642afbe39da83abfec319822818cf45ac8](https://github.com/titouannwtt/freqtrade-ultimate/commit/4dc76a642afbe39da83abfec319822818cf45ac8) |
| Reviewed | 2026-10-10 |
| Declared license | GPL-3.0 ([source](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | A stable fingerprint tags bot-owned client IDs; reconciliation groups positions by wallet and coin and skips wallets whose net state could not be fetched. A fingerprint does not solve ambiguous fills or make a shared wallet safe by itself. |

## What this project does

A Hyperliquid-oriented Freqtrade fork with multiple bots sharing a wallet and a netting reconciler. [Project README](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/README.md#L33).

## Mechanism inspected

A stable fingerprint tags bot-owned client IDs; reconciliation groups positions by wallet and coin and skips wallets whose net state could not be fetched. [Implementation](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/freqtrade/order_identity.py#L61). [Related source 1](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/.claude-tips/data_quality.md#L3). [Related source 2](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/user_data/netting_reconciler.py#L304).

## Limitation that matters

A fingerprint does not solve ambiguous fills or make a shared wallet safe by itself. The large fork and bundled history add substantial operational weight. This is a source review, not a runtime or security test.

## Practical check for a trading system

Classify each unmatched order as owned, external, or unknown before any automatic cancellation.

## Why this score

Its ownership and unknown-wallet handling directly address live order safety, but adopting the fork would be disproportionate.

## Source trail

[README](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/README.md#L33); [Implementation](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/freqtrade/order_identity.py#L61); [Related source 1](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/.claude-tips/data_quality.md#L3); [Related source 2](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/user_data/netting_reconciler.py#L304) - [License](https://github.com/titouannwtt/freqtrade-ultimate/blob/4dc76a642afbe39da83abfec319822818cf45ac8/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
