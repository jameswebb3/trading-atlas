# Blockscout: route reorg notifications to the affected indexers

**Decision question:** What does a rollup reorg monitor actually detect, and who repairs the derived data?

| Field | Review |
| --- | --- |
| Upstream | [Blockscout](https://github.com/blockscout/blockscout) |
| Primary area | Market Data & Ingestion |
| Source commit | [3ea5c7ac7eea9a748f1fe7f932c4358194b0309e](https://github.com/blockscout/blockscout/commit/3ea5c7ac7eea9a748f1fe7f932c4358194b0309e) |
| Reviewed | 2026-09-26 |
| Declared license | [LicenseRef-Blockscout, source-available commercial restrictions](https://github.com/blockscout/blockscout/blob/3ea5c7ac7eea9a748f1fe7f932c4358194b0309e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Provides an EVM explorer and indexing services. Its rollup monitor routes an observed L1 height decrease to dependent fetchers, making repair ownership explicit; that trigger alone cannot detect every canonical-chain replacement. |

## Project overview

An EVM explorer indexes transactions, contracts, and related chain data. The inspected module coordinates L1 reorg notifications for selected rollup fetchers. [Project documentation](https://github.com/blockscout/blockscout/blob/3ea5c7ac7eea9a748f1fe7f932c4358194b0309e/README.md#L1-L35).

## Mechanism worth inspecting

The [module documentation](https://github.com/blockscout/blockscout/blob/3ea5c7ac7eea9a748f1fe7f932c4358194b0309e/apps/indexer/lib/indexer/fetcher/rollup_l1_reorg_monitor.ex#L3-L9) assigns reorg handling to consumers of per-module queues. [Initialization](https://github.com/blockscout/blockscout/blob/3ea5c7ac7eea9a748f1fe7f932c4358194b0309e/apps/indexer/lib/indexer/fetcher/rollup_l1_reorg_monitor.ex#L102-L124) registers only fetchers that require the monitor. The [loop](https://github.com/blockscout/blockscout/blob/3ea5c7ac7eea9a748f1fe7f932c4358194b0309e/apps/indexer/lib/indexer/fetcher/rollup_l1_reorg_monitor.ex#L147-L167) pushes the new height to those consumers when the observed tip height decreases.

## Important limit

Equal-height or advancing-height canonical replacements do not satisfy this module's trigger; this is a limitation of the inspected monitor, not a claim about every Blockscout reorg path. At this commit the [license](https://github.com/blockscout/blockscout/blob/3ea5c7ac7eea9a748f1fe7f932c4358194b0309e/LICENSE#L134-L183) contains commercial-use and derivative-distribution restrictions, so it must not be presented as an unrestricted open-source dependency.

## Questions to take into your own design

- Does every derived-data consumer own a repair cursor and an acknowledgement?
- Does detection compare canonical block identity, or only whether height moved backwards?

## Why this score for a trading system

2/5: an instructive coordination pattern, limited by the monitor's detection scope and a restrictive source-available license. It is an architectural case study rather than a default implementation choice.

**Scope of this review:** README, documented rollup monitor and its full loop, and relevant license restrictions; other reorg handlers are outside this review.
