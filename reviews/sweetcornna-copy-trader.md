# copy-trader — Do not mark a dry run as filled

**Decision question:** Can an order adapter report a fill that never happened?

| Field | Review |
| --- | --- |
| Upstream | [sweetcornna/copy-trader](https://github.com/sweetcornna/copy-trader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [fa7977c08defa878c24ddf51c68ed33367edfe55](https://github.com/sweetcornna/copy-trader/commit/fa7977c08defa878c24ddf51c68ed33367edfe55) |
| Reviewed | 2026-10-09 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | The adapter returns status filled with a synthetic ID when dry-run or wallet credentials are absent; for live responses it defaults to open and swallows parsing errors while examining the first nested status. A dry-run fill is not execution evidence. The inspected live path can also return open with an empty order ID when a response is malformed or unrecognized, leaving reconciliation ambiguous. |

## What this project does

Cross-venue perpetual copy-trading system with a Hyperliquid exchange adapter. [README](https://github.com/sweetcornna/copy-trader/blob/fa7977c08defa878c24ddf51c68ed33367edfe55/README.md).

## Mechanism inspected

The adapter returns status filled with a synthetic ID when dry-run or wallet credentials are absent; for live responses it defaults to open and swallows parsing errors while examining the first nested status. [Implementation](https://github.com/sweetcornna/copy-trader/blob/fa7977c08defa878c24ddf51c68ed33367edfe55/execution_engine/engine/exchanges/hyperliquid.py#L174-L232).

## Limitation that matters

A dry-run fill is not execution evidence. The inspected live path can also return open with an empty order ID when a response is malformed or unrecognized, leaving reconciliation ambiguous. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Carry simulation status separately from venue order state and require explicit response-shape validation before a live order becomes accepted or filled.

## Why this score

The adapter returns status filled with a synthetic ID when dry-run or wallet credentials are absent; for live responses it defaults to open and swallows parsing errors while examining the first nested status. A dry-run fill is not execution evidence. The inspected live path can also return open with an empty order ID when a response is malformed or unrecognized, leaving reconciliation ambiguous.

## Source trail

[README](https://github.com/sweetcornna/copy-trader/blob/fa7977c08defa878c24ddf51c68ed33367edfe55/README.md) · [Implementation](https://github.com/sweetcornna/copy-trader/blob/fa7977c08defa878c24ddf51c68ed33367edfe55/execution_engine/engine/exchanges/hyperliquid.py#L174-L232).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
