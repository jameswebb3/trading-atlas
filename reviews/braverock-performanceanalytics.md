# PerformanceAnalytics — What time basis does annualized performance actually use

**Decision question:** What time basis does annualized performance actually use?

| Field | Review |
| --- | --- |
| Upstream | [PerformanceAnalytics](https://github.com/braverock/PerformanceAnalytics) |
| Primary area | Portfolio & Risk |
| Source commit | [c079aea14727f68b5bfcc1e90292ceeb8a1f22e7](https://github.com/braverock/PerformanceAnalytics/commit/c079aea14727f68b5bfcc1e90292ceeb8a1f22e7) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-2 or GPL-3](https://github.com/braverock/PerformanceAnalytics/blob/c079aea14727f68b5bfcc1e90292ceeb8a1f22e7/DESCRIPTION) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A practical reference for inspecting performance formulas rather than accepting headline metrics. Its annualization depends on periods per year and the number of retained observations, making calendar and missing-data policy essential inputs. |

## Project overview

PerformanceAnalytics computes financial performance and risk statistics from return series. [Project documentation](https://github.com/braverock/PerformanceAnalytics/blob/c079aea14727f68b5bfcc1e90292ceeb8a1f22e7/man/Return.annualized.Rd#L7-L38).

## Mechanism worth inspecting

Return.annualized infers periods per year, with a daily default of 252, removes missing observations by default, and annualizes geometric return using the remaining count. [Implementation](https://github.com/braverock/PerformanceAnalytics/blob/c079aea14727f68b5bfcc1e90292ceeb8a1f22e7/R/Return.annualized.R#L58-L106).

## Important limit

The output depends on the sampling calendar and missing-data policy. A 24/7 series, irregular observations or incomplete history requires an explicit time basis; silently dropping observations can change the apparent annual rate.

## Questions to take into your own design

- What time basis does annualized performance actually use?
- Do missing observations change elapsed exposure time or only the statistical sample count?

## Why this score for a trading system

3/5: direct trading measurement with transparent formulas and consequential defaults. This focused reading does not validate every metric in the package.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
