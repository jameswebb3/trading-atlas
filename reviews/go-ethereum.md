# Geth: treat removed logs as reversals of earlier observations

**Decision question:** Can a log consumer undo an event when its block leaves the canonical chain?

| Field | Review |
| --- | --- |
| Upstream | [Geth](https://github.com/ethereum/go-ethereum) |
| Primary area | Market Data & Ingestion |
| Source commit | [920c07774c65ebb3023536f85df642c44478b540](https://github.com/ethereum/go-ethereum/commit/920c07774c65ebb3023536f85df642c44478b540) |
| Reviewed | 2026-09-26 |
| Declared license | [LGPL-3.0 library; GPL-3.0 command binaries](https://github.com/ethereum/go-ethereum/blob/920c07774c65ebb3023536f85df642c44478b540/README.md#L247-L255) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | An Ethereum execution client with RPC queries and live subscriptions. Its log event system forwards both added and removed logs through the same matching path, giving consumers explicit reversal evidence after a reorg. |

## Project overview

Geth provides an Ethereum execution node and JSON-RPC interfaces over HTTP, WebSocket, and IPC. [Project documentation](https://github.com/ethereum/go-ethereum/blob/920c07774c65ebb3023536f85df642c44478b540/README.md#L161-L173).

## Mechanism worth inspecting

The [event-system setup](https://github.com/ethereum/go-ethereum/blob/920c07774c65ebb3023536f85df642c44478b540/eth/filters/filter_system.go#L224-L237) subscribes to added and removed log events independently. The [event loop](https://github.com/ethereum/go-ethereum/blob/920c07774c65ebb3023536f85df642c44478b540/eth/filters/filter_system.go#L475-L484) forwards both through [the same filter matching function](https://github.com/ethereum/go-ethereum/blob/920c07774c65ebb3023536f85df642c44478b540/eth/filters/filter_system.go#L428-L437). The [filter API contract](https://github.com/ethereum/go-ethereum/blob/920c07774c65ebb3023536f85df642c44478b540/eth/filters/api.go#L405-L421) documents that previously returned logs can reappear with removed=true.

## Important limit

The [polling state](https://github.com/ethereum/go-ethereum/blob/920c07774c65ebb3023536f85df642c44478b540/eth/filters/api.go#L594-L601) drains a filter's accumulated log buffer and returns an error for an unknown filter. Consumers still need durable block identity, idempotent reversals, and recovery after disconnection; this review does not establish an archive service or downstream exactly-once delivery.

## Questions to take into your own design

- Is an event keyed by canonical block hash as well as transaction and log identity?
- Can removal reverse every derived balance and feature that consumed the original event?

## Why this score for a trading system

4/5: concrete reorg semantics and an inspectable dispatch path for market-data consumers. Persistent repair and historical completeness remain consumer responsibilities.

**Scope of this review:** README RPC/license sections, filter API documentation and buffer handling, event subscriptions, and added/removed dispatch code.
