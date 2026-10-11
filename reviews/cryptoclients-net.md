# CryptoClients.Net: shared APIs should expose capability absence

**Decision question:** How should a multi-exchange API handle an unsupported futures operation?

| Field | Review |
| --- | --- |
| Upstream | [CryptoClients.Net](https://github.com/JKorf/CryptoClients.Net) |
| Primary area | Execution & Exchange Integration |
| Source commit | [a84d5b8d743fe5192533100e573431cb86976681](https://github.com/JKorf/CryptoClients.Net/commit/a84d5b8d743fe5192533100e573431cb86976681) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/JKorf/CryptoClients.Net/blob/a84d5b8d743fe5192533100e573431cb86976681/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Discovers exchange capabilities by operation and trading mode, then returns an explicit failure when client-ID futures order lookup or cancellation is unavailable. This avoids pretending that every exchange implements the same order lifecycle. |

## Mechanism worth inspecting

The [overview](https://github.com/JKorf/CryptoClients.Net/blob/a84d5b8d743fe5192533100e573431cb86976681/README.md#L11-L23) warns that shared API coverage varies by exchange, operation, and trading mode. The [API map](https://github.com/JKorf/CryptoClients.Net/blob/a84d5b8d743fe5192533100e573431cb86976681/docs/ai-api-map.md#L25-L34) treats capability lookup and null handling as the support check. The [futures client-ID methods](https://github.com/JKorf/CryptoClients.Net/blob/a84d5b8d743fe5192533100e573431cb86976681/CryptoClients.Net/Clients/Rest/ExchangeRestClient.FuturesOrderClientId.cs#L16-L45) resolve a matching client for the requested trading mode and return a structured failure when none exists. This makes absence a first-class result.

## Important limit

A capability existing in an adapter does not prove that its venue-specific fields, rate limits, or response timing are correct. The wrapper covers many exchanges; for a single venue its main value is the explicit support matrix, not abstraction for its own sake.

## Questions to take into your own design

- Are unsupported operations rejected before an order is sent?
- Does a shared interface preserve venue-specific client IDs and error meanings?

## Why this score for a trading system

Explicit capability discovery is directly useful for exchange integration, though one-venue systems still need venue-specific order and error semantics.

**Scope of this review:** We read the pinned README, API map, and futures client-ID dispatch code. We did not call an exchange.
