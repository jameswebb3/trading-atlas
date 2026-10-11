# Pinax API: HTTP cache age is part of market-data age

**Decision question:** How old can a supposedly current market-data response be?

| Field | Review |
| --- | --- |
| Upstream | [Pinax API](https://github.com/pinax-network/pinax-api) |
| Primary area | Market Data & Ingestion |
| Source commit | [4a033d5bd41bbae5b0f1ec3b5c21308ef9f57c11](https://github.com/pinax-network/pinax-api/commit/4a033d5bd41bbae5b0f1ec3b5c21308ef9f57c11) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/pinax-network/pinax-api/blob/4a033d5bd41bbae5b0f1ec3b5c21308ef9f57c11/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Documents Hyperliquid market-data endpoints, but selected routes permit shared-proxy caching and stale-while-revalidate. A response timestamp and the upstream event timestamp must be kept distinct before using this feed in time-sensitive decisions. |

## Mechanism worth inspecting

The [perpetual-market overview](https://github.com/pinax-network/pinax-api/blob/4a033d5bd41bbae5b0f1ec3b5c21308ef9f57c11/README.md#L48-L52) lists Hyperliquid OHLC, open interest, and liquidations. The [cache guide](https://github.com/pinax-network/pinax-api/blob/4a033d5bd41bbae5b0f1ec3b5c21308ef9f57c11/README.md#L182-L207) documents default and extended cache tiers. The [middleware](https://github.com/pinax-network/pinax-api/blob/4a033d5bd41bbae5b0f1ec3b5c21308ef9f57c11/src/middleware/cacheControl.ts#L28-L46) adds public max-age, shared-proxy s-maxage, and stale-while-revalidate headers after a 200 response. This is a useful reminder that transport delivery time is not event availability time.

## Important limit

The [backend requirements](https://github.com/pinax-network/pinax-api/blob/4a033d5bd41bbae5b0f1ec3b5c21308ef9f57c11/README.md#L263-L280) require ClickHouse and separate Substreams pipelines. This review did not inspect the Hyperliquid ingestion path or prove its event completeness. Cache-control headers are a serving policy, not a point-in-time data contract.

## Questions to take into your own design

- Do records carry exchange event time, indexer observation time, and response time separately?
- Can a cache return an older response without the decision layer noticing?

## Why this score for a trading system

It exposes a direct market-data freshness trap, but the inspected API depends on separate pipelines and does not establish decision-time completeness or availability.

**Scope of this review:** We read the pinned README, cache documentation, and middleware. We did not query the service or audit its ingest pipelines.
