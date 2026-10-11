# viem — a watcher cursor is not a durable checkpoint

**Decision question:** What survives if an event callback or collector process fails?

| Field | Review |
| --- | --- |
| Upstream | [viem](https://github.com/wevm/viem) |
| Primary area | Market Data & Ingestion |
| Source commit | [51f9ad9595507c3a5032254b3bc1ed342af2ba68](https://github.com/wevm/viem/commit/51f9ad9595507c3a5032254b3bc1ed342af2ba68) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/wevm/viem/blob/51f9ad9595507c3a5032254b3bc1ed342af2ba68/src/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Its watcher makes filter fallback and range polling explicit. The in-memory cursor advances before callback delivery, so durable ingestion, restart replay and canonical-chain reconciliation need an additional collector contract. |

## Project overview

viem supplies typed Ethereum JSON-RPC and contract APIs; event watching supports filters with a log-polling fallback. [Project documentation](https://github.com/wevm/viem/blob/51f9ad9595507c3a5032254b3bc1ed342af2ba68/src/actions/public/watchEvent.ts#L122-L131).

## Mechanism worth inspecting

When filters are unavailable, the watcher fetches logs between the prior block plus one and the latest block, then updates its in-memory block cursor before delivering logs. Filter errors can trigger reinitialization. [Range and cursor](https://github.com/wevm/viem/blob/51f9ad9595507c3a5032254b3bc1ed342af2ba68/src/actions/public/watchEvent.ts#L237-L280); [error handling](https://github.com/wevm/viem/blob/51f9ad9595507c3a5032254b3bc1ed342af2ba68/src/actions/public/watchEvent.ts#L281-L286).

## Important limit

Delivering logs to a callback is not proof they were durably committed. The cursor is process state, and this fallback path alone is not a canonical-chain rollback system. A durable collector needs transactional ingestion, restart/backfill and block-hash reconciliation outside the watcher.

## Questions to take into your own design

- Does the durable checkpoint advance only after the complete log batch is committed?
- Can restart or a reorg replay the range without duplicating derived observations?

## Why this score for a trading system

3/5: a concrete event-delivery and checkpoint boundary, useful to collectors that add durable replay and canonicality controls.

**Scope of this review:** Polling event watcher and filter fallback; websocket delivery and all reorg behavior were not audited.
