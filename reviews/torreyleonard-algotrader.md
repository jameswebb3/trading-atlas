# algotrader — Broker acceptance is marked as executed

**Decision question:** Can a submitted order be mistaken for a completed fill?

| Field | Review |
| --- | --- |
| Upstream | [torreyleonard/algotrader](https://github.com/torreyleonard/algotrader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [7197f722939d14676147c0fac076b83a08a397a2](https://github.com/torreyleonard/algotrader/commit/7197f722939d14676147c0fac076b83a08a397a2) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/torreyleonard/algotrader/blob/7197f722939d14676147c0fac076b83a08a397a2/LICENSE.md)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | On a successful POST response, submit sets executed=true and resolves the order object. The flag names broker acceptance as execution without inspecting subsequent fills, cancellations or partials; its Robinhood semantics do not match Hyperliquid. |

## What this project does

Node.js stock and option broker wrapper with a Robinhood order adapter. [README](https://github.com/torreyleonard/algotrader/blob/7197f722939d14676147c0fac076b83a08a397a2/README.md).

## Mechanism inspected

On a successful POST response, submit sets executed=true and resolves the order object. [Implementation](https://github.com/torreyleonard/algotrader/blob/7197f722939d14676147c0fac076b83a08a397a2/objects/broker/robinhood/Order.js#L76-L117).

## Limitation that matters

The flag names broker acceptance as execution without inspecting subsequent fills, cancellations or partials; its Robinhood semantics do not match Hyperliquid. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep submitted, acknowledged, partially filled and terminal states separate in any adapter or operator display.

## Why this score

On a successful POST response, submit sets executed=true and resolves the order object. The flag names broker acceptance as execution without inspecting subsequent fills, cancellations or partials; its Robinhood semantics do not match Hyperliquid.

## Source trail

[README](https://github.com/torreyleonard/algotrader/blob/7197f722939d14676147c0fac076b83a08a397a2/README.md) · [Implementation](https://github.com/torreyleonard/algotrader/blob/7197f722939d14676147c0fac076b83a08a397a2/objects/broker/robinhood/Order.js#L76-L117) · [License](https://github.com/torreyleonard/algotrader/blob/7197f722939d14676147c0fac076b83a08a397a2/LICENSE.md).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
