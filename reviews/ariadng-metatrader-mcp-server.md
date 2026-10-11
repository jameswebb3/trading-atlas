# MetaTrader MCP Server - Can a bulk cancel report success when individual cancels failed?

**Decision question:** Can a bulk cancel report success when individual cancels failed?

| Field | Review |
| --- | --- |
| Upstream | [ariadng/metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server) |
| Primary area | Execution Exchange Integration |
| Source commit | [bd2ff591e32cb492fafefe74221d502dd78b71ef](https://github.com/ariadng/metatrader-mcp-server/commit/bd2ff591e32cb492fafefe74221d502dd78b71ef) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Loops through pending IDs and counts each cancellation call, regardless of the returned error flag. The single-order helper returns an error dictionary on failure; bulk success therefore need not mean every pending order was cancelled. |

## What this project does

A MetaTrader MCP server that exposes trading operations to an assistant. The inspected path implements cancellation of all pending orders.

## Mechanism inspected

cancel_all_pending_orders gets pending IDs, calls cancel_pending_order for each, increments a counter and returns error=False with a success message. The single-order helper returns a structured dictionary with error=True if the ID is invalid or the underlying REMOVE request fails.

## Limitation that matters

The bulk function ignores each helper result. It reports the number of attempts as successful cancels, even if a helper returned error=True. A synchronous exception may still abort the loop; the examined failure mode is a returned error dictionary. This is a source review, not an exchange test.

## Practical check for a trading system

For bulk order actions, report attempted, confirmed, failed and unresolved IDs separately. Query open orders after the batch before claiming the account is flat or safe to replace quotes.

## Why this score

2/5 because the source exposes a concrete accounting trap in bulk cancellation, while the venue and MCP interface are not a Hyperliquid execution reference.

## Source trail

[README](https://github.com/ariadng/metatrader-mcp-server/blob/bd2ff591e32cb492fafefe74221d502dd78b71ef/README.md#L1); [Bulk cancel](https://github.com/ariadng/metatrader-mcp-server/blob/bd2ff591e32cb492fafefe74221d502dd78b71ef/src/metatrader_client/order/cancel_all_pending_orders.py#L11); [Individual error contract](https://github.com/ariadng/metatrader-mcp-server/blob/bd2ff591e32cb492fafefe74221d502dd78b71ef/src/metatrader_client/order/cancel_pending_order.py#L17); [License](https://github.com/ariadng/metatrader-mcp-server/blob/bd2ff591e32cb492fafefe74221d502dd78b71ef/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
