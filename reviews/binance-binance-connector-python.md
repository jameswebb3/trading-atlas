# Binance Python Connectors — Which operations are eligible for an automatic HTTP retry

**Decision question:** Which operations are eligible for an automatic HTTP retry?

| Field | Review |
| --- | --- |
| Upstream | [Binance Python Connectors](https://github.com/binance/binance-connector-python) |
| Primary area | Execution & Exchange Integration |
| Source commit | [3698bb195e38ce6ec3be2cb6103fcc9a0d4abb0a](https://github.com/binance/binance-connector-python/commit/3698bb195e38ce6ec3be2cb6103fcc9a0d4abb0a) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/binance/binance-connector-python/blob/3698bb195e38ce6ec3be2cb6103fcc9a0d4abb0a/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Restricts automatic retries by HTTP method and error class rather than retrying every failed call. A strong reference for keeping query recovery separate from uncertain trading actions. |

## Project overview

Binance's collection of generated Python SDKs shares common transport and request-handling utilities. [Project documentation](https://github.com/binance/binance-connector-python/blob/3698bb195e38ce6ec3be2cb6103fcc9a0d4abb0a/README.md#L1-L24).

## Mechanism worth inspecting

The common retry predicate allows GET and DELETE, excludes other methods, requires remaining attempts and limits response-based retries to selected server-error statuses. Network errors without a response can be retried only after the method gate. [Retry predicate](https://github.com/binance/binance-connector-python/blob/3698bb195e38ce6ec3be2cb6103fcc9a0d4abb0a/common/src/binance_common/utils.py#L344-L368); [configuration example](https://github.com/binance/binance-connector-python/blob/3698bb195e38ce6ec3be2cb6103fcc9a0d4abb0a/clients/derivatives_trading_usds_futures/docs/rest_api/retries.md#L1-L20).

## Important limit

HTTP-method eligibility is an initial policy, not a proof of an operation's business outcome. A timed-out cancellation still needs order reconciliation; the absence of a POST retry does not recover an unacknowledged order.

## Questions to take into your own design

- Which failures are retryable reads and which leave a trading action uncertain?
- How is a timed-out cancel reconciled before a replacement order is allowed?

## Why this score for a trading system

4/5: a small, directly inspectable method gate addresses a concrete duplicate-order risk at the exchange boundary.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
