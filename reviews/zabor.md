# Record exchange payloads and receipt time without hiding reconnect gaps

**Decision question:** Can a recovered WebSocket feed prove its capture was continuous?

| Field | Review |
| --- | --- |
| Upstream | [zaBor](https://github.com/zabor-crypto/zaBor) |
| Primary area | Market Data & Ingestion |
| Source commit | [bc05cf69334c895312c601f201856f6f0a343eee](https://github.com/zabor-crypto/zaBor/commit/bc05cf69334c895312c601f201856f6f0a343eee) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/zabor-crypto/zaBor/blob/bc05cf69334c895312c601f201856f6f0a343eee/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Its Hyperliquid recorder preserves exchange payloads beside local receipt timestamps and writes per-channel health state. Reconnect backoff restores subscriptions, but the inspected loop does not backfill the disconnected interval. Useful capture evidence; continuity must be established separately. |

## Project overview

Market-engineering toolkit with data recording, risk-control modules, and research utilities. Its recorder preserves raw exchange payloads and local receipt times, supplying capture evidence for microstructure research.

[Project documentation](https://github.com/zabor-crypto/zaBor/blob/bc05cf69334c895312c601f201856f6f0a343eee/README.md#L11-L20).

## Mechanism worth inspecting

The [project overview](https://github.com/zabor-crypto/zaBor/blob/bc05cf69334c895312c601f201856f6f0a343eee/README.md#L11-L20) frames the toolkit as operational safety and reproducible research. The [recorder guide](https://github.com/zabor-crypto/zaBor/blob/bc05cf69334c895312c601f201856f6f0a343eee/scripts/hl_microstructure_recorder/README.md#L26-L38) describes raw channel capture. The [implementation](https://github.com/zabor-crypto/zaBor/blob/bc05cf69334c895312c601f201856f6f0a343eee/scripts/hl_microstructure_recorder/hl_l2_recorder.py#L72-L129) records last-message times and counts, wraps payloads with recv_ts_ms, and reconnects with exponential backoff.

## Important limit

The subscribed streams in this file are l2Book, bbo, and trades; broader funding/OI claims in the toolkit description should not be assumed to come from this loop. Health snapshots show activity, not completeness, and no backfill appears in the reconnect branch.

## Questions to take into your own design

- Which intervals are explicitly marked unavailable after disconnects?
- Can analyses distinguish exchange event time from local receipt time?

## Why this score for a trading system

3/5: Raw payload preservation and per-channel receipt evidence are directly useful for trading research, while gap recovery and complete channel coverage remain separate work.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
