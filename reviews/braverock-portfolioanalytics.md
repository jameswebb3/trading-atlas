# PortfolioAnalytics — What exact return window produced each rebalance decision

**Decision question:** What exact return window produced each rebalance decision?

| Field | Review |
| --- | --- |
| Upstream | [PortfolioAnalytics](https://github.com/braverock/PortfolioAnalytics) |
| Primary area | Portfolio & Risk |
| Source commit | [c44f11149fd69c53dd73ed2152f6f99345ab5a82](https://github.com/braverock/PortfolioAnalytics/commit/c44f11149fd69c53dd73ed2152f6f99345ab5a82) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0](https://github.com/braverock/PortfolioAnalytics/blob/c44f11149fd69c53dd73ed2152f6f99345ab5a82/DESCRIPTION) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A portfolio-optimization reference with explicit rebalance endpoints and training windows. Inspect the actual inclusive row slice and decision timing before treating a configured window as a fixed-duration out-of-sample test. |

## Project overview

PortfolioAnalytics supports portfolio constraints, objectives and optimization at rebalance dates. [Project documentation](https://github.com/braverock/PortfolioAnalytics/blob/c44f11149fd69c53dd73ed2152f6f99345ab5a82/man/optimize.portfolio.rebalancing.Rd#L37-L81).

## Mechanism worth inspecting

The rebalancing path derives endpoints from a training-period threshold and selects an expanding or rolling input slice. Its rolling expression includes both the start and endpoint rows. [Window selection](https://github.com/braverock/PortfolioAnalytics/blob/c44f11149fd69c53dd73ed2152f6f99345ab5a82/R/optimize.portfolio.R#L3590-L3653).

## Important limit

The inspected rolling slice can contain rolling_window plus one rows when its full range is available. Row counts also do not imply elapsed-time coverage; an out-of-sample claim still needs an execution-time and availability contract.

## Questions to take into your own design

- What exact return window produced each rebalance decision?
- What exact first and last training rows precede each rebalance's effective execution time?

## Why this score for a trading system

3/5: direct portfolio research mechanism, with concrete window semantics; solver and turnover behavior outside this slice were not assessed.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
