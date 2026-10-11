# hyperliquid-ai-signal-bot — A placeholder account state cannot enforce live risk

**Decision question:** Does the risk gate read actual exposure before submitting an order?

| Field | Review |
| --- | --- |
| Upstream | [picotts544/hyperliquid-ai-signal-bot](https://github.com/picotts544/hyperliquid-ai-signal-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [93c5d0a6e1219839451f7c24027101f79a474429](https://github.com/picotts544/hyperliquid-ai-signal-bot/commit/93c5d0a6e1219839451f7c24027101f79a474429) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/picotts544/hyperliquid-ai-signal-bot/blob/93c5d0a6e1219839451f7c24027101f79a474429/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | Before each order the runner constructs a position with size zero and leverage one, passes that fabricated snapshot to the risk gate, then submits any generated orders; its signal is a simple recent-close difference adjusted by a configured funding value. The inspected path does not read reconciled positions or outstanding orders before this check, and its daily PnL counter is process memory. The README's production-grade and performance claims are not established by this code. |

## What this project does

Hyperliquid perpetual bot template presented as an AI signal and live-risk system. [README](https://github.com/picotts544/hyperliquid-ai-signal-bot/blob/93c5d0a6e1219839451f7c24027101f79a474429/README.md).

## Mechanism inspected

Before each order the runner constructs a position with size zero and leverage one, passes that fabricated snapshot to the risk gate, then submits any generated orders; its signal is a simple recent-close difference adjusted by a configured funding value. [Implementation](https://github.com/picotts544/hyperliquid-ai-signal-bot/blob/93c5d0a6e1219839451f7c24027101f79a474429/src/hyperliquid_bot/runner.py#L41-L72). [Related implementation](https://github.com/picotts544/hyperliquid-ai-signal-bot/blob/93c5d0a6e1219839451f7c24027101f79a474429/src/hyperliquid_bot/risk.py#L15-L43).

## Limitation that matters

The inspected path does not read reconciled positions or outstanding orders before this check, and its daily PnL counter is process memory. The README's production-grade and performance claims are not established by this code. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Require reconciled account exposure, pending orders and persisted loss state at the order gate; do not treat a zero-position placeholder or a dashboard image as live-risk evidence.

## Why this score

Before each order the runner constructs a position with size zero and leverage one, passes that fabricated snapshot to the risk gate, then submits any generated orders; its signal is a simple recent-close difference adjusted by a configured funding value. The inspected path does not read reconciled positions or outstanding orders before this check, and its daily PnL counter is process memory. The README's production-grade and performance claims are not established by this code.

## Source trail

[README](https://github.com/picotts544/hyperliquid-ai-signal-bot/blob/93c5d0a6e1219839451f7c24027101f79a474429/README.md) · [Implementation](https://github.com/picotts544/hyperliquid-ai-signal-bot/blob/93c5d0a6e1219839451f7c24027101f79a474429/src/hyperliquid_bot/runner.py#L41-L72) · [Related implementation](https://github.com/picotts544/hyperliquid-ai-signal-bot/blob/93c5d0a6e1219839451f7c24027101f79a474429/src/hyperliquid_bot/risk.py#L15-L43) · [License](https://github.com/picotts544/hyperliquid-ai-signal-bot/blob/93c5d0a6e1219839451f7c24027101f79a474429/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
