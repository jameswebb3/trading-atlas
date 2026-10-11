# kalshi-cpp - Are WebSocket control errors distinguishable from data?

**Decision question:** Are WebSocket control errors distinguishable from data?

| Field | Review |
| --- | --- |
| Upstream | [Reddimus/kalshi-cpp](https://github.com/Reddimus/kalshi-cpp) |
| Primary area | Market Data & Ingestion |
| Source commit | [6d9d995052e04e52c108b6d4aeb9cc091d4c0433](https://github.com/Reddimus/kalshi-cpp/commit/6d9d995052e04e52c108b6d4aeb9cc091d4c0433) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The parser returns distinct subscribed, OK, error, malformed and data frame variants, carrying IDs and sequence fields. An unrecognized frame becomes an empty result here; callers still need gap checks and explicit unknown-frame handling. |

## What this project does

A C++ Kalshi client with typed WebSocket frame parsing.

## Mechanism inspected

The parser returns distinct subscribed, OK, error, malformed and data frame variants, carrying IDs and sequence fields.

## Limitation that matters

An unrecognized frame becomes an empty result here; callers still need gap checks and explicit unknown-frame handling.

## Practical check for a trading system

Keep the raw frame, parse outcome and sequence evidence so a schema change cannot silently erase events.

## Why this score

3/5. Typed envelopes are useful, but transport completeness is outside this parser.

## Source trail

[README](https://github.com/Reddimus/kalshi-cpp/blob/6d9d995052e04e52c108b6d4aeb9cc091d4c0433/README.md#L1); [docs/api-coverage.md](https://github.com/Reddimus/kalshi-cpp/blob/6d9d995052e04e52c108b6d4aeb9cc091d4c0433/docs/api-coverage.md#L1); [src/ws/frames.cpp](https://github.com/Reddimus/kalshi-cpp/blob/6d9d995052e04e52c108b6d4aeb9cc091d4c0433/src/ws/frames.cpp#L49); [Root license](https://github.com/Reddimus/kalshi-cpp/blob/6d9d995052e04e52c108b6d4aeb9cc091d4c0433/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
