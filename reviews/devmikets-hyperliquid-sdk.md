# Devmikets Hyperliquid SDK — Does cancelling a request cancel its exchange-side effect

**Decision question:** Does cancelling a request cancel its exchange-side effect?

| Field | Review |
| --- | --- |
| Upstream | [Devmikets Hyperliquid SDK](https://github.com/devmikets/hyperliquid-sdk) |
| Primary area | Execution & Exchange Integration |
| Source commit | [a234da908c21681d08248f605351c277457bb762](https://github.com/devmikets/hyperliquid-sdk/commit/a234da908c21681d08248f605351c277457bb762) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/devmikets/hyperliquid-sdk/blob/a234da908c21681d08248f605351c277457bb762/LICENSE.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A focused reference for typed requests and WebSocket correlation. Timeout cleanup is explicit; an expired local request still leaves the exchange-side order outcome to be established. |

## Project overview

A typed Hyperliquid SDK with HTTP and WebSocket transports and client-side signing interfaces. [Project documentation](https://github.com/devmikets/hyperliquid-sdk/blob/a234da908c21681d08248f605351c277457bb762/README.md#L48-L64).

## Mechanism worth inspecting

The WebSocket post manager assigns request IDs, matches replies and combines caller cancellation with a timeout. Its finally block removes pending requests and abort listeners. [Correlation](https://github.com/devmikets/hyperliquid-sdk/blob/a234da908c21681d08248f605351c277457bb762/src/transport/websocket/_postRequest.ts#L47-L87), [request lifecycle](https://github.com/devmikets/hyperliquid-sdk/blob/a234da908c21681d08248f605351c277457bb762/src/transport/websocket/_postRequest.ts#L184-L237).

## Important limit

Aborting the local wait removes its correlation entry, but the inspected path does not cancel an order already sent to the exchange. A later outcome needs independent account reconciliation.

## Questions to take into your own design

- Does cancelling a request cancel its exchange-side effect?
- How are exchange outcomes recorded when their local request waits have already expired?

## Why this score for a trading system

3/5: useful direct execution lifecycle, without evidence in this path of reconciliation after a late or missing reply.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
