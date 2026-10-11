# Roboquant: an event's time is its availability time

**Decision question:** What timestamp should order a replayed market event?

| Field | Review |
| --- | --- |
| Upstream | [Roboquant](https://github.com/neurallayer/roboquant) |
| Primary area | Backtesting & Simulation |
| Source commit | [c82664a8476683c74d50b7f82b65fd5ec5bdda7e](https://github.com/neurallayer/roboquant/commit/c82664a8476683c74d50b7f82b65fd5ec5bdda7e) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/neurallayer/roboquant/blob/c82664a8476683c74d50b7f82b65fd5ec5bdda7e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Defines event time as the moment all contained items became available and sorts events by that time. Its convenience price map keeps only the last price item for an asset within an event, so replay design must preserve the full item list where multiple updates matter. |

## Mechanism worth inspecting

The [overview](https://github.com/neurallayer/roboquant/blob/c82664a8476683c74d50b7f82b65fd5ec5bdda7e/README.md#L67-L77) presents event-based strategy and broker integration. The [Event type](https://github.com/neurallayer/roboquant/blob/c82664a8476683c74d50b7f82b65fd5ec5bdda7e/roboquant/src/org/roboquant/common/Event.kt#L5-L12) documents its clock as when items became available. Its [price projection](https://github.com/neurallayer/roboquant/blob/c82664a8476683c74d50b7f82b65fd5ec5bdda7e/roboquant/src/org/roboquant/common/Event.kt#L14-L29) retains the last price per asset, while [ordering](https://github.com/neurallayer/roboquant/blob/c82664a8476683c74d50b7f82b65fd5ec5bdda7e/roboquant/src/org/roboquant/common/Event.kt#L54-L58) compares event times. That distinction makes an easy-to-miss data reduction visible.

## Important limit

The event object trusts the supplied time; it cannot prove the feed actually arrived then. Multiple updates batched under one time can lose sequence detail if a strategy uses the convenience map rather than the full items list.

## Questions to take into your own design

- Is replay ordered by observed availability rather than exchange event time alone?
- Are multiple updates at one timestamp retained where sequence affects decisions?

## Why this score for a trading system

An explicit available-time event clock is a useful replay contract, but this small abstraction does not validate source publication or fill mechanics.

**Scope of this review:** We read the pinned README and event implementation. We did not run a strategy.
