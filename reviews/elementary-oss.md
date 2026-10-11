# Elementary OSS: distinguish a detected problem from a delivered alert

**Decision question:** Does an alert remain pending when its notification fails?

| Field | Review |
| --- | --- |
| Upstream | [Elementary OSS](https://github.com/elementary-data/elementary) |
| Primary area | Operations & Observability |
| Source commit | [e34d8539b9c7f350c2de9ee954794d40b9260d93](https://github.com/elementary-data/elementary/commit/e34d8539b9c7f350c2de9ee954794d40b9260d93) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/elementary-data/elementary/blob/e34d8539b9c7f350c2de9ee954794d40b9260d93/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Turns dbt run and quality evidence into reports and notifications. It records pending, sent, and skipped states and marks only successfully delivered alerts as sent; suppression and latest-only selection still affect what reaches an operator. |

## Project overview

A self-hosted CLI reads warehouse evidence collected by the Elementary dbt package, generates reports, and sends operational alerts. [Project documentation](https://github.com/elementary-data/elementary/blob/e34d8539b9c7f350c2de9ee954794d40b9260d93/README.md#L27-L41).

## Mechanism worth inspecting

The [alert schema](https://github.com/elementary-data/elementary/blob/e34d8539b9c7f350c2de9ee954794d40b9260d93/elementary/monitor/fetchers/alerts/schema/pending_alerts.py#L24-L45) separates detection, creation, update, and send timestamps. The [delivery loop](https://github.com/elementary-data/elementary/blob/e34d8539b9c7f350c2de9ee954794d40b9260d93/elementary/monitor/data_monitoring/alerts/data_monitoring_alerts.py#L389-L420) updates sent state only for alerts whose integration reports successful sending. [Sorting](https://github.com/elementary-data/elementary/blob/e34d8539b9c7f350c2de9ee954794d40b9260d93/elementary/monitor/data_monitoring/alerts/data_monitoring_alerts.py#L179-L197) explicitly distinguishes suppressed or superseded alerts from those to send.

## Important limit

The send action precedes the persisted sent update, leaving a crash interval where an already delivered alert can be retried. The [documentation](https://github.com/elementary-data/elementary/blob/e34d8539b9c7f350c2de9ee954794d40b9260d93/docs/oss/guides/alerts/alerts-configuration.mdx#L10-L18) also says skipped tests/models are filtered out by default. Quiet notifications therefore do not prove that checks ran successfully.

## Questions to take into your own design

- Can an operator inspect detected, suppressed, delivered, and delivery-failed states separately?
- Does retry tolerate a duplicate notification without losing the underlying incident record?

## Why this score for a trading system

3/5: precise reusable delivery-state and suppression semantics for data operations. It is generic dbt observability, not a trading risk controller.

**Scope of this review:** README, OSS alert configuration, pending schema, alert selection, and delivery-state code; no notification sent.
