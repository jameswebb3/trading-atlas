# Alpaca scalping example — Restart state inferred from orders and positions

**Decision question:** Can a bot rebuild intent after restart from current orders and positions?

| Field | Review |
| --- | --- |
| Upstream | [Alpaca scalping example](https://github.com/alpacahq/example-scalping) |
| Primary area | Execution & Exchange Integration |
| Source commit | [4d0962785e272a01fcb4c89f0e961264e9a91827](https://github.com/alpacahq/example-scalping/commit/4d0962785e272a01fcb4c89f0e961264e9a91827) |
| Reviewed | 2026-10-06 |
| Declared license | No root license file found |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | At initialization it queries current orders and positions, chooses a buy or sell state and logs when order side conflicts with inferred state. It chooses the first matching order and merely warns on a mismatch; current snapshots alone do not reconstruct fills or earlier intent. |

## What this project does

A compact asynchronous equity scalping example that combines order updates and minute bars. [README](https://github.com/alpacahq/example-scalping/blob/4d0962785e272a01fcb4c89f0e961264e9a91827/README.md).

## Mechanism inspected

At initialization it queries current orders and positions, chooses a buy or sell state and logs when order side conflicts with inferred state. [Implementation](https://github.com/alpacahq/example-scalping/blob/4d0962785e272a01fcb4c89f0e961264e9a91827/main.py#L45-L67).

## Limitation that matters

It chooses the first matching order and merely warns on a mismatch; current snapshots alone do not reconstruct fills or earlier intent. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Use as a negative restart fixture: two open orders or side mismatch must not silently choose a strategy state.

## Why this score

Direct trading-system relevance: At initialization it queries current orders and positions, chooses a buy or sell state and logs when order side conflicts with inferred state. It chooses the first matching order and merely warns on a mismatch; current snapshots alone do not reconstruct fills or earlier intent.

## Source trail

[README](https://github.com/alpacahq/example-scalping/blob/4d0962785e272a01fcb4c89f0e961264e9a91827/README.md) · [Implementation](https://github.com/alpacahq/example-scalping/blob/4d0962785e272a01fcb4c89f0e961264e9a91827/main.py#L45-L67).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
