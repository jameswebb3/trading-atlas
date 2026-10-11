# A daily completeness check can silently assume weekdays

**Decision question:** Does a daily data-quality rule use the calendar your market actually trades?

| Field | Review |
| --- | --- |
| Upstream | [cuallee](https://github.com/canimus/cuallee) |
| Primary area | Data Quality & Lineage |
| Source commit | [907d93c310c160de0c8858442452a4e3c2b8fbde](https://github.com/canimus/cuallee/commit/907d93c310c160de0c8858442452a4e3c2b8fbde) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/canimus/cuallee/blob/907d93c310c160de0c8858442452a4e3c2b8fbde/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The pandas is_daily check defaults to Monday-Friday and builds expected dates from the observed minimum and maximum. For a 24/7 market, that can exclude missing weekends and cannot detect an absent boundary day outside the observed range. Supply the expected calendar explicitly. |

## Mechanism worth inspecting

The [README](https://github.com/canimus/cuallee/blob/907d93c310c160de0c8858442452a4e3c2b8fbde/README.md#L71-L75) presents daily continuity checks, and the [Check API page](https://github.com/canimus/cuallee/blob/907d93c310c160de0c8858442452a4e3c2b8fbde/docs/module/check.md#L1-L6) identifies the check abstraction. The [pandas implementation](https://github.com/canimus/cuallee/blob/907d93c310c160de0c8858442452a4e3c2b8fbde/cuallee/pandas_validation.py#L177-L203) uses weekday mask 0-4 by default and creates the expected sequence between input extrema.

## Important limit

Internal date continuity is not complete delivery against an external schedule. Changing the day mask addresses weekends; it still needs independent requested-range and intraday cadence checks. Backend equivalence was not established.

## Questions to take into your own design

- Is every calendar day expected, including weekends?
- Who supplies the required first and last observation dates?

## Why this score for a trading system

3/5: Calendar-aware completeness is a strong transferable data-contract pattern, with the backend's observed-range limitation made explicit.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
