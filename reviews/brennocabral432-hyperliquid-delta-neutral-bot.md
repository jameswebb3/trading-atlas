# hyperliquid-delta-neutral-bot — A delta-neutral label does not create paired hedges

**Decision question:** Does the strategy construct both legs needed for its neutral claim?

| Field | Review |
| --- | --- |
| Upstream | [brennocabral432/hyperliquid-delta-neutral-bot](https://github.com/brennocabral432/hyperliquid-delta-neutral-bot) |
| Primary area | Portfolio & Risk |
| Source commit | [f341f656f2e755abc6187dd2a879a478cebb6a11](https://github.com/brennocabral432/hyperliquid-delta-neutral-bot/commit/f341f656f2e755abc6187dd2a879a478cebb6a11) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/brennocabral432/hyperliquid-delta-neutral-bot/blob/f341f656f2e755abc6187dd2a879a478cebb6a11/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | `on_tick` reads an in-memory net-delta value and `build_orders` emits a single order in the configured coin when the value crosses a band. The inspected path neither derives net delta from positions nor creates paired legs; its README's performance table is not substantiated by this code. |

## What this project does

Hyperliquid bot presented as a delta-neutral hedging strategy. [README](https://github.com/brennocabral432/hyperliquid-delta-neutral-bot/blob/f341f656f2e755abc6187dd2a879a478cebb6a11/README.md).

## Mechanism inspected

`on_tick` reads an in-memory net-delta value and `build_orders` emits a single order in the configured coin when the value crosses a band. [Implementation](https://github.com/brennocabral432/hyperliquid-delta-neutral-bot/blob/f341f656f2e755abc6187dd2a879a478cebb6a11/src/hyperliquid_bot/strategy.py#L7-L26).

## Limitation that matters

The inspected path neither derives net delta from positions nor creates paired legs; its README's performance table is not substantiated by this code. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Require a source-linked position calculation, both hedge legs and fill accounting before considering a neutrality claim.

## Why this score

`on_tick` reads an in-memory net-delta value and `build_orders` emits a single order in the configured coin when the value crosses a band. The inspected path neither derives net delta from positions nor creates paired legs; its README's performance table is not substantiated by this code.

## Source trail

[README](https://github.com/brennocabral432/hyperliquid-delta-neutral-bot/blob/f341f656f2e755abc6187dd2a879a478cebb6a11/README.md) · [Implementation](https://github.com/brennocabral432/hyperliquid-delta-neutral-bot/blob/f341f656f2e755abc6187dd2a879a478cebb6a11/src/hyperliquid_bot/strategy.py#L7-L26) · [License](https://github.com/brennocabral432/hyperliquid-delta-neutral-bot/blob/f341f656f2e755abc6187dd2a879a478cebb6a11/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
