# baby-smith — A new fill is not proof of this order's fill

**Decision question:** Does an order verifier match the fill to the order it submitted?

| Field | Review |
| --- | --- |
| Upstream | [algo-traders-club/baby-smith](https://github.com/algo-traders-club/baby-smith) |
| Primary area | Execution & Exchange Integration |
| Source commit | [63ff0d63f92f4df94fef4487095f57856874b55c](https://github.com/algo-traders-club/baby-smith/commit/63ff0d63f92f4df94fef4487095f57856874b55c) |
| Reviewed | 2026-10-09 |
| Declared license | No root license found; README badge claims MIT |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | It counts account fills before submission, waits one second after an SDK response marked ok, then treats any increase in account fill count as confirmation and reports the newest fill. The verifier does not correlate order ID, client ID, asset, side or quantity. Another order's fill can satisfy the count check; no new fill after one second is reported as failure despite an accepted order. |

## What this project does

Hyperliquid autonomous market-making bot with order and position management paths. [README](https://github.com/algo-traders-club/baby-smith/blob/63ff0d63f92f4df94fef4487095f57856874b55c/README.md).

## Mechanism inspected

It counts account fills before submission, waits one second after an SDK response marked ok, then treats any increase in account fill count as confirmation and reports the newest fill. [Implementation](https://github.com/algo-traders-club/baby-smith/blob/63ff0d63f92f4df94fef4487095f57856874b55c/src/agent_smith/core/order_manager.py#L26-L49). [Related implementation](https://github.com/algo-traders-club/baby-smith/blob/63ff0d63f92f4df94fef4487095f57856874b55c/src/agent_smith/core/order_manager.py#L292-L316).

## Limitation that matters

The verifier does not correlate order ID, client ID, asset, side or quantity. Another order's fill can satisfy the count check; no new fill after one second is reported as failure despite an accepted order. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Bind each acknowledgement and fill to one client/order identity, retaining unknown or partial states until account reconciliation resolves them.

## Why this score

It counts account fills before submission, waits one second after an SDK response marked ok, then treats any increase in account fill count as confirmation and reports the newest fill. The verifier does not correlate order ID, client ID, asset, side or quantity. Another order's fill can satisfy the count check; no new fill after one second is reported as failure despite an accepted order.

## Source trail

[README](https://github.com/algo-traders-club/baby-smith/blob/63ff0d63f92f4df94fef4487095f57856874b55c/README.md) · [Implementation](https://github.com/algo-traders-club/baby-smith/blob/63ff0d63f92f4df94fef4487095f57856874b55c/src/agent_smith/core/order_manager.py#L26-L49) · [Related implementation](https://github.com/algo-traders-club/baby-smith/blob/63ff0d63f92f4df94fef4487095f57856874b55c/src/agent_smith/core/order_manager.py#L292-L316).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
