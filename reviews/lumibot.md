# A quote-based fill needs a timestamp qualification before a price

**Decision question:** Can a valid-looking bid or ask come from the wrong execution bar?

| Field | Review |
| --- | --- |
| Upstream | [LumiBot](https://github.com/Lumiwealth/lumibot) |
| Primary area | Backtesting & Simulation |
| Source commit | [2dfdda100cdc34e5acb46a7f13e8208a35aede72](https://github.com/Lumiwealth/lumibot/commit/2dfdda100cdc34e5acb46a7f13e8208a35aede72) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0](https://github.com/Lumiwealth/lumibot/blob/2dfdda100cdc34e5acb46a7f13e8208a35aede72/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | LumiBot has a quote guard that rejects missing timestamps or mismatched execution bars when the order requires current-bar evidence. The normal quote-fill path applies it before using bid/ask. Its coverage is conditional, and fallback fill models remain a separate audit boundary. |

## Mechanism worth inspecting

The [README](https://github.com/Lumiwealth/lumibot/blob/2dfdda100cdc34e5acb46a7f13e8208a35aede72/README.md#L589-L603) describes data-source routing and a spot-history route for crypto futures. The [architecture](https://github.com/Lumiwealth/lumibot/blob/2dfdda100cdc34e5acb46a7f13e8208a35aede72/docs/BACKTESTING_ARCHITECTURE.md#L23-L39) distinguishes regression from live replay. The [quote guard](https://github.com/Lumiwealth/lumibot/blob/2dfdda100cdc34e5acb46a7f13e8208a35aede72/lumibot/backtesting/backtesting_broker.py#L3659-L3686) checks timestamp qualification, and the [quote path](https://github.com/Lumiwealth/lumibot/blob/2dfdda100cdc34e5acb46a7f13e8208a35aede72/lumibot/backtesting/backtesting_broker.py#L2318-L2344) invokes it before using bid and ask.

## Important limit

The guard returns true when current-bar qualification is not required. We did not audit all fast paths, OHLC fallbacks, or venue-specific funding and margin. Spot history is not evidence of perpetual execution or basis behavior.

## Questions to take into your own design

- Which orders require current-bar evidence and which bypass that requirement?
- Does the result report expose quote-based versus fallback fills?

## Why this score for a trading system

3/5: Conditional quote-time qualification is a useful direct fill-model pattern, but its scope and alternative paths require further audit.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
