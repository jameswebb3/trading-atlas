# Bitget API for Node.js — Can an event classified as a response also contain an error

**Decision question:** Can an event classified as a response also contain an error?

| Field | Review |
| --- | --- |
| Upstream | [Bitget API for Node.js](https://github.com/tiagosiebler/bitget-api) |
| Primary area | Execution & Exchange Integration |
| Source commit | [7dfaa1f09e3f34f40eae56012e2846d56cb4b995](https://github.com/tiagosiebler/bitget-api/commit/7dfaa1f09e3f34f40eae56012e2846d56cb4b995) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/tiagosiebler/bitget-api/blob/7dfaa1f09e3f34f40eae56012e2846d56cb4b995/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Shows that a WebSocket response event can coexist with an exception event for the same error message. Consumers need an explicit event contract rather than treating every response callback as success. |

## Project overview

A Node.js and TypeScript SDK for Bitget's REST and WebSocket interfaces across classic and unified-account APIs. [Project documentation](https://github.com/tiagosiebler/bitget-api/blob/7dfaa1f09e3f34f40eae56012e2846d56cb4b995/README.md#L26-L40).

## Mechanism worth inspecting

The inspected V2 event decoder emits response for messages containing an event field, and additionally emits exception when that event is error. Login success and messages carrying subscription arguments follow separate branches. [V2 event classifier](https://github.com/tiagosiebler/bitget-api/blob/7dfaa1f09e3f34f40eae56012e2846d56cb4b995/src/websocket-client-v2.ts#L391-L448).

## Important limit

Listening only to the response event would discard an important distinction. This review covers the V2 classifier, not V3 commands, order-book reconstruction, reconnection completeness or an entire account lifecycle.

## Questions to take into your own design

- Does each event consumer inspect the message outcome instead of trusting its callback name?
- Are error, authentication and data events mapped to distinct application states?

## Why this score for a trading system

2/5: a narrow adapter-event caution, with limited evidence here for broader execution guarantees.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
