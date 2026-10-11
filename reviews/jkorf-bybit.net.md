# Bybit.Net — batch success has per-order outcomes

**Decision question:** Can a successful batch contain rejected orders?

| Field | Review |
| --- | --- |
| Upstream | [Bybit.Net](https://github.com/JKorf/Bybit.Net) |
| Primary area | Execution & Exchange Integration |
| Source commit | [c34540b0dc0f233bff0ec4e6365704994d5b50e7](https://github.com/JKorf/Bybit.Net/commit/c34540b0dc0f233bff0ec4e6365704994d5b50e7) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/JKorf/Bybit.Net/blob/c34540b0dc0f233bff0ec4e6365704994d5b50e7/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Makes mixed batch outcomes visible: the outer result may succeed while individual orders fail. A useful execution contract for per-order state, correlation and unresolved responses rather than a single batch boolean. |

## Project overview

Bybit.Net is a typed .NET client for Bybit REST and WebSocket APIs, including batch order operations. [Project documentation](https://github.com/JKorf/Bybit.Net/blob/c34540b0dc0f233bff0ec4e6365704994d5b50e7/README.md#L6-L12).

## Mechanism worth inspecting

The batch-create method checks transport and top-level return codes, then builds an individual `CallResult` for each per-order result. If all items fail it returns a global failure; with a mix it can return a successful batch containing failed items. [Batch outcome mapping](https://github.com/JKorf/Bybit.Net/blob/c34540b0dc0f233bff0ec4e6365704994d5b50e7/ByBit.Net/Clients/V5/Rest/BybitRestClientApiTrading.cs#L222-L244). [Documented batch warning](https://github.com/JKorf/Bybit.Net/blob/c34540b0dc0f233bff0ec4e6365704994d5b50e7/ByBit.Net/Interfaces/Clients/V5/IBybitRestClientApiTrading.cs#L462-L478).

## Important limit

A successful outer result is not successful acceptance of every order, and acceptance is not execution. The inspected mapping associates result and error lists by array position, so response cardinality and ordering are important contracts to verify at the adapter boundary.

## Questions to take into your own design

- Does every requested order receive its own accepted, rejected or unresolved record?
- Are result-list length and client-ID correlation checked before a partially successful batch is applied?

## Why this score for a trading system

3/5: a clear mixed-batch outcome reference, requiring identity checks and later fill reconciliation for a complete execution lifecycle.

**Scope of this review:** Batch-create response mapping; transport and exchange guarantees were not independently tested.
