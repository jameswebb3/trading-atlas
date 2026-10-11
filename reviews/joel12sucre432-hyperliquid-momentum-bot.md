# hyperliquid-momentum-bot — An EMA direction is not an EMA-cross event

**Decision question:** What signal does the Hyperliquid momentum bot actually emit?

| Field | Review |
| --- | --- |
| Upstream | [Joel12Sucre432/hyperliquid-momentum-bot](https://github.com/Joel12Sucre432/hyperliquid-momentum-bot) |
| Primary area | Signals & Models |
| Source commit | [d2168e3b8154bb1114bc1cbb187feab685b2ff16](https://github.com/Joel12Sucre432/hyperliquid-momentum-bot/commit/d2168e3b8154bb1114bc1cbb187feab685b2ff16) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/Joel12Sucre432/hyperliquid-momentum-bot/blob/d2168e3b8154bb1114bc1cbb187feab685b2ff16/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | It calculates fast and slow EMAs from recent closes and emits long whenever fast exceeds slow, short when below; there is no prior-state crossing condition in this function. The source does not show a closed-candle filter or independent return evidence for the README's performance table; it can repeat the same direction every tick. |

## What this project does

HL bot advertised as an EMA-cross momentum strategy. [README](https://github.com/Joel12Sucre432/hyperliquid-momentum-bot/blob/d2168e3b8154bb1114bc1cbb187feab685b2ff16/README.md).

## Mechanism inspected

It calculates fast and slow EMAs from recent closes and emits long whenever fast exceeds slow, short when below; there is no prior-state crossing condition in this function. [Implementation](https://github.com/Joel12Sucre432/hyperliquid-momentum-bot/blob/d2168e3b8154bb1114bc1cbb187feab685b2ff16/src/hyperliquid_bot/strategy.py#L12-L40).

## Limitation that matters

The source does not show a closed-candle filter or independent return evidence for the README's performance table; it can repeat the same direction every tick. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Separate a crossing event from persistent trend state and require finalized candles before alpha preregistration.

## Why this score

It calculates fast and slow EMAs from recent closes and emits long whenever fast exceeds slow, short when below; there is no prior-state crossing condition in this function. The source does not show a closed-candle filter or independent return evidence for the README's performance table; it can repeat the same direction every tick.

## Source trail

[README](https://github.com/Joel12Sucre432/hyperliquid-momentum-bot/blob/d2168e3b8154bb1114bc1cbb187feab685b2ff16/README.md) · [Implementation](https://github.com/Joel12Sucre432/hyperliquid-momentum-bot/blob/d2168e3b8154bb1114bc1cbb187feab685b2ff16/src/hyperliquid_bot/strategy.py#L12-L40) · [License](https://github.com/Joel12Sucre432/hyperliquid-momentum-bot/blob/d2168e3b8154bb1114bc1cbb187feab685b2ff16/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
