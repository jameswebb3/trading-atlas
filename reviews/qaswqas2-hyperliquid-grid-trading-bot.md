# hyperliquid-grid-trading-bot — Hold outside the grid still builds orders

**Decision question:** Does an out-of-range grid signal prevent submissions?

| Field | Review |
| --- | --- |
| Upstream | [qaswqas2/hyperliquid-grid-trading-bot](https://github.com/qaswqas2/hyperliquid-grid-trading-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [fd1c4f143156adbdfdf630b725f8cf343c743e3d](https://github.com/qaswqas2/hyperliquid-grid-trading-bot/commit/fd1c4f143156adbdfdf630b725f8cf343c743e3d) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/qaswqas2/hyperliquid-grid-trading-bot/blob/fd1c4f143156adbdfdf630b725f8cf343c743e3d/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | `on_tick` returns `hold` outside configured bounds, but `build_orders` ignores the signal and creates both sides of the ladder; the runner calls it for every risk-approved tick. The runner's risk check uses a synthetic zero-size position, so this inspected path cannot establish live exposure protection; README metrics are unsupported here. |

## What this project does

Hyperliquid grid bot with post-only ladder construction. [README](https://github.com/qaswqas2/hyperliquid-grid-trading-bot/blob/fd1c4f143156adbdfdf630b725f8cf343c743e3d/README.md).

## Mechanism inspected

`on_tick` returns `hold` outside configured bounds, but `build_orders` ignores the signal and creates both sides of the ladder; the runner calls it for every risk-approved tick. [Implementation](https://github.com/qaswqas2/hyperliquid-grid-trading-bot/blob/fd1c4f143156adbdfdf630b725f8cf343c743e3d/src/hyperliquid_bot/strategy.py#L11-L30). [Related implementation](https://github.com/qaswqas2/hyperliquid-grid-trading-bot/blob/fd1c4f143156adbdfdf630b725f8cf343c743e3d/src/hyperliquid_bot/runner.py#L41-L71).

## Limitation that matters

The runner's risk check uses a synthetic zero-size position, so this inspected path cannot establish live exposure protection; README metrics are unsupported here. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Make an out-of-range signal yield zero intents and test that the runner submits none, with position fetched from the venue.

## Why this score

`on_tick` returns `hold` outside configured bounds, but `build_orders` ignores the signal and creates both sides of the ladder; the runner calls it for every risk-approved tick. The runner's risk check uses a synthetic zero-size position, so this inspected path cannot establish live exposure protection; README metrics are unsupported here.

## Source trail

[README](https://github.com/qaswqas2/hyperliquid-grid-trading-bot/blob/fd1c4f143156adbdfdf630b725f8cf343c743e3d/README.md) · [Implementation](https://github.com/qaswqas2/hyperliquid-grid-trading-bot/blob/fd1c4f143156adbdfdf630b725f8cf343c743e3d/src/hyperliquid_bot/strategy.py#L11-L30) · [Related implementation](https://github.com/qaswqas2/hyperliquid-grid-trading-bot/blob/fd1c4f143156adbdfdf630b725f8cf343c743e3d/src/hyperliquid_bot/runner.py#L41-L71) · [License](https://github.com/qaswqas2/hyperliquid-grid-trading-bot/blob/fd1c4f143156adbdfdf630b725f8cf343c743e3d/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
