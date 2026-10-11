# re_data: keep alert counts separate from the displayed sample

**Decision question:** Can a compact data-quality notification preserve the scope of the underlying failures?

| Field | Review |
| --- | --- |
| Upstream | [re_data](https://github.com/re-data/re-data) |
| Primary area | Operations & Observability |
| Source commit | [d43f6b1c369e667bb9b469b3a691e5050f278f9b](https://github.com/re-data/re-data/commit/d43f6b1c369e667bb9b469b3a691e5050f278f9b) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/re-data/re-data/blob/d43f6b1c369e667bb9b469b3a691e5050f278f9b/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Builds dbt reliability reports and groups anomaly, schema-change, and test alerts by model and owner. Its notification shows full category counts while limiting displayed examples, a useful distinction when a compact message summarizes many failures. |

## Project overview

A dbt-oriented reliability framework observes warehouse data and generates HTML/JSON overviews for explicit dates and time grains. [Project documentation](https://github.com/re-data/re-data/blob/d43f6b1c369e667bb9b469b3a691e5050f278f9b/README.md#L9-L14).

## Mechanism worth inspecting

The [overview contract](https://github.com/re-data/re-data/blob/d43f6b1c369e667bb9b469b3a691e5050f278f9b/docs/docs/re_data/reference/cli/overview.md#L14-L29) separates report generation from the prior computation of monitored models. [Alert grouping](https://github.com/re-data/re-data/blob/d43f6b1c369e667bb9b469b3a691e5050f278f9b/re_data/notifications/utils.py#L32-L58) preserves anomaly, schema-change, and test categories and validates selected types. [Message construction](https://github.com/re-data/re-data/blob/d43f6b1c369e667bb9b469b3a691e5050f278f9b/re_data/notifications/slack.py#L103-L146) reports category counts while showing at most ten formatted examples of each.

## Important limit

The [webhook sender](https://github.com/re-data/re-data/blob/d43f6b1c369e667bb9b469b3a691e5050f278f9b/re_data/notifications/slack.py#L8-L22) checks HTTP status but specifies no request timeout and records no durable delivery state in this function. A bounded example list also needs a route to the complete evidence. The anomaly algorithms documented elsewhere are not implemented in the inspected notification code.

## Questions to take into your own design

- Does a notification distinguish total failures from examples shown?
- Can undelivered or delayed notifications be audited independently of the generated quality report?

## Why this score for a trading system

2/5: a useful compact-reporting pattern, limited by the inspected delivery path and its generic dbt context. This is not an endorsement of an end-to-end alert reliability guarantee.

**Scope of this review:** README, overview and anomaly documentation, alert grouping, formatting, and webhook source; anomaly computation package not evaluated.
