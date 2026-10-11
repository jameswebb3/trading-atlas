# Replay time advances with events, but equal-time ordering still needs a rule

**Decision question:** Can asynchronous handlers observe a different order during a replay?

| Field | Review |
| --- | --- |
| Upstream | [Basana](https://github.com/gbeced/basana) |
| Primary area | Backtesting & Simulation |
| Source commit | [8e722becd8255db70cce1f139e0f4cebfe604b48](https://github.com/gbeced/basana/commit/8e722becd8255db70cce1f139e0f4cebfe604b48) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/gbeced/basana/blob/8e722becd8255db70cce1f139e0f4cebfe604b48/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Basana's replay dispatcher rejects backward timestamps, advances time from events, and waits for same-timestamp work before moving forward. Scheduled jobs run before events at that timestamp. Multiple equal-time event handlers use a concurrency pool, so timestamp monotonicity alone does not define every state transition. |

## Mechanism worth inspecting

The [README](https://github.com/gbeced/basana/blob/8e722becd8255db70cce1f139e0f4cebfe604b48/README.md#L9-L15) introduces asynchronous trading and backtesting, and the [exchange reference](https://github.com/gbeced/basana/blob/8e722becd8255db70cce1f139e0f4cebfe604b48/docs/backtesting_exchange.rst#L6-L24) exposes fills and order events. The [dispatcher](https://github.com/gbeced/basana/blob/8e722becd8255db70cce1f139e0f4cebfe604b48/basana/core/dispatcher/backtesting.py#L55-L104) checks ascending time, processes scheduled jobs first, and waits for the concurrent equal-time event group.

## Important limit

A shared timestamp does not settle exchange-event order, local receipt order, or callback interleaving. This review covers the replay dispatcher, not proof of full live/replay equivalence or a perpetual-futures fill model.

## Questions to take into your own design

- Can equal-time fills and cancels produce different outcomes under handler interleaving?
- Is the scheduling precedence part of the replay specification?

## Why this score for a trading system

3/5: The inspected event-clock boundary is directly useful for replay design, with unresolved equal-time and live-ordering assumptions.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
