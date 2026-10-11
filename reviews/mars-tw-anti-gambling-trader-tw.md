# Anti-Gambling Trader - A null-centered bootstrap is still a trade-sample test

**Decision question:** Does a positive mean trade PnL survive a defined null test?

| Field | Review |
| --- | --- |
| Upstream | [mars-tw/anti-gambling-trader-tw](https://github.com/mars-tw/anti-gambling-trader-tw) |
| Primary area | Portfolio & Risk |
| Source commit | [8609cef73718a056fddb74201fc304f174fa1553](https://github.com/mars-tw/anti-gambling-trader-tw/commit/8609cef73718a056fddb74201fc304f174fa1553) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Centers per-trade PnL under a zero-mean null, uses finite-input checks and a plus-one bootstrap p-value, then requires both t and bootstrap evidence before calling expectancy significant. Individual-trade resampling does not address serial dependence, overlapping exposure or strategy selection; the included calibration test is deliberately coarse. |

## What this project does

A local trading-performance analyzer for securities, derivatives, crypto and foreign exchange. It combines trade-level expectancy, statistical checks and forensic warnings; the reviewed path is its significance test, not its complete decision system.

## Mechanism inspected

The function rejects non-finite PnL, centers observed trade outcomes at zero for the bootstrap null, resamples with a fixed seed, applies a plus-one Monte Carlo p-value correction and requires both the one-sided t test and bootstrap test to pass. A source test checks null centering and a coarse type-I calibration on generated normal samples.

## Limitation that matters

The resampling unit is an individual trade. Serially dependent trades, overlapping positions, strategy selection and repeated testing are outside this test. The quick calibration accepts a type-I rate as high as 13 percent over 120 trials; this source review has not independently calibrated it. This is a source review, not a runtime or security test.

## Practical check for a trading system

Preserve the unit of dependence and the number of tried strategies when evaluating an edge. Treat this test as one descriptive gate, then use blocked or event-level resampling and the full multiple-testing protocol when trades are dependent.

## Why this score

3/5 because the code gives a directly relevant, inspectable expectancy check and targeted test source, while its iid trade unit and omitted selection effects limit trading conclusions.

## Source trail

[README](https://github.com/mars-tw/anti-gambling-trader-tw/blob/8609cef73718a056fddb74201fc304f174fa1553/README.md#L87); [Significance implementation](https://github.com/mars-tw/anti-gambling-trader-tw/blob/8609cef73718a056fddb74201fc304f174fa1553/core/verdict/statistics.py#L169); [Centered bootstrap](https://github.com/mars-tw/anti-gambling-trader-tw/blob/8609cef73718a056fddb74201fc304f174fa1553/core/verdict/statistics.py#L240); [Calibration test](https://github.com/mars-tw/anti-gambling-trader-tw/blob/8609cef73718a056fddb74201fc304f174fa1553/tests/test_round9.py#L61); [License](https://github.com/mars-tw/anti-gambling-trader-tw/blob/8609cef73718a056fddb74201fc304f174fa1553/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
