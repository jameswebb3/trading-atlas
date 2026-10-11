# alpha-rptr — Order retries need outcome evidence

**Decision question:** Does retrying a failed request prove that the first order was rejected?

| Field | Review |
| --- | --- |
| Upstream | [alpha-rptr](https://github.com/TheFourGreatErrors/alpha-rptr) |
| Primary area | Execution & Exchange Integration |
| Source commit | [31a7ae00744ee58689a1b5baa1ab525ff4b3981d](https://github.com/TheFourGreatErrors/alpha-rptr/commit/31a7ae00744ee58689a1b5baa1ab525ff4b3981d) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/TheFourGreatErrors/alpha-rptr/blob/31a7ae00744ee58689a1b5baa1ab525ff4b3981d/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The Binance futures order call is wrapped in a shared retry helper. Retry eligibility is not proof that a trading write had no effect. |

## Project overview

Crypto-trading framework with backtesting, paper trading and exchange execution paths. [Documentation](https://github.com/TheFourGreatErrors/alpha-rptr/blob/31a7ae00744ee58689a1b5baa1ab525ff4b3981d/README.md).

## Mechanism worth inspecting

The Binance futures order call is wrapped in a shared retry helper. That helper retries selected API errors, server errors and request exceptions. [Source](https://github.com/TheFourGreatErrors/alpha-rptr/blob/31a7ae00744ee58689a1b5baa1ab525ff4b3981d/src/exchange/binance_futures/binance_futures.py#L594-L644).

## Important limit

Retry eligibility is not proof that a trading write had no effect. The inspected helper contains no account-reconciliation step before retrying the supplied function. [Evidence 1](https://github.com/TheFourGreatErrors/alpha-rptr/blob/31a7ae00744ee58689a1b5baa1ab525ff4b3981d/src/exchange/binance_futures/binance_futures.py#L594-L644). [Evidence 2](https://github.com/TheFourGreatErrors/alpha-rptr/blob/31a7ae00744ee58689a1b5baa1ab525ff4b3981d/src/__init__.py#L454-L492).

## Questions to take into your own design

- Which errors prove an order was never submitted?
- What evidence is required before repeating an uncertain write?

## Why this score for a trading system

Directly useful as a counterexample for order retry design; neither the framework's strategy results nor exchange-wide idempotency were verified.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
