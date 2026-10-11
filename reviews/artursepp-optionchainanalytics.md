# OptionChainAnalytics - Does point-in-time chain reconstruction silently select a later quote?

**Decision question:** Does point-in-time chain reconstruction silently select a later quote?

| Field | Review |
| --- | --- |
| Upstream | [ArturSepp/OptionChainAnalytics](https://github.com/ArturSepp/OptionChainAnalytics) |
| Primary area | Signals Models |
| Source commit | [f130fba8afcb44caf3b7c54803cff184200c4b7e](https://github.com/ArturSepp/OptionChainAnalytics/commit/f130fba8afcb44caf3b7c54803cff184200c4b7e) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Reconstructs an option chain at an exact observation time by default; an explicit previous policy chooses the latest earlier feed time and returns that actual time. The previous policy has no maximum-age guard, so an old chain can be causally eligible but economically stale. |

## What this project does

A provider-normalized option-chain library covering feed adapters, historical panels and chain queries. The inspected path turns option observations into expiry slices for a requested research timestamp.

## Mechanism inspected

create_chain_at_time delegates selection to OptionsDataDFs.get_time_slice. Exact selection is the default. Under previous selection, the data container pads backward in its observed time index and never selects a future row. The returned chain records the actual selected exchange time rather than only the requested schedule time.

## Limitation that matters

Backward selection has no maximum staleness interval. A chain could be old yet still satisfy the causal inequality; the caller must decide whether it was fresh enough for the intended signal or trade. The module models option data, not a directly tradable perpetuals strategy, and a recorded exchange timestamp does not establish local receipt time.

## Practical check for a trading system

Keep requested time, selected source time and arrival time as separate fields. Require an explicit max-age budget for as-of joins and reject missing or stale chains rather than forward-filling indefinitely.

## Why this score

3/5 because the code provides a strong transferable point-in-time selection contract, with a precise staleness gap and an options-specific input requirement.

## Source trail

[README](https://github.com/ArturSepp/OptionChainAnalytics/blob/f130fba8afcb44caf3b7c54803cff184200c4b7e/README.md#L20); [Exact/previous reconstruction](https://github.com/ArturSepp/OptionChainAnalytics/blob/f130fba8afcb44caf3b7c54803cff184200c4b7e/src/option_chain_analytics/reconstruction.py#L20); [Backward selector](https://github.com/ArturSepp/OptionChainAnalytics/blob/f130fba8afcb44caf3b7c54803cff184200c4b7e/src/option_chain_analytics/option_data.py#L102); [License](https://github.com/ArturSepp/OptionChainAnalytics/blob/f130fba8afcb44caf3b7c54803cff184200c4b7e/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
