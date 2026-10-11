# KuCoin Universal SDK — Does a successful HTTP response prove the exchange operation succeeded

**Decision question:** Does a successful HTTP response prove the exchange operation succeeded?

| Field | Review |
| --- | --- |
| Upstream | [KuCoin Universal SDK](https://github.com/Kucoin/kucoin-universal-sdk) |
| Primary area | Execution & Exchange Integration |
| Source commit | [c2f39bdb8b7d5f31cfb3fd532f9baf2f09fd8f12](https://github.com/Kucoin/kucoin-universal-sdk/commit/c2f39bdb8b7d5f31cfb3fd532f9baf2f09fd8f12) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/Kucoin/kucoin-universal-sdk/blob/c2f39bdb8b7d5f31cfb3fd532f9baf2f09fd8f12/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Checks exchange business errors before returning typed response data. Its transport loop also illustrates why retry control must be inspected separately from HTTP and API error handling. |

## Project overview

KuCoin's generated SDK spans several languages and exposes unified trading, futures and broker interfaces. [Project documentation](https://github.com/Kucoin/kucoin-universal-sdk/blob/c2f39bdb8b7d5f31cfb3fd532f9baf2f09fd8f12/README.md#L6-L23).

## Mechanism worth inspecting

The Go transport checks HTTP status, decodes the common API envelope, attaches rate-limit metadata and calls its business-error method before decoding data. Separately, its transport retry loop repeats client requests after errors. [Envelope validation](https://github.com/Kucoin/kucoin-universal-sdk/blob/c2f39bdb8b7d5f31cfb3fd532f9baf2f09fd8f12/sdk/golang/internal/infra/default_transport.go#L287-L315); [transport retries](https://github.com/Kucoin/kucoin-universal-sdk/blob/c2f39bdb8b7d5f31cfb3fd532f9baf2f09fd8f12/sdk/golang/internal/infra/default_transport.go#L71-L114).

## Important limit

The inspected retry loop has no HTTP-method gate: shouldRetry controls whether it sleeps, while the loop continues after any client error. That is a source-level caution, not evidence of a duplicated live order.

## Questions to take into your own design

- Are HTTP status, exchange error and operation outcome represented separately?
- Does a nonretryable error actually exit the retry loop?

## Why this score for a trading system

3/5: useful separation of transport and business errors, with a retry-loop boundary that prevents a stronger endorsement.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
