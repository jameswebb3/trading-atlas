# Crypto-Signal — When is an indicator's latest candle safe to use

**Decision question:** When is an indicator's latest candle safe to use?

| Field | Review |
| --- | --- |
| Upstream | [Crypto-Signal](https://github.com/CryptoSignal/Crypto-Signal) |
| Primary area | Signals & Models |
| Source commit | [7cb9c5c6cd226c6fe2d345e4bda3bec8156cefec](https://github.com/CryptoSignal/Crypto-Signal/commit/7cb9c5c6cd226c6fe2d345e4bda3bec8156cefec) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/CryptoSignal/Crypto-Signal/blob/7cb9c5c6cd226c6fe2d345e4bda3bec8156cefec/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | A readable technical-analysis scanner with configurable indicators and alerts. Its OHLCV boundary still needs closed-candle and historical-availability checks before the output can guide trading research. |

## Project overview

Crypto-Signal is a configurable technical-analysis scanner with indicator dispatch and notifications, rather than evidence that its alerts form a profitable strategy. [Project documentation](https://github.com/CryptoSignal/Crypto-Signal/blob/7cb9c5c6cd226c6fe2d345e4bda3bec8156cefec/docs/config.md#L12-L45).

## Mechanism worth inspecting

The data path requests OHLCV from a calculated start timestamp and returns the resulting bars to analysis. Indicator and informant dispatch are explicit. [Fetch boundary](https://github.com/CryptoSignal/Crypto-Signal/blob/7cb9c5c6cd226c6fe2d345e4bda3bec8156cefec/app/exchange.py#L93-L102), [dispatch](https://github.com/CryptoSignal/Crypto-Signal/blob/7cb9c5c6cd226c6fe2d345e4bda3bec8156cefec/app/analysis.py#L24-L59).

## Important limit

The inspected fetch call does not establish that the newest candle is closed or that a historical response was available at a past decision time. An alert needs those guarantees from a separate input contract.

## Questions to take into your own design

- When is an indicator's latest candle safe to use?
- Which timestamp and closed-candle rule qualify the last returned bar for a decision?

## Why this score for a trading system

2/5: direct trading utility as a scanner example, but familiar indicator dispatch adds little beyond explicit input-boundary checks.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
