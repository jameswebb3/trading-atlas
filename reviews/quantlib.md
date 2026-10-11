# Tail risk estimates should fail when the tail has no observations

**Decision question:** Should a risk report emit a number when the selected tail has no samples?

| Field | Review |
| --- | --- |
| Upstream | [QuantLib](https://github.com/lballabio/QuantLib) |
| Primary area | Portfolio & Risk |
| Source commit | [0191ca7cccbb62e538fd10f5c88f640594d4eaed](https://github.com/lballabio/QuantLib/commit/0191ca7cccbb62e538fd10f5c88f640594d4eaed) |
| Reviewed | 2026-09-25 |
| Declared license | [BSD-3-Clause](https://github.com/lballabio/QuantLib/blob/0191ca7cccbb62e538fd10f5c88f640594d4eaed/LICENSE.TXT) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | QuantLib's risk-statistics code checks percentile bounds and refuses an expected-shortfall estimate when the relevant sample tail is empty. This is a useful reporting invariant, but it does not validate that the sampled returns represent a live perpetual-futures portfolio. |

## Project overview

Quantitative finance library for financial modelling and risk calculations. Offers numerical building blocks and explicit input checks, including rejection of tail estimates with no supporting observations.

[Project documentation](https://github.com/lballabio/QuantLib/blob/0191ca7cccbb62e538fd10f5c88f640594d4eaed/README.md#L19-L25).

## Mechanism worth inspecting

The [project overview](https://github.com/lballabio/QuantLib/blob/0191ca7cccbb62e538fd10f5c88f640594d4eaed/README.md#L21-L34) describes QuantLib as a quantitative finance library. The [risk statistics implementation](https://github.com/lballabio/QuantLib/blob/0191ca7cccbb62e538fd10f5c88f640594d4eaed/ql/math/statistics/riskstatistics.hpp#L178-L205) bounds the percentile argument and rejects an expected-shortfall calculation when there are no observations in the selected tail.

## Important limit

A nonempty tail does not prove a reliable estimate. Sampling window, dependence, regime, horizon, and mark-to-market convention remain decisions for the user of the statistic.

## Questions to take into your own design

- How many observations actually support the reported tail estimate?
- Which horizon and loss definition generated those observations?

## Why this score for a trading system

2/5: The empty-tail guard is a useful fail-closed rule for risk reports. QuantLib's wider scope is derivatives valuation, and these routines alone do not solve return sampling, dependence, or crypto-specific risk.

**Scope of this review:** We read the README and the risk-statistics source.
