# Optopsy: a cache gap threshold can hide missing market days

**Decision question:** How does a historical-data cache decide what to refetch?

| Field | Review |
| --- | --- |
| Upstream | [Optopsy](https://github.com/goldspanlabs/optopsy) |
| Primary area | Backtesting & Simulation |
| Source commit | [40bb8b2aa07ef8763caeadf752961faecb494efd](https://github.com/goldspanlabs/optopsy/commit/40bb8b2aa07ef8763caeadf752961faecb494efd) |
| Reviewed | 2026-09-25 |
| Declared license | [AGPL-3.0](https://github.com/goldspanlabs/optopsy/blob/40bb8b2aa07ef8763caeadf752961faecb494efd/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Checks cached option quote dates for leading, trailing, and interior gaps, then refetches gaps longer than five calendar days. Shorter holes are treated as weekends or holidays, which can conceal a missing trading session without an exchange calendar. |

## Mechanism worth inspecting

The [data guide](https://github.com/goldspanlabs/optopsy/blob/40bb8b2aa07ef8763caeadf752961faecb494efd/docs/data.md#L71-L91) describes a local Parquet cache with interior-gap fetching. The [gap detector](https://github.com/goldspanlabs/optopsy/blob/40bb8b2aa07ef8763caeadf752961faecb494efd/optopsy/data/providers/cache.py#L26-L52) distinguishes missing ranges before, inside, and after cached dates. Its [interior rule](https://github.com/goldspanlabs/optopsy/blob/40bb8b2aa07ef8763caeadf752961faecb494efd/optopsy/data/providers/cache.py#L67-L83) ignores adjacent observed dates separated by five or fewer calendar days. This is concrete evidence of a cache policy that trades unnecessary requests for possible omissions.

## Important limit

The source market is historical options data, often from a keyed provider; it is not a perpetuals data source. A fixed five-day rule does not know holidays, outages, early closes, or a missing single active session. The AGPL-3.0 license matters for any code reuse.

## Questions to take into your own design

- Is completeness checked against the actual venue calendar or expected event cadence?
- Can short interior holes be flagged instead of silently accepted?

## Why this score for a trading system

Its gap detector is a useful adjacent data-quality example, but the fixed calendar-day threshold is unsafe as a completeness guarantee and the assets are options.

**Scope of this review:** We read the pinned README, data guide, and cache-gap implementation. We did not fetch options data.
