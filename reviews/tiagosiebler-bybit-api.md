# Bybit TypeScript SDK — What does a rejected order promise mean after connection loss

**Decision question:** What does a rejected order promise mean after connection loss?

| Field | Review |
| --- | --- |
| Upstream | [Bybit TypeScript SDK](https://github.com/tiagosiebler/bybit-api) |
| Primary area | Execution & Exchange Integration |
| Source commit | [043f353fed77e6271d3b97fc0818207714eaebf9](https://github.com/tiagosiebler/bybit-api/commit/043f353fed77e6271d3b97fc0818207714eaebf9) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/tiagosiebler/bybit-api/blob/043f353fed77e6271d3b97fc0818207714eaebf9/LICENSE.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Useful for understanding request lifecycles over trading WebSockets. Connection loss rejects outstanding promises, but the resulting order state must be reconciled before retrying. |

## Project overview

The SDK provides Bybit REST and WebSocket APIs, including a promise-based interface for placing, amending and cancelling orders. [Project documentation](https://github.com/tiagosiebler/bybit-api/blob/043f353fed77e6271d3b97fc0818207714eaebf9/README.md#L445-L472).

## Mechanism worth inspecting

Unexpected socket closure rejects outstanding deferred promises before reconnecting; intentional closure also rejects them and clears connection state. [Close handling](https://github.com/tiagosiebler/bybit-api/blob/043f353fed77e6271d3b97fc0818207714eaebf9/src/util/BaseWSClient.ts#L1551-L1577).

## Important limit

A local promise rejection says the response was not delivered through that connection. It does not prove that the exchange rejected the order, so blind resubmission can duplicate intent.

## Questions to take into your own design

- What does a rejected order promise mean after connection loss?
- Which order identity is queried before retrying a request whose response was lost?

## Why this score for a trading system

3/5: exposes a consequential execution boundary, without establishing end-to-end order reconciliation in the inspected path.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
