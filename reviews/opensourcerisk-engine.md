# Open Source Risk Engine — Scenario files have an explicit shape

**Decision question:** What does a valid scenario row establish?

| Field | Review |
| --- | --- |
| Upstream | [Open Source Risk Engine](https://github.com/OpenSourceRisk/Engine) |
| Primary area | Portfolio & Risk |
| Source commit | [3d75a69087911a7e2cf1e6882da7bc27135c0762](https://github.com/OpenSourceRisk/Engine/commit/3d75a69087911a7e2cf1e6882da7bc27135c0762) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-style custom license](https://github.com/OpenSourceRisk/Engine/blob/3d75a69087911a7e2cf1e6882da7bc27135c0762/license.txt) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The CSV scenario generator parses risk-factor keys from the header, checks the requested date and requires each row to contain the expected number of values before building a scenario. A matching date and column count do not establish publication time, units or realistic scenarios. |

## Project overview

Pricing and risk framework covering financial instruments, scenarios and valuation adjustments. [Documentation](https://github.com/OpenSourceRisk/Engine/blob/3d75a69087911a7e2cf1e6882da7bc27135c0762/README.md).

## Mechanism worth inspecting

The CSV scenario generator parses risk-factor keys from the header, checks the requested date and requires each row to contain the expected number of values before building a scenario. [Source](https://github.com/OpenSourceRisk/Engine/blob/3d75a69087911a7e2cf1e6882da7bc27135c0762/OREAnalytics/orea/scenario/csvscenariogenerator.cpp#L22-L91).

## Important limit

A matching date and column count do not establish publication time, units or realistic scenarios. The reviewed parser is a data boundary, not validation of the engine's financial models. [Evidence 1](https://github.com/OpenSourceRisk/Engine/blob/3d75a69087911a7e2cf1e6882da7bc27135c0762/OREAnalytics/orea/scenario/csvscenariogenerator.cpp#L22-L91).

## Questions to take into your own design

- Is the factor order fixed in each scenario receipt?
- Where are valuation date, knowledge time and factor units validated?

## Why this score for a trading system

A narrow risk-input contract worth borrowing; operating the larger pricing stack is unnecessary for this pattern.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
