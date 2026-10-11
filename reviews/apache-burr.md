# Apache Burr: state contracts are useful but only partly checked

**Decision question:** Can an agent step declare which state it reads and writes, and does that declaration enforce itself?

| Field | Review |
| --- | --- |
| Upstream | [apache/burr](https://github.com/apache/burr) |
| Primary area | Agents & Decision Systems |
| Source commit | [8161159148e9b9c795f683625d6721f2c955f9d8](https://github.com/apache/burr/commit/8161159148e9b9c795f683625d6721f2c955f9d8) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/apache/burr/blob/8161159148e9b9c795f683625d6721f2c955f9d8/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Defines agent workflows as state machines with declared reads and writes, plus validation of selected action results. Its static read check skips unavailable source and only sees literal state subscriptions; declarations alone are not a complete isolation boundary. |

## Mechanism worth inspecting

The [README example](https://github.com/apache/burr/blob/8161159148e9b9c795f683625d6721f2c955f9d8/README.md#L81-L115) attaches `reads` and `writes` to state-machine actions. The [action helper](https://github.com/apache/burr/blob/8161159148e9b9c795f683625d6721f2c955f9d8/burr/core/action.py#L55-L100) inspects source AST for literal `state["key"]` reads not declared by the action. The [application path](https://github.com/apache/burr/blob/8161159148e9b9c795f683625d6721f2c955f9d8/burr/core/application.py#L92-L127) also checks result shape and rejects invalid single-step returns. These are concrete ways to make agent handoffs inspectable.

## Important limit

The AST check returns early when the declared list is empty, source is unavailable, or the state parameter is not recognized; dynamic key access is outside the shown pattern. This is a helpful lint, not a complete security or evidence-integrity guarantee.

## Questions to take into your own design

- Which state fields may each step consume and produce?
- Are undeclared reads caught in the actual execution mode?
- Do malformed or missing outputs stop the next stage?

## Why this score for a trading system

Declared agent state reads can improve research automation, but the inspected linter skips paths and does not enforce trading permissions.

**Scope of this review:** We read the pinned README, action read checker, and application result validator. We did not run Burr or inspect every state persistence backend.
