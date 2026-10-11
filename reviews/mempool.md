# Mempool: protect a local transaction cache during node restarts

**Decision question:** Can a temporarily empty node response be distinguished from a genuine mempool contraction?

| Field | Review |
| --- | --- |
| Upstream | [Mempool](https://github.com/mempool/mempool) |
| Primary area | Market Data & Ingestion |
| Source commit | [5b8486a9e376ec8d1e3658c8256a4e2de95d2e85](https://github.com/mempool/mempool/commit/5b8486a9e376ec8d1e3658c8256a4e2de95d2e85) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0 with proxy-version and trademark notices](https://github.com/mempool/mempool/blob/5b8486a9e376ec8d1e3658c8256a4e2de95d2e85/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Tracks Bitcoin mempool transactions and fee conditions. Its cache temporarily delays mass deletion after a large contraction, reducing restart-induced false changes, and excludes catch-up traffic from live arrival-rate counters. |

## Project overview

A Bitcoin explorer and fee-market application with a self-hosted backend, transaction cache, and live mempool statistics. [Project documentation](https://github.com/mempool/mempool/blob/5b8486a9e376ec8d1e3658c8256a4e2de95d2e85/README.md#L1-L12).

## Mechanism worth inspecting

The [cache update path](https://github.com/mempool/mempool/blob/5b8486a9e376ec8d1e3658c8256a4e2de95d2e85/backend/src/api/mempool.ts#L294-L326) counts arrivals only while synchronized. The [clear-protection branch](https://github.com/mempool/mempool/blob/5b8486a9e376ec8d1e3658c8256a4e2de95d2e85/backend/src/api/mempool.ts#L354-L386) delays deletion after a substantial contraction in a sufficiently large cache, marks it out of sync, and later resumes normal removal. [Sync reporting](https://github.com/mempool/mempool/blob/5b8486a9e376ec8d1e3658c8256a4e2de95d2e85/backend/src/api/mempool.ts#L407-L427) tracks remaining cache-size difference separately from new transaction callbacks.

## Important limit

Protection depends on hard-coded size/contraction thresholds and a configured timeout, not a proof of node restart. It deliberately keeps stale entries temporarily. Equal counts can support an in-sync flag but do not establish global mempool coverage. The [backend documentation](https://github.com/mempool/mempool/blob/5b8486a9e376ec8d1e3658c8256a4e2de95d2e85/backend/README.md#L31-L46) also separates node transactions from optional address lookup infrastructure.

## Questions to take into your own design

- Can backfill arrivals accidentally inflate a live transaction-flow feature?
- When deletion is deferred, are downstream consumers told the cache is provisional?

## Why this score for a trading system

4/5: concrete safeguards and explicit sync state directly relevant to mempool data ingestion. Heuristic deletion protection requires separate provenance and recovery rules.

**Scope of this review:** Project and backend README, cache-update implementation, and license notice; no fee estimates or live behavior tested.
