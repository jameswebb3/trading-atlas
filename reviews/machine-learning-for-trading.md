# Machine Learning for Trading: an as-of match can be stale or early

**Decision question:** Can a perfectly filled as-of join still give a signal data from the future?

| Field | Review |
| --- | --- |
| Upstream | [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) |
| Primary area | Signals & Models |
| Source commit | [dd5ec27aaee25d5d6c4017014a544cd87236f0ce](https://github.com/stefan-jansen/machine-learning-for-trading/commit/dd5ec27aaee25d5d6c4017014a544cd87236f0ce) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/stefan-jansen/machine-learning-for-trading/blob/dd5ec27aaee25d5d6c4017014a544cd87236f0ce/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Shifts premium bars from open time to publication time before a backward join, then measures matched-value age. A non-null as-of match can carry the last value across an interior publication gap; null counts alone overstate coverage. |

## Mechanism worth inspecting

The [project overview](https://github.com/stefan-jansen/machine-learning-for-trading/blob/dd5ec27aaee25d5d6c4017014a544cd87236f0ce/README.md#L33-L40) separates research from evaluation. In its crypto-perpetuals notebook, it first checks hourly gaps [per symbol](https://github.com/stefan-jansen/machine-learning-for-trading/blob/dd5ec27aaee25d5d6c4017014a544cd87236f0ce/02_financial_data_universe/10_crypto_perps_eda.py#L423-L447). For the premium join, it [moves the bar-open timestamp to publication time](https://github.com/stefan-jansen/machine-learning-for-trading/blob/dd5ec27aaee25d5d6c4017014a544cd87236f0ce/02_financial_data_universe/10_crypto_perps_eda.py#L482-L513) before a backward as-of match. It then measures [age since publication](https://github.com/stefan-jansen/machine-learning-for-trading/blob/dd5ec27aaee25d5d6c4017014a544cd87236f0ce/02_financial_data_universe/10_crypto_perps_eda.py#L521-L548) to catch intervals where the expected update did not arrive.

## Important limit

The eight-hour cadence in this file describes its chosen source and bars; it is not a universal rule for every market feed. The review establishes a timing and coverage method, not that the repo's trading strategies are profitable or that its source timestamps are correct for other venues.

## Questions to take into your own design

- Is a timestamp bar open, bar close, publication, or receipt?
- Does each symbol meet its own expected cadence?
- Can a joined value be non-null but too old for the decision?

## Why this score for a trading system

The crypto-perpetual premium example handles publication time and carried values, two direct sources of false signal evidence.

**Scope of this review:** We read the pinned README, repository documentation, and the crypto-perpetuals notebook. We did not reproduce notebook outputs or review the book's trading results.
