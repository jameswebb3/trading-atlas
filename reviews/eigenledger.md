# EigenLedger: audit missing prices before trusting optimized weights

**Decision question:** Can missing historical prices be converted into artificial returns before optimization?

| Field | Review |
| --- | --- |
| Upstream | [EigenLedger](https://github.com/santoshlite/EigenLedger) |
| Primary area | Portfolio & Risk |
| Source commit | [0f965f95c147b1a339e8565738cc49bd784474d2](https://github.com/santoshlite/EigenLedger/commit/0f965f95c147b1a339e8565738cc49bd784474d2) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0 (LICENSE; README badge differs)](https://github.com/santoshlite/EigenLedger/blob/0f965f95c147b1a339e8565738cc49bd784474d2/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | Wraps portfolio analysis and optimization libraries. Its inspected return path rejects missing symbols, but a separate optimizer replaces missing prices with one before estimating returns and covariance, a material inconsistency to inspect before trusting resulting weights. |

## Project overview

A portfolio-analysis wrapper combines reporting and optimization interfaces. [Project documentation](https://github.com/santoshlite/EigenLedger/blob/0f965f95c147b1a339e8565738cc49bd784474d2/README.md#L26-L30).

## Mechanism worth inspecting

The [return loader](https://github.com/santoshlite/EigenLedger/blob/0f965f95c147b1a339e8565738cc49bd784474d2/EigenLedger/main.py#L171-L209) checks weight lengths, missing symbols, and initial allocations. The [efficient-frontier path](https://github.com/santoshlite/EigenLedger/blob/0f965f95c147b1a339e8565738cc49bd784474d2/EigenLedger/main.py#L755-L783) uses the requested date range but fills missing prices with one before estimating expected returns and covariance.

## Important limit

An invented price is neither a missing-data marker nor evidence of a tradable listing. The [optimization input](https://github.com/santoshlite/EigenLedger/blob/0f965f95c147b1a339e8565738cc49bd784474d2/EigenLedger/main.py#L763-L773) can therefore change the return distribution. The root [license file](https://github.com/santoshlite/EigenLedger/blob/0f965f95c147b1a339e8565738cc49bd784474d2/LICENSE#L1-L9) says Apache-2.0 while the [README badge](https://github.com/santoshlite/EigenLedger/blob/0f965f95c147b1a339e8565738cc49bd784474d2/README.md#L13-L17) says MIT; external documentation was unavailable during review.

## Questions to take into your own design

- Does every optimization path enforce the same missing-data policy?
- Are pre-listing periods excluded rather than assigned synthetic prices?

## Why this score for a trading system

1/5: a useful cautionary data-policy example, with artificial price substitution and inconsistent license presentation.

**Scope of this review:** README quickstart/overview, return loader, efficient-frontier source, license; linked external documentation unavailable.
