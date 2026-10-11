# peregrine — Arbitrage edges need venue costs

**Decision question:** Does a cross-exchange path include its trading fee?

| Field | Review |
| --- | --- |
| Upstream | [peregrine](https://github.com/wardbradt/peregrine) |
| Primary area | Signals & Models |
| Source commit | [685c60237926e54181866cd0ded8c4199a3c6fa2](https://github.com/wardbradt/peregrine/commit/685c60237926e54181866cd0ded8c4199a3c6fa2) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/wardbradt/peregrine/blob/685c60237926e54181866cd0ded8c4199a3c6fa2/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The graph builder can weight exchange edges with trading fees when requested. The opportunity requires multiple venues and spot pairs; it cannot become a Hyperliquid USDC-perp signal by changing a symbol name. |

## What this project does

A 2017 proof-of-concept for cross-exchange crypto arbitrage; its README explicitly says the maintainer lacks capacity to maintain it. [README](https://github.com/wardbradt/peregrine/blob/685c60237926e54181866cd0ded8c4199a3c6fa2/README.md).

## Mechanism inspected

The graph builder can weight exchange edges with trading fees when requested. [Implementation](https://github.com/wardbradt/peregrine/blob/685c60237926e54181866cd0ded8c4199a3c6fa2/peregrinearb/utils/multi_exchange.py#L47-L84).

## Limitation that matters

The opportunity requires multiple venues and spot pairs; it cannot become a Hyperliquid USDC-perp signal by changing a symbol name. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Retain the fee-inclusive graph as a cautionary example, not an alpha candidate.

## Why this score

Indirect relevance only: The graph builder can weight exchange edges with trading fees when requested. The opportunity requires multiple venues and spot pairs; it cannot become a Hyperliquid USDC-perp signal by changing a symbol name.

## Source trail

[README](https://github.com/wardbradt/peregrine/blob/685c60237926e54181866cd0ded8c4199a3c6fa2/README.md) · [Implementation](https://github.com/wardbradt/peregrine/blob/685c60237926e54181866cd0ded8c4199a3c6fa2/peregrinearb/utils/multi_exchange.py#L47-L84).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
