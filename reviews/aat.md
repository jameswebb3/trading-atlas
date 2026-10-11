# AAT: retaining a fill that precedes its acknowledgement

**Decision question:** How can an execution engine retain a fill that arrives before its order acknowledgement?

| Field | Review |
| --- | --- |
| Upstream | [AsyncAlgoTrading/aat](https://github.com/AsyncAlgoTrading/aat) |
| Primary area | Execution & Exchange Integration |
| Source commit | [c4a07d4102a811c779957033aa26a598c1795cdb](https://github.com/AsyncAlgoTrading/aat/commit/c4a07d4102a811c779957033aa26a598c1795cdb) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/AsyncAlgoTrading/aat/blob/c4a07d4102a811c779957033aa26a598c1795cdb/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | AAT records a pending action before sending the order, then matches an early trade against it and ignores known duplicate trades. Its path still raises when the trade cannot be matched to any tracked action. |

## Project overview

Asynchronous trading framework using the same strategy class for backtesting and live trading. Separates trading, risk, and execution engines, and tracks pending intent before an order send completes.

[Project documentation](https://github.com/AsyncAlgoTrading/aat/blob/c4a07d4102a811c779957033aa26a598c1795cdb/README.md#L10-L38).

## Mechanism worth inspecting

AAT describes an [asynchronous execution engine](https://github.com/AsyncAlgoTrading/aat/blob/c4a07d4102a811c779957033aa26a598c1795cdb/README.md#L10-L24). Its [`newOrder`](https://github.com/AsyncAlgoTrading/aat/blob/c4a07d4102a811c779957033aa26a598c1795cdb/aat/engine/dispatch/execution/execution.py#L44-L70) appends the order and strategy to `_pending_action` before awaiting the exchange send. That preserves enough context if an execution event is dispatched before the send call returns.

In [`onTrade`](https://github.com/AsyncAlgoTrading/aat/blob/c4a07d4102a811c779957033aa26a598c1795cdb/aat/engine/dispatch/execution/execution.py#L103-L140), the engine first looks for a pending order, then a past order, then a pending action. A past order is ignored as a duplicate; a trade matched to the pending action is attached to its strategy and moved into the pending-order map if unfinished. This is an explicit model for event-order permutations, not just a comment saying they might occur.

## Boundary and practical use

An unmatched early trade [raises an exception](https://github.com/AsyncAlgoTrading/aat/blob/c4a07d4102a811c779957033aa26a598c1795cdb/aat/engine/dispatch/execution/execution.py#L118-L133). The source does not establish what a venue adapter should do with trades lacking stable order IDs or with repeated events after restart. The reusable idea is to register intent before crossing an asynchronous boundary and test several ACK/trade permutations.

## Why this score for a trading system

Fill-before-ACK handling is a direct trading execution race, backed by an inspectable pending-action path; restart behavior remains unproved.

**Scope of this review:** We read the pinned README, API documentation, and execution dispatcher. We did not run AAT or verify its behavior with an exchange.
