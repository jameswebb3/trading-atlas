# Tickgrinder — Can simulated transport delays change event order without sleeping

**Decision question:** Can simulated transport delays change event order without sleeping?

| Field | Review |
| --- | --- |
| Upstream | [Tickgrinder](https://github.com/Ameobea/tickgrinder) |
| Primary area | Backtesting & Simulation |
| Source commit | [f2ccd640b173cb17b0af4e04df9b203935eb2dc2](https://github.com/Ameobea/tickgrinder/commit/f2ccd640b173cb17b0af4e04df9b203935eb2dc2) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/Ameobea/tickgrinder/blob/f2ccd640b173cb17b0af4e04df9b203935eb2dc2/License.txt) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | A historical reference for separating market, broker and client clocks in a simulator. The inspected implementation is unfinished, so the useful takeaway is the event-queue design rather than adoption of the platform. |

## Project overview

Tickgrinder is an early event-driven trading platform. Its SimBroker models ticks, commands and responses through a simulated event queue. [Project documentation](https://github.com/Ameobea/tickgrinder/blob/f2ccd640b173cb17b0af4e04df9b203935eb2dc2/broker_shims/simbroker/README.md#L3-L24).

## Mechanism worth inspecting

The SimBroker schedules incoming actions at broker time plus processing delay, then schedules client ticks and responses after network delay. [Queue and clocks](https://github.com/Ameobea/tickgrinder/blob/f2ccd640b173cb17b0af4e04df9b203935eb2dc2/broker_shims/simbroker/src/lib.rs#L168-L244).

## Important limit

The documentation explicitly says this subsystem is unfinished; the inspected push_msg implementation is commented out. Treat the queue design as a historical reference, not a working broker certification. [Incomplete path](https://github.com/Ameobea/tickgrinder/blob/f2ccd640b173cb17b0af4e04df9b203935eb2dc2/broker_shims/simbroker/src/lib.rs#L282-L289).

## Questions to take into your own design

- Can simulated transport delays change event order without sleeping?
- What breaks ties between simultaneous market, command and response events in your simulation?

## Why this score for a trading system

2/5: relevant event timing in source, with explicit unfinished delivery paths and an obsolete platform stack.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
