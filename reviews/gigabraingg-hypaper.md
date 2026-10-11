# HyPaper - Does a paper IOC fill use executable book liquidity?

**Decision question:** Does a paper IOC fill use executable book liquidity?

| Field | Review |
| --- | --- |
| Upstream | [GigabrainGG/HyPaper](https://github.com/GigabrainGG/HyPaper) |
| Primary area | Backtesting & Simulation |
| Source commit | [b054fdd2cea7e1a9f5c5ba03f85a56d74f67f972](https://github.com/GigabrainGG/HyPaper/commit/b054fdd2cea7e1a9f5c5ba03f85a56d74f67f972) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | For IOC orders it checks the mid against the limit, saves the order and executes a full fill at a computed price. A mid-price crossing does not prove executable depth, queue position or a partial-fill quantity. |

## What this project does

A Hyperliquid-shaped paper trading engine with order and margin handling.

## Mechanism inspected

For IOC orders it checks the mid against the limit, saves the order and executes a full fill at a computed price.

## Limitation that matters

A mid-price crossing does not prove executable depth, queue position or a partial-fill quantity.

## Practical check for a trading system

Label paper fills as assumptions and compare them with raw book depth before using paper P&L for sizing.

## Why this score

3/5. The order path is concrete; its fill evidence is much thinner than an exchange execution.

## Source trail

[README](https://github.com/GigabrainGG/HyPaper/blob/b054fdd2cea7e1a9f5c5ba03f85a56d74f67f972/README.md#L1); [src/engine/order.ts](https://github.com/GigabrainGG/HyPaper/blob/b054fdd2cea7e1a9f5c5ba03f85a56d74f67f972/src/engine/order.ts#L75); [src/engine/order.ts](https://github.com/GigabrainGG/HyPaper/blob/b054fdd2cea7e1a9f5c5ba03f85a56d74f67f972/src/engine/order.ts#L78); [Root license](https://github.com/GigabrainGG/HyPaper/blob/b054fdd2cea7e1a9f5c5ba03f85a56d74f67f972/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
