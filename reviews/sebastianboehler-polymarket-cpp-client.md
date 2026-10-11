# Polymarket C++ Client - Can a reconnect leave an old orderbook callback looking current?

**Decision question:** Can a reconnect leave an old orderbook callback looking current?

| Field | Review |
| --- | --- |
| Upstream | [SebastianBoehler/polymarket-cpp-client](https://github.com/SebastianBoehler/polymarket-cpp-client) |
| Primary area | Market Data & Ingestion |
| Source commit | [2a2129cd063afacd0dfe925ef151f7137b199cca](https://github.com/SebastianBoehler/polymarket-cpp-client/commit/2a2129cd063afacd0dfe925ef151f7137b199cca) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Invalidates cached books and rejects callbacks from an old WebSocket generation. A fresh snapshot still needs venue-specific continuity checks. |

## What this project does

A C++20 Polymarket client with market-data streaming, orderbook ownership and order signing.

## Mechanism inspected

Every streamed book update is checked against both owner and WebSocket generation; disconnect or stream invalidation bumps the generation and clears cached books and market legs. A parse error requests a resnapshot.

## Limitation that matters

Generation guards reject stale callbacks, but they do not prove that a venue stream has no missing update between snapshots. Order submission and venue fill correctness are separate paths.

## Practical check for a trading system

Tag subscriptions and cached books by stream generation; require a fresh snapshot after invalidation and test callback races.

## Why this score

4/5. The inspected code directly addresses stale-book reuse after reconnect with explicit state invalidation.

## Source trail

[README](https://github.com/SebastianBoehler/polymarket-cpp-client/blob/2a2129cd063afacd0dfe925ef151f7137b199cca/README.md#L78); [docs/order-flow.md](https://github.com/SebastianBoehler/polymarket-cpp-client/blob/2a2129cd063afacd0dfe925ef151f7137b199cca/docs/order-flow.md#L1); [src/orderbook_runtime_stream.cpp](https://github.com/SebastianBoehler/polymarket-cpp-client/blob/2a2129cd063afacd0dfe925ef151f7137b199cca/src/orderbook_runtime_stream.cpp#L9); [src/orderbook_runtime_stream.cpp](https://github.com/SebastianBoehler/polymarket-cpp-client/blob/2a2129cd063afacd0dfe925ef151f7137b199cca/src/orderbook_runtime_stream.cpp#L37); [src/orderbook_runtime_lifecycle.cpp](https://github.com/SebastianBoehler/polymarket-cpp-client/blob/2a2129cd063afacd0dfe925ef151f7137b199cca/src/orderbook_runtime_lifecycle.cpp#L59); [License text](https://github.com/SebastianBoehler/polymarket-cpp-client/blob/2a2129cd063afacd0dfe925ef151f7137b199cca/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
