# OKX API for Node.js — Does resolving a WebSocket request promise mean the order is filled

**Decision question:** Does resolving a WebSocket request promise mean the order is filled?

| Field | Review |
| --- | --- |
| Upstream | [OKX API for Node.js](https://github.com/tiagosiebler/okx-api) |
| Primary area | Execution & Exchange Integration |
| Source commit | [bd09f365cf24070a9355aefd6c561e747893abfe](https://github.com/tiagosiebler/okx-api/commit/bd09f365cf24070a9355aefd6c561e747893abfe) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/tiagosiebler/okx-api/blob/bd09f365cf24070a9355aefd6c561e747893abfe/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Matches trading-command replies to request identity and operation, while separating them from stream updates. Request resolution remains distinct from order execution, and missing IDs need an explicit recovery policy. |

## Project overview

A TypeScript SDK for OKX REST, account streams and WebSocket trading commands, including request-response matching. [Project documentation](https://github.com/tiagosiebler/okx-api/blob/bd09f365cf24070a9355aefd6c561e747893abfe/README.md#L25-L38).

## Mechanism worth inspecting

The client identifies WebSocket API responses and matches deferred promises by request ID plus operation. A nonzero top-level code rejects the promise; zero resolves it and emits a response. Updates take a separate event path. [Request result matching](https://github.com/tiagosiebler/okx-api/blob/bd09f365cf24070a9355aefd6c561e747893abfe/src/websocket-client.ts#L567-L653); [data-update branch](https://github.com/tiagosiebler/okx-api/blob/bd09f365cf24070a9355aefd6c561e747893abfe/src/websocket-client.ts#L671-L676).

## Important limit

This is request-result classification, not a fill ledger. A missing request ID is logged as a condition that can leave the promise stuck; item-level result data and account executions still require application interpretation. [Missing identity warning](https://github.com/tiagosiebler/okx-api/blob/bd09f365cf24070a9355aefd6c561e747893abfe/src/websocket-client.ts#L588-L606).

## Questions to take into your own design

- Is request acceptance kept separate from the account's fill evidence?
- What happens when a response arrives without the identity needed to resolve it?

## Why this score for a trading system

3/5: directly relevant command correlation, with execution confirmation and item-level interpretation outside the inspected branch.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
