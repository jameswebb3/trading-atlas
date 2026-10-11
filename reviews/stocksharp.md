# An early trade can be held until its order identity is known

**Decision question:** How should an execution event be handled before its order is mapped?

| Field | Review |
| --- | --- |
| Upstream | [StockSharp](https://github.com/StockSharp/StockSharp) |
| Primary area | Execution & Exchange Integration |
| Source commit | [cfcc246e6d2de3a22b478f22e52f7c02e9f3ead4](https://github.com/StockSharp/StockSharp/commit/cfcc246e6d2de3a22b478f22e52f7c02e9f3ead4) |
| Reviewed | 2026-09-26 |
| Declared license | [StockSharp proprietary terms; not a general open-source license](https://github.com/StockSharp/StockSharp/blob/cfcc246e6d2de3a22b478f22e52f7c02e9f3ead4/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Its transaction ordering manager suspends trades with unknown order identity and releases them after order information supplies a matching key. That is a concrete execution pattern, but these buffers are in memory and reset clears them. The pinned repository license declares proprietary terms. |

## Mechanism worth inspecting

The [README](https://github.com/StockSharp/StockSharp/blob/cfcc246e6d2de3a22b478f22e52f7c02e9f3ead4/README.md#L9-L15) describes broker integration; the [Algo overview](https://github.com/StockSharp/StockSharp/blob/cfcc246e6d2de3a22b478f22e52f7c02e9f3ead4/Algo/README.md#L5-L13) explains message adapters. The [suspension branch](https://github.com/StockSharp/StockSharp/blob/cfcc246e6d2de3a22b478f22e52f7c02e9f3ead4/Algo/TransactionOrderingManager.cs#L247-L287) buffers unmapped trades, and the [release path](https://github.com/StockSharp/StockSharp/blob/cfcc246e6d2de3a22b478f22e52f7c02e9f3ead4/Algo/TransactionOrderingManager.cs#L361-L400) removes them by known order ID. The [license notice](https://github.com/StockSharp/StockSharp/blob/cfcc246e6d2de3a22b478f22e52f7c02e9f3ead4/LICENSE#L6-L22) limits the source to proprietary terms.

## Important limit

The [reset path](https://github.com/StockSharp/StockSharp/blob/cfcc246e6d2de3a22b478f22e52f7c02e9f3ead4/Algo/TransactionOrderingManager.cs#L70-L85) clears associations and suspended messages. We did not establish persistence, expiry, deduplication, or full recovery. Extract the design question; adoption or code reuse requires checking the applicable rights.

## Questions to take into your own design

- Can an unmatched execution survive restart and eventually be reconciled?
- What bounds the buffer and escalates a permanently unmatched trade?

## Why this score for a trading system

2/5: Trade-before-order association is directly relevant, but proprietary licensing and unverified recovery make this a narrow design reference.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
