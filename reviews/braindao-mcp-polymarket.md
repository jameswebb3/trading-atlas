# Polymarket MCP - Can an agent receive a structured failure before submitting a trade?

**Decision question:** Can an agent receive a structured failure before submitting a trade?

| Field | Review |
| --- | --- |
| Upstream | [BrainDAO/mcp-polymarket](https://github.com/BrainDAO/mcp-polymarket) |
| Primary area | Agents & Decision Systems |
| Source commit | [0e35d4b56bc3c50da1cc37ad079b5084eb8e3db7](https://github.com/BrainDAO/mcp-polymarket/commit/0e35d4b56bc3c50da1cc37ad079b5084eb8e3db7) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The trading client checks required on-chain allowances before placing orders and sets the SDK to throw on API errors. Tool wrappers serialize ApprovalRequiredError into a structured tool response while other exceptions propagate. The approval in this code is a token allowance, not a human authorization decision. Returning an error as JSON text also requires the agent to treat that response as failure; it cannot be mistaken for a successful order acknowledgement. |

## What this project does

Makes missing token allowances and API errors explicit before agent trades, but a serialized prerequisite error is not human approval or an order ACK.

## Mechanism inspected

The trading client checks required on-chain allowances before placing orders and sets the SDK to throw on API errors. Tool wrappers serialize ApprovalRequiredError into a structured tool response while other exceptions propagate.

## Limitation that matters

The approval in this code is a token allowance, not a human authorization decision. Returning an error as JSON text also requires the agent to treat that response as failure; it cannot be mistaken for a successful order acknowledgement.

## Practical check for a trading system

Separate machine prerequisites, human authorization and exchange ACK; require typed error states and reconcile the venue result before an agent reports a completed action.

## Why this score

3/5. The typed prerequisite path is a concrete agent-safety reference, though it targets a different venue and does not solve authorization or reconciliation.

## Source trail

[README.md](https://github.com/BrainDAO/mcp-polymarket/blob/0e35d4b56bc3c50da1cc37ad079b5084eb8e3db7/README.md#L1); [src/services/trading.ts](https://github.com/BrainDAO/mcp-polymarket/blob/0e35d4b56bc3c50da1cc37ad079b5084eb8e3db7/src/services/trading.ts#L98); [src/services/trading.ts](https://github.com/BrainDAO/mcp-polymarket/blob/0e35d4b56bc3c50da1cc37ad079b5084eb8e3db7/src/services/trading.ts#L160); [src/services/approvals.ts](https://github.com/BrainDAO/mcp-polymarket/blob/0e35d4b56bc3c50da1cc37ad079b5084eb8e3db7/src/services/approvals.ts#L150); [src/util/with-approval-guard.ts](https://github.com/BrainDAO/mcp-polymarket/blob/0e35d4b56bc3c50da1cc37ad079b5084eb8e3db7/src/util/with-approval-guard.ts#L1); [src/tools/cancel-all-orders.ts](https://github.com/BrainDAO/mcp-polymarket/blob/0e35d4b56bc3c50da1cc37ad079b5084eb8e3db7/src/tools/cancel-all-orders.ts#L7); [LICENSE](https://github.com/BrainDAO/mcp-polymarket/blob/0e35d4b56bc3c50da1cc37ad079b5084eb8e3db7/LICENSE#L1)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
