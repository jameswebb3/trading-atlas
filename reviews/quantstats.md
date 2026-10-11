# QuantStats: A drawdown report needs a return convention

**Decision question:** Does the report’s drawdown reflect the same equity path as the trading ledger?

| Field | Review |
| --- | --- |
| Upstream | [ranaroussi/quantstats](https://github.com/ranaroussi/quantstats) |
| Primary area | Portfolio & Risk |
| Source commit | [fbd10daed0227aa0d10da6513f1b15e7e98d7fae](https://github.com/ranaroussi/quantstats/commit/fbd10daed0227aa0d10da6513f1b15e7e98d7fae) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/ranaroussi/quantstats/blob/fbd10daed0227aa0d10da6513f1b15e7e98d7fae/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Computes drawdown and risk summaries from a returns series and provides Monte Carlo report views. A returns-only report inherits any omitted fees, funding, liquidations, or capital flows. |

## Mechanism worth inspecting

The statistics module calculates maximum drawdown from a cumulative path, including an initial baseline when the first return is negative. The report layer can resample returns for uncertainty displays. These are useful presentation and consistency patterns for a ledger-backed report.

**Source trail:** [project overview](https://github.com/ranaroussi/quantstats/blob/fbd10daed0227aa0d10da6513f1b15e7e98d7fae/README.md) · [documentation](https://github.com/ranaroussi/quantstats/blob/fbd10daed0227aa0d10da6513f1b15e7e98d7fae/docs/montecarlo.md#L1-L45) · [implementation](https://github.com/ranaroussi/quantstats/blob/fbd10daed0227aa0d10da6513f1b15e7e98d7fae/quantstats/stats.py#L2451-L2487) · [additional source](https://github.com/ranaroussi/quantstats/blob/fbd10daed0227aa0d10da6513f1b15e7e98d7fae/quantstats/stats.py#L841-L860).

## Important limit

The function sees the supplied series, not the order/fill ledger that produced it. If the series excludes costs or changes its capital base, a correct drawdown formula still describes the wrong account history.

## Questions to take into your own design

- Can each reported drawdown be reconciled to dated equity snapshots?
- Does the report state its return, fee, and capital-flow conventions?

## Why this score for a trading system

Drawdown calculations can audit trading reports when reconciled to equity, but the function cannot detect omitted costs or flows.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
