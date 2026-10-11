# Kalshi WebSocket Client - Can a stream parser preserve timestamp strings before typed conversion?

**Decision question:** Can a stream parser preserve timestamp strings before typed conversion?

| Field | Review |
| --- | --- |
| Upstream | [Marfusios/kalshi-client-websocket](https://github.com/Marfusios/kalshi-client-websocket) |
| Primary area | Market Data & Ingestion |
| Source commit | [0a2b19472d3b7f014a67c09f801b9327dee67c92](https://github.com/Marfusios/kalshi-client-websocket/commit/0a2b19472d3b7f014a67c09f801b9327dee67c92) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The handler disables automatic JSON date parsing and routes control, book and trade message types to separate streams. The handler does not itself verify sequence continuity or require a complete book before dispatching deltas. |

## What this project does

A .NET client for Kalshi WebSocket channels.

## Mechanism inspected

The handler disables automatic JSON date parsing and routes control, book and trade message types to separate streams.

## Limitation that matters

The handler does not itself verify sequence continuity or require a complete book before dispatching deltas.

## Practical check for a trading system

Keep raw timestamp text and add subscription-scoped sequence and snapshot gates downstream.

## Why this score

2/5. Typed routing is useful, but continuity is a separate contract.

## Source trail

[README](https://github.com/Marfusios/kalshi-client-websocket/blob/0a2b19472d3b7f014a67c09f801b9327dee67c92/README.md#L1); [src/Kalshi.Client.Websocket/Client/KalshiMessageHandler.cs](https://github.com/Marfusios/kalshi-client-websocket/blob/0a2b19472d3b7f014a67c09f801b9327dee67c92/src/Kalshi.Client.Websocket/Client/KalshiMessageHandler.cs#L25); [src/Kalshi.Client.Websocket/Client/KalshiMessageHandler.cs](https://github.com/Marfusios/kalshi-client-websocket/blob/0a2b19472d3b7f014a67c09f801b9327dee67c92/src/Kalshi.Client.Websocket/Client/KalshiMessageHandler.cs#L105); [Root license](https://github.com/Marfusios/kalshi-client-websocket/blob/0a2b19472d3b7f014a67c09f801b9327dee67c92/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
