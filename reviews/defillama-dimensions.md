# DefiLlama Dimensions: read the metric convention before comparing protocols

**Decision question:** Does an open-interest history preserve the same units, market coverage, and observation time?

| Field | Review |
| --- | --- |
| Upstream | [DefiLlama Dimensions](https://github.com/DefiLlama/dimension-adapters) |
| Primary area | Data Quality & Lineage |
| Source commit | [48b5eda5da0ef831cf883bb0091b1daafe53c283](https://github.com/DefiLlama/dimension-adapters/commit/48b5eda5da0ef831cf883bb0091b1daafe53c283) |
| Reviewed | 2026-09-26 |
| Declared license | [ISC declared in package.json](https://github.com/DefiLlama/dimension-adapters/blob/48b5eda5da0ef831cf883bb0091b1daafe53c283/package.json#L21) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Publishes auditable definitions for fees, volume, and open interest. Its perpetual adapter illustrates how changing sources and counting conventions alter a series; a recent historical request can also fall back to current data. |

## Project overview

A collection of adapters computes protocol metrics from chain data and external endpoints. The shared contract distinguishes interval flows from end-of-period open interest. [Project documentation](https://github.com/DefiLlama/dimension-adapters/blob/48b5eda5da0ef831cf883bb0091b1daafe53c283/adapters/types.ts#L144-L168).

## Mechanism worth inspecting

The [shared fetch contract](https://github.com/DefiLlama/dimension-adapters/blob/48b5eda5da0ef831cf883bb0091b1daafe53c283/adapters/types.ts#L25-L58) carries explicit time and block boundaries. The [open-interest adapter](https://github.com/DefiLlama/dimension-adapters/blob/48b5eda5da0ef831cf883bb0091b1daafe53c283/open-interest/hyperliquid-perp-oi.ts#L6-L28) switches sources at a coverage threshold and halves the older series. Its [new-source helper](https://github.com/DefiLlama/dimension-adapters/blob/48b5eda5da0ef831cf883bb0091b1daafe53c283/helpers/hyperliquid.ts#L463-L495) also applies a declared one-sided convention and reports separate default-market and deployer totals. These are inspectable metric definitions rather than interchangeable numbers.

## Important limit

The [snapshot fallback](https://github.com/DefiLlama/dimension-adapters/blob/48b5eda5da0ef831cf883bb0091b1daafe53c283/helpers/hyperliquid.ts#L498-L518) substitutes the current API response for recent requested dates when the indexer fails; older failures return null. The aggregation skips null market responses. The factor-of-two convention is an upstream choice shown in code, not independently validated here. Preserve original units, source, and collection time before adopting it.

## Questions to take into your own design

- Can a fallback change the observation time without changing the field name?
- Does a missing market make an aggregate incomplete, or appear as zero contribution?

## Why this score for a trading system

3/5: directly relevant, transparent metric contracts and a concrete historical-data hazard. Snapshot substitution and incomplete-market aggregation prevent a stronger data-reliability score.

**Scope of this review:** README, adapter contract, metric methodology documentation, one perpetual adapter, and its snapshot helper; no validation of reported metric values.
