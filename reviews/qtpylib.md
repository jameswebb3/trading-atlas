# QTPyLib: audit what an on_fill callback actually means

**Decision question:** Does an advertised fill callback run for every execution or only terminal order status?

| Field | Review |
| --- | --- |
| Upstream | [QTPyLib](https://github.com/ranaroussi/qtpylib) |
| Primary area | Execution & Exchange Integration |
| Source commit | [2c1af0eef85fb3205d8fcefc41a421b074b371de](https://github.com/ranaroussi/qtpylib/commit/2c1af0eef85fb3205d8fcefc41a421b074b371de) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/ranaroussi/qtpylib/blob/2c1af0eef85fb3205d8fcefc41a421b074b371de/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Provides event-driven strategies and an Interactive Brokers adapter. The inspected callback path invokes on_fill after a FILLED status, showing why a framework's callback name must be checked against its handling of partial executions and cancellations. |

## Project overview

A Python trading framework supports market-event callbacks, backtests, and broker trading. [Project documentation](https://github.com/ranaroussi/qtpylib/blob/2c1af0eef85fb3205d8fcefc41a421b074b371de/README.rst#L38-L41).

## Mechanism worth inspecting

The [algorithm guide](https://github.com/ranaroussi/qtpylib/blob/2c1af0eef85fb3205d8fcefc41a421b074b371de/docs/source/algo.rst#L4-L23) describes market and fill callbacks. The [broker handler](https://github.com/ranaroussi/qtpylib/blob/2c1af0eef85fb3205d8fcefc41a421b074b371de/qtpylib/broker.py#L289-L341) cleans up canceled orders and invokes trade registration/on_fill on FILLED status.

## Important limit

The [quantity lookup](https://github.com/ranaroussi/qtpylib/blob/2c1af0eef85fb3205d8fcefc41a421b074b371de/qtpylib/broker.py#L316-L323) substitutes one after missing history. The inspected branch does not explicitly process partial executions, so the guide's fill wording should not be taken as an audited per-execution contract.

## Questions to take into your own design

- Does a fill callback carry an execution identity and incremental quantity?
- Can missing order history produce an indeterminate state instead of a invented quantity?

## Why this score for a trading system

2/5: readable broker-event adaptation, constrained by terminal-status semantics and a quantity fallback unsuitable as reliable evidence.

**Scope of this review:** README, algorithm and generated broker API documentation, broker order-status source.
