# exchange_calendars — session boundaries belong in the data contract

**Decision question:** Which session owns an observation exactly at the boundary?

| Field | Review |
| --- | --- |
| Upstream | [exchange_calendars](https://github.com/gerrymanoim/exchange_calendars) |
| Primary area | Data Quality & Lineage |
| Source commit | [bbda29fed902374bdb75acab008f421fbd567823](https://github.com/gerrymanoim/exchange_calendars/commit/bbda29fed902374bdb75acab008f421fbd567823) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/gerrymanoim/exchange_calendars/blob/bbda29fed902374bdb75acab008f421fbd567823/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Makes session boundary ownership explicit, including restrictions for continuous sessions. Useful for preventing duplicate or omitted boundary observations; an expected calendar still needs separate evidence of actual feed coverage. |

## Project overview

exchange_calendars defines and queries exchange sessions, trading minutes and calendar boundaries. [Project documentation](https://github.com/gerrymanoim/exchange_calendars/blob/bbda29fed902374bdb75acab008f421fbd567823/README.md#L5-L7).

## Mechanism worth inspecting

The calendar exposes left, right, both and neither boundary policies. For continuous sessions with matching open/close times, valid policies are restricted to left or right. First and last minute calculations follow that selected side. [Allowed sides](https://github.com/gerrymanoim/exchange_calendars/blob/bbda29fed902374bdb75acab008f421fbd567823/exchange_calendars/exchange_calendar.py#L764-L784); [minute endpoints](https://github.com/gerrymanoim/exchange_calendars/blob/bbda29fed902374bdb75acab008f421fbd567823/exchange_calendars/exchange_calendar.py#L865-L876).

## Important limit

An expected-session calendar is not observed data coverage. A half-open boundary policy can prevent double attribution, but missing bars, UTC/local-time conversion and calendar validity bounds still need explicit checks. [Accuracy bounds](https://github.com/gerrymanoim/exchange_calendars/blob/bbda29fed902374bdb75acab008f421fbd567823/exchange_calendars/exchange_calendar.py#L205-L209).

## Questions to take into your own design

- Are all session, funding-period and return buckets explicit about interval closure and timezone?
- Can a calendar-complete index still fail observed-feed coverage validation?

## Why this score for a trading system

3/5: a concrete temporal-boundary reference for financial datasets, with observed coverage and usable-time evidence separate from expected sessions.

**Scope of this review:** Calendar boundary policies and minute endpoints; individual exchange holiday accuracy was not audited.
