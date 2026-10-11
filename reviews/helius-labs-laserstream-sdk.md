# LaserStream SDK — Is a replay cursor a durable consumer checkpoint

**Decision question:** Is a replay cursor a durable consumer checkpoint?

| Field | Review |
| --- | --- |
| Upstream | [LaserStream SDK](https://github.com/helius-labs/laserstream-sdk) |
| Primary area | Market Data & Ingestion |
| Source commit | [d410dcbd3386dfa77cdb24379d3258bb0153f778](https://github.com/helius-labs/laserstream-sdk/commit/d410dcbd3386dfa77cdb24379d3258bb0153f778) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/helius-labs/laserstream-sdk/blob/d410dcbd3386dfa77cdb24379d3258bb0153f778/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A useful Solana streaming reference for commitment-aware replay. The tracked slot is a receipt cursor, so durable consumers still need their own checkpoints, deduplication and out-of-range recovery. |

## Project overview

LaserStream's SDK streams Solana updates over gRPC and provides reconnection with slot-based replay. [Project documentation](https://github.com/helius-labs/laserstream-sdk/blob/d410dcbd3386dfa77cdb24379d3258bb0153f778/rust/README.md#L1-L3).

## Mechanism worth inspecting

The Rust client derives the reconnection slot from commitment level, rewinding processed subscriptions by 31 slots. It advances the tracked slot when a slot update arrives, before yielding consumer data. [Reconnect cursor](https://github.com/helius-labs/laserstream-sdk/blob/d410dcbd3386dfa77cdb24379d3258bb0153f778/rust/src/client.rs#L150-L162), [tracking and delivery](https://github.com/helius-labs/laserstream-sdk/blob/d410dcbd3386dfa77cdb24379d3258bb0153f778/rust/src/client.rs#L214-L237).

## Important limit

The cursor tracks received slot updates, not an application's durable storage acknowledgment. Replay can duplicate data, and the README documents a bounded replay horizon with an endpoint query for its oldest slot. [Replay boundary](https://github.com/helius-labs/laserstream-sdk/blob/d410dcbd3386dfa77cdb24379d3258bb0153f778/README.md#L55-L73).

## Questions to take into your own design

- Is a replay cursor a durable consumer checkpoint?
- What durable checkpoint and recovery path cover an interruption beyond server replay retention?

## Why this score for a trading system

3/5: concrete on-chain ingestion behavior, limited by service replay bounds and the absence of a consumer durability contract in this path.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
