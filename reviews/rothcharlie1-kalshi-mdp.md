# Kalshi Market Data Platform - Does a Redis market-data sink surface lost writes?

**Decision question:** Does a Redis market-data sink surface lost writes?

| Field | Review |
| --- | --- |
| Upstream | [rothcharlie1/kalshi-mdp](https://github.com/rothcharlie1/kalshi-mdp) |
| Primary area | Market Data & Ingestion |
| Source commit | [4010bb3369ba0d5b144e244ecc25eae269b8108d](https://github.com/rothcharlie1/kalshi-mdp/commit/4010bb3369ba0d5b144e244ecc25eae269b8108d) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Writes Kalshi book snapshots and deltas to Redis. Sink failures can be reported as success while the cached book remains unverified. |

## What this project does

A small Rust Kalshi WebSocket receiver that writes snapshots and deltas to Redis.

## Mechanism inspected

Its sink replaces a snapshot hash and applies each delta to the Redis snapshot; the server forwards parsed market-data messages to the sink.

## Limitation that matters

A Redis snapshot HSET failure is logged but returned as success, and the server also turns other sink-write errors into success. Trade messages are only logged. The receive loop unwraps messages; no sequence-gap recovery is visible in these paths. No root license text was verified.

## Practical check for a trading system

Count and persist rejected updates, invalidate book state after sink failure, and resume only from a fresh verified snapshot.

## Why this score

1/5. The data path demonstrates a concrete silent-loss failure more than a safe feed implementation.

## Source trail

[README](https://github.com/rothcharlie1/kalshi-mdp/blob/4010bb3369ba0d5b144e244ecc25eae269b8108d/README.md#L1); [src/server.rs](https://github.com/rothcharlie1/kalshi-mdp/blob/4010bb3369ba0d5b144e244ecc25eae269b8108d/src/server.rs#L65); [src/server.rs](https://github.com/rothcharlie1/kalshi-mdp/blob/4010bb3369ba0d5b144e244ecc25eae269b8108d/src/server.rs#L92); [src/sinks/redis.rs](https://github.com/rothcharlie1/kalshi-mdp/blob/4010bb3369ba0d5b144e244ecc25eae269b8108d/src/sinks/redis.rs#L48); [src/sinks/redis.rs](https://github.com/rothcharlie1/kalshi-mdp/blob/4010bb3369ba0d5b144e244ecc25eae269b8108d/src/sinks/redis.rs#L70).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
