# Go Quant Tick: recovery needs a verifiable cursor

**Decision question:** What proves a Hyperliquid trade stream is complete after reconnect?

| Field | Review |
| --- | --- |
| Upstream | [globophobe/go-quant-tick](https://github.com/globophobe/go-quant-tick) |
| Primary area | Market Data & Ingestion |
| Source commit | [a8feab89bda0235ff64063f59a865185b6a3a7b5](https://github.com/globophobe/go-quant-tick/commit/a8feab89bda0235ff64063f59a865185b6a3a7b5) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/globophobe/go-quant-tick/blob/a8feab89bda0235ff64063f59a865185b6a3a7b5/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Keeps exchange time, receipt time, and a stable trade ID separate when ingesting Hyperliquid trades. If recentTrades no longer contains the cursor, recovery returns no rows and relies on WebSocket replay; completeness is not proved by that return. |

## Mechanism worth inspecting

The [README](https://github.com/globophobe/go-quant-tick/blob/a8feab89bda0235ff64063f59a865185b6a3a7b5/README.md#L1-L11) describes WebSocket trade aggregation and filtering. In the Hyperliquid parser, each trade becomes an event with a UID built from exchange time, coin, and trade ID; [exchange timestamp and local receipt time are separate](https://github.com/globophobe/go-quant-tick/blob/a8feab89bda0235ff64063f59a865185b6a3a7b5/quanttick/exchanges/hyperliquid_protocol.go#L40-L64). The recovery path requests recent trades for a coin and slices them after the last remembered UID ([request construction](https://github.com/globophobe/go-quant-tick/blob/a8feab89bda0235ff64063f59a865185b6a3a7b5/quanttick/exchanges/hyperliquid_recovery.go#L16-L64), [cursor handling](https://github.com/globophobe/go-quant-tick/blob/a8feab89bda0235ff64063f59a865185b6a3a7b5/quanttick/exchanges/hyperliquid_recovery.go#L84-L98). This is a useful separation between market event time, ingestion time, and continuity evidence.

## Important limit

When the cursor is absent from recentTrades, the inspected function returns `nil, nil` with a comment that the WebSocket reconnect snapshot also replays missed trades. That return does not itself show which UIDs arrived, whether the recentTrades window was exhausted, or whether the snapshot covered the gap. A consumer needs an explicit unknown-coverage state until the replay is verified.

## Questions to take into your own design

- Do you retain both exchange and receipt times for every trade?
- If a cursor falls outside the REST window, where is the missing interval recorded?
- Which UID sequence or replay evidence closes a reconnect gap?

## Why this score for a trading system

Exchange and receipt clocks plus trade identity apply directly to market-data ingestion, but the missing-cursor recovery path does not prove completeness.

**Scope of this review:** We read the pinned README and Hyperliquid parsing/recovery paths. We did not run a reconnection, inspect every WebSocket snapshot path, or test venue behavior.
