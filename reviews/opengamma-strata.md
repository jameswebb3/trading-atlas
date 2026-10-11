# Strata — Missing data and failed data builds

**Decision question:** Can a missing market value conceal a failed calculation?

| Field | Review |
| --- | --- |
| Upstream | [Strata](https://github.com/OpenGamma/Strata) |
| Primary area | Portfolio & Risk |
| Source commit | [a712bfd58c650f24e180941de51bdff8fe371f98](https://github.com/OpenGamma/Strata/commit/a712bfd58c650f24e180941de51bdff8fe371f98) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/OpenGamma/Strata/blob/a712bfd58c650f24e180941de51bdff8fe371f98/LICENSE.txt) |
| Review depth | 3/3: documentation, relevant implementation, and relevant test code read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | BuiltScenarioMarketData stores failed value and time-series builds separately. The optional findValue method delegates to the underlying data and does not expose the failure map. |

## Project overview

Java library for financial analytics, pricing and market risk. [Documentation](https://github.com/OpenGamma/Strata/blob/a712bfd58c650f24e180941de51bdff8fe371f98/README.md).

## Mechanism worth inspecting

BuiltScenarioMarketData stores failed value and time-series builds separately. Its strict value lookup raises the recorded construction failure; an unknown value raises a different missing-data exception. [Source](https://github.com/OpenGamma/Strata/blob/a712bfd58c650f24e180941de51bdff8fe371f98/modules/calc/src/main/java/com/opengamma/strata/calc/marketdata/BuiltScenarioMarketData.java#L39-L152).

## Important limit

The optional findValue method delegates to the underlying data and does not expose the failure map. Choosing a convenience accessor changes the evidence available to the caller. [Evidence 1](https://github.com/OpenGamma/Strata/blob/a712bfd58c650f24e180941de51bdff8fe371f98/modules/calc/src/main/java/com/opengamma/strata/calc/marketdata/BuiltScenarioMarketData.java#L39-L152). [Evidence 2](https://github.com/OpenGamma/Strata/blob/a712bfd58c650f24e180941de51bdff8fe371f98/modules/calc/src/test/java/com/opengamma/strata/calc/marketdata/BuiltScenarioMarketDataTest.java#L36-L70).

## Questions to take into your own design

- Does a receipt distinguish unavailable input from failed computation?
- Can an optional lookup erase an actionable failure?

## Why this score for a trading system

Useful for financial data admission and risk calculations; the inspected accessor contract does not validate an entire market-data pipeline.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. Relevant tests were read, not executed.
