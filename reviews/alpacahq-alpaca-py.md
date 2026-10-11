# Alpaca-py — Does a retry option actually disable retries when set to zero

**Decision question:** Does a retry option actually disable retries when set to zero?

| Field | Review |
| --- | --- |
| Upstream | [Alpaca-py](https://github.com/alpacahq/alpaca-py) |
| Primary area | Execution & Exchange Integration |
| Source commit | [c803f2d1af7a3c5eb69c2a7ff6b0139e400c4cb1](https://github.com/alpacahq/alpaca-py/commit/c803f2d1af7a3c5eb69c2a7ff6b0139e400c4cb1) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/alpacahq/alpaca-py/blob/c803f2d1af7a3c5eb69c2a7ff6b0139e400c4cb1/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Provides a concrete retry-configuration caution: zero does not override the default attempt count. Review the effective settings and operation semantics before assuming a write request will run once. |

## Project overview

Alpaca's Python SDK exposes REST, WebSocket and SSE interfaces for trading, market data and brokerage applications. [Project documentation](https://github.com/alpacahq/alpaca-py/blob/c803f2d1af7a3c5eb69c2a7ff6b0139e400c4cb1/README.md#L33-L35).

## Mechanism worth inspecting

The REST client starts with default retry settings and only replaces retry_attempts when the supplied value is positive. Its request loop retries configured HTTP status codes without a method-specific gate in the inspected branch. [Configuration](https://github.com/alpacahq/alpaca-py/blob/c803f2d1af7a3c5eb69c2a7ff6b0139e400c4cb1/alpaca/common/rest.py#L68-L83); [request loop and error classification](https://github.com/alpacahq/alpaca-py/blob/c803f2d1af7a3c5eb69c2a7ff6b0139e400c4cb1/alpaca/common/rest.py#L122-L135), [response check](https://github.com/alpacahq/alpaca-py/blob/c803f2d1af7a3c5eb69c2a7ff6b0139e400c4cb1/alpaca/common/rest.py#L194-L210).

## Important limit

Passing retry_attempts=0 does not replace the default in this constructor. This source observation does not establish that an order was duplicated: endpoint semantics and request identities must be checked separately.

## Questions to take into your own design

- Are requested retry settings recorded alongside the effective attempt policy?
- Which order errors require reconciliation before a retry?

## Why this score for a trading system

3/5: useful for verifying exchange-adapter retry contracts, but the inspected HTTP loop does not itself establish safe order retry semantics.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
