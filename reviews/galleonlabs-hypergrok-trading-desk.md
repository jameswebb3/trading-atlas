# HyperGrok Trading Desk — Prompt checklists are not authority

**Decision question:** Does an agent instruction enforce a trading approval?

| Field | Review |
| --- | --- |
| Upstream | [galleonlabs/hypergrok-trading-desk](https://github.com/galleonlabs/hypergrok-trading-desk) |
| Primary area | Execution & Exchange Integration |
| Source commit | [3b4e08d1331bc467bb80e83ce03606e300b2e6c8](https://github.com/galleonlabs/hypergrok-trading-desk/commit/3b4e08d1331bc467bb80e83ce03606e300b2e6c8) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/galleonlabs/hypergrok-trading-desk/blob/3b4e08d1331bc467bb80e83ce03606e300b2e6c8/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Its execution-agent document asks for a ticket ID, risk pass, approval, exchange order status, and reconciliation after sending. Those are prompt instructions; the inspected doctor script checks presence of agent files rather than enforcing approval in the exchange client. |

## What this project does

A set of agent roles and scripts for a Hyperliquid trading desk. [Project README](https://github.com/galleonlabs/hypergrok-trading-desk/blob/3b4e08d1331bc467bb80e83ce03606e300b2e6c8/README.md#L9).

## Mechanism inspected

Its execution-agent document asks for a ticket ID, risk pass, approval, exchange order status, and reconciliation after sending. [Implementation](https://github.com/galleonlabs/hypergrok-trading-desk/blob/3b4e08d1331bc467bb80e83ce03606e300b2e6c8/scripts/desk_doctor.py#L137). [Related source 1](https://github.com/galleonlabs/hypergrok-trading-desk/blob/3b4e08d1331bc467bb80e83ce03606e300b2e6c8/agents/execution-trader.md#L33).

## Limitation that matters

Those are prompt instructions; the inspected doctor script checks presence of agent files rather than enforcing approval in the exchange client. This is a source review, not a runtime or security test.

## Practical check for a trading system

Put ticket binding and risk authorization in the order API, and treat prompt text as advisory.

## Why this score

The checklist names useful evidence, but there is no demonstrated code-enforced authority boundary.

## Source trail

[README](https://github.com/galleonlabs/hypergrok-trading-desk/blob/3b4e08d1331bc467bb80e83ce03606e300b2e6c8/README.md#L9); [Implementation](https://github.com/galleonlabs/hypergrok-trading-desk/blob/3b4e08d1331bc467bb80e83ce03606e300b2e6c8/scripts/desk_doctor.py#L137); [Related source 1](https://github.com/galleonlabs/hypergrok-trading-desk/blob/3b4e08d1331bc467bb80e83ce03606e300b2e6c8/agents/execution-trader.md#L33) - [License](https://github.com/galleonlabs/hypergrok-trading-desk/blob/3b4e08d1331bc467bb80e83ce03606e300b2e6c8/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
