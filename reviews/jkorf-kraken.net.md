# Kraken.Net — How is a venue-side cancellation deadline different from a client timeout

**Decision question:** How is a venue-side cancellation deadline different from a client timeout?

| Field | Review |
| --- | --- |
| Upstream | [Kraken.Net](https://github.com/JKorf/Kraken.Net) |
| Primary area | Execution & Exchange Integration |
| Source commit | [76f271a3752c3c96d9b3a168e6334d9bce080ca1](https://github.com/JKorf/Kraken.Net/commit/76f271a3752c3c96d9b3a168e6334d9bce080ca1) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/JKorf/Kraken.Net/blob/76f271a3752c3c96d9b3a168e6334d9bce080ca1/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Exposes a venue cancellation deadline separately from immediate cancel and execution history. Useful when designing an order watchdog, provided its scope, refresh policy and confirmation path are explicit. |

## Project overview

A typed .NET client for Kraken REST and WebSocket interfaces, with rate limiting and client-side order-book support. [Project documentation](https://github.com/JKorf/Kraken.Net/blob/76f271a3752c3c96d9b3a168e6334d9bce080ca1/README.md#L8-L17).

## Mechanism worth inspecting

The futures trading client exposes cancel-all-after as a dedicated authenticated request, converting a TimeSpan into a whole-second timeout. It separately exposes immediate cancellation and execution-history retrieval. [Cancellation interfaces](https://github.com/JKorf/Kraken.Net/blob/76f271a3752c3c96d9b3a168e6334d9bce080ca1/Kraken.Net/Clients/FuturesApi/Rest/KrakenRestClientFuturesApiTrading.cs#L253-L306).

## Important limit

A callable deadline endpoint does not prove a watchdog is refreshed correctly or that a cancellation was confirmed. Its account scope and venue semantics must be established before use; a local socket timeout is a different event.

## Questions to take into your own design

- What evidence confirms that the venue accepted the current cancellation deadline?
- Which order scope and renewal failure policy does the watchdog cover?

## Why this score for a trading system

3/5: a direct order-protection interface, but the inspected method does not establish a complete watchdog lifecycle.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
