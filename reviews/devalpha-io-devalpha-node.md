# DevAlpha — Does an event-sourced backtest preserve real order timing

**Decision question:** Does an event-sourced backtest preserve real order timing?

| Field | Review |
| --- | --- |
| Upstream | [DevAlpha](https://github.com/devalpha-io/devalpha-node) |
| Primary area | Backtesting & Simulation |
| Source commit | [d51f5ca24207bfdc51a9234d6e7acb41737ac506](https://github.com/devalpha-io/devalpha-node/commit/d51f5ca24207bfdc51a9234d6e7acb41737ac506) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0](https://github.com/devalpha-io/devalpha-node/blob/d51f5ca24207bfdc51a9234d6e7acb41737ac506/LICENSE.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Separates order events in a compact stream architecture, but its backtest broker places and fills orders in one cycle. Suitable for simple event-flow examples. |

## Project overview

Small TypeScript trading framework organized around streams and event-sourced consumers. [Project documentation](https://github.com/devalpha-io/devalpha-node/blob/d51f5ca24207bfdc51a9234d6e7acb41737ac506/README.md#L8-L19).

## Mechanism worth inspecting

Backtest middleware dispatches ORDER_CREATED, ORDER_PLACED and ORDER_FILLED events. Placement and fill happen in the same processing cycle with the placed order's timestamp. [Broker middleware](https://github.com/devalpha-io/devalpha-node/blob/d51f5ca24207bfdc51a9234d6e7acb41737ac506/lib/middleware/createBrokerBacktest.ts#L19-L63), [configuration](https://github.com/devalpha-io/devalpha-node/blob/d51f5ca24207bfdc51a9234d6e7acb41737ac506/README.md#L93-L114).

## Important limit

The middleware explicitly assumes transactions can happen at the historical time. The event names alone therefore do not model exchange latency, acceptance failure or asynchronous fills. [Declared simplification](https://github.com/devalpha-io/devalpha-node/blob/d51f5ca24207bfdc51a9234d6e7acb41737ac506/lib/middleware/createBrokerBacktest.ts#L19-L23).

## Questions to take into your own design

- Does an event-sourced backtest preserve real order timing?
- Can acceptance failures and delayed fills occur separately in the replay event stream?

## Why this score for a trading system

2/5: direct trading code with a useful caution; immediate-fill timing is too simplified for execution-sensitive conclusions.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
