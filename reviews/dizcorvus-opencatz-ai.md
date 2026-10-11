# opencatz-ai - An empty account can mean a failed request

**Decision question:** Does an empty position response prove that the account is flat?

| Field | Review |
| --- | --- |
| Upstream | [dizcorvus/opencatz-ai](https://github.com/dizcorvus/opencatz-ai) |
| Primary area | Execution & Exchange Integration |
| Source commit | [9cb31e0b6908a7bccb448e77b040a38a949b98d1](https://github.com/dizcorvus/opencatz-ai/commit/9cb31e0b6908a7bccb448e77b040a38a949b98d1) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/dizcorvus/opencatz-ai/blob/9cb31e0b6908a7bccb448e77b040a38a949b98d1/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | fetchClearinghouseState returns an empty list on HTTP failure, malformed payload, and exception, the same shape as a genuinely empty account. The adapter does log errors, but its return value alone cannot distinguish no positions from no evidence; fills also include spot, so a perp consumer must filter instrument class. |

## What this project does

A trading-agent adapter fetches Hyperliquid account positions and fills through the public info API. [README](https://github.com/dizcorvus/opencatz-ai/blob/9cb31e0b6908a7bccb448e77b040a38a949b98d1/README.md).

## Mechanism inspected

fetchClearinghouseState returns an empty list on HTTP failure, malformed payload, and exception, the same shape as a genuinely empty account. [Implementation](https://github.com/dizcorvus/opencatz-ai/blob/9cb31e0b6908a7bccb448e77b040a38a949b98d1/src/adapters/hyperliquid-adapter.ts#L107-L143).

## Limitation that matters

The adapter does log errors, but its return value alone cannot distinguish no positions from no evidence; fills also include spot, so a perp consumer must filter instrument class. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

Preserve a typed fetch status alongside positions and refuse account reconciliation on failed or malformed responses.

## Why this score

fetchClearinghouseState returns an empty list on HTTP failure, malformed payload, and exception, the same shape as a genuinely empty account. The adapter does log errors, but its return value alone cannot distinguish no positions from no evidence; fills also include spot, so a perp consumer must filter instrument class.

## Source trail

[README](https://github.com/dizcorvus/opencatz-ai/blob/9cb31e0b6908a7bccb448e77b040a38a949b98d1/README.md) - [Implementation](https://github.com/dizcorvus/opencatz-ai/blob/9cb31e0b6908a7bccb448e77b040a38a949b98d1/src/adapters/hyperliquid-adapter.ts#L107-L143) - [License](https://github.com/dizcorvus/opencatz-ai/blob/9cb31e0b6908a7bccb448e77b040a38a949b98d1/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
