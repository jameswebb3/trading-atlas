# ffn: make the calendar behind annualized statistics explicit

**Decision question:** Does a performance report use the correct annualization basis for a continuously traded market?

| Field | Review |
| --- | --- |
| Upstream | [ffn](https://github.com/pmorissette/ffn) |
| Primary area | Portfolio & Risk |
| Source commit | [abd3adb5b2b20dadb9608f665bb299065cbb4d75](https://github.com/pmorissette/ffn/commit/abd3adb5b2b20dadb9608f665bb299065cbb4d75) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/pmorissette/ffn/blob/abd3adb5b2b20dadb9608f665bb299065cbb4d75/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Calculates portfolio performance statistics and return transformations. Its frequency inference distinguishes time units, while daily and intraday annualization share a configurable trading-days basis; a 24/7 market needs an explicit convention. |

## Project overview

A financial analysis library provides return transformations, drawdowns, performance statistics, and allocation utilities through pandas-based interfaces. [Project documentation](https://github.com/pmorissette/ffn/blob/abd3adb5b2b20dadb9608f665bb299065cbb4d75/README.md#L1-L24).

## Mechanism worth inspecting

The [performance-statistics object](https://github.com/pmorissette/ffn/blob/abd3adb5b2b20dadb9608f665bb299065cbb4d75/ffn/core.py#L78-L88) records whether an annualization factor was supplied. [Frequency handling](https://github.com/pmorissette/ffn/blob/abd3adb5b2b20dadb9608f665bb299065cbb4d75/ffn/core.py#L2529-L2550) maps daily and intraday aliases to a shared basis, and [inference](https://github.com/pmorissette/ffn/blob/abd3adb5b2b20dadb9608f665bb299065cbb4d75/ffn/core.py#L2587-L2606) returns no frequency when the index cannot establish one. The [Sharpe calculation](https://github.com/pmorissette/ffn/blob/abd3adb5b2b20dadb9608f665bb299065cbb4d75/ffn/core.py#L1562-L1587) requires a period basis when deannualizing a nonzero scalar risk-free rate.

## Important limit

A regular daily timestamp sequence does not establish whether the correct basis is business days or calendar days. The [default basis](https://github.com/pmorissette/ffn/blob/abd3adb5b2b20dadb9608f665bb299065cbb4d75/ffn/core.py#L2587-L2603) is trading days. The [quickstart](https://github.com/pmorissette/ffn/blob/abd3adb5b2b20dadb9608f665bb299065cbb4d75/docs/source/quickstart.md#L9-L47) also illustrates adjusted equity prices and adds methods to pandas objects at import; those data choices are separate from performance correctness.

## Questions to take into your own design

- Does every report record period frequency, annualization basis, and risk-free-rate units?
- Are irregular timestamps rejected, normalized under a documented rule, or allowed to alter inferred statistics?

## Why this score for a trading system

3/5: directly useful metric conventions and edge-case behavior, but market calendars and input completeness must be specified outside automatic frequency inference.

**Scope of this review:** README, quickstart, annualization inference, PerformanceStats initialization, and Sharpe input contract; no metrics run.
