# Feast: event time is not always publication time

**Decision question:** When does a historical feature join exclude a value that was recorded for an earlier event but published later?

| Field | Review |
| --- | --- |
| Upstream | [feast-dev/feast](https://github.com/feast-dev/feast) |
| Primary area | Data Quality & Lineage |
| Source commit | [d4e96194d4d4f039f89ea71fe81926cc519ed5df](https://github.com/feast-dev/feast/commit/d4e96194d4d4f039f89ea71fe81926cc519ed5df) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/feast-dev/feast/blob/d4e96194d4d4f039f89ea71fe81926cc519ed5df/LICENSE) |
| Review depth | 2/3: documentation and API implementation read; no backend or runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Feast exposes an optional creation-time filter for historical feature joins. It can prevent late updates from appearing early, but the source must declare creation time and the filter must be enabled. |

## Project overview

Feature store for historical training datasets and online inference. Its timestamp-aware joins provide an explicit place to control which feature values are eligible at each observation time.

[Project documentation](https://github.com/feast-dev/feast/blob/d4e96194d4d4f039f89ea71fe81926cc519ed5df/README.md#L26-L38).

## Mechanism worth inspecting

Feast's historical retrieval joins features to entity rows by event timestamp. Its [API contract](https://github.com/feast-dev/feast/blob/d4e96194d4d4f039f89ea71fe81926cc519ed5df/sdk/python/feast/feature_store.py#L1988-L2031) also offers `filter_by_created_timestamp`, which excludes a value created after the entity row's event time when the batch source declares a `created_timestamp_column`. The [FeatureStore path forwards this option](https://github.com/feast-dev/feast/blob/d4e96194d4d4f039f89ea71fe81926cc519ed5df/sdk/python/feast/feature_store.py#L2132-L2152) to the provider.

Two details matter for a reader: the option defaults to `False`, and feature views without that created-timestamp column are unaffected. An event-time join alone does not answer when a revised value became available.

## Questions to take into your own data contract

- Which timestamp describes the event, and which describes publication or creation?
- Can late corrections be distinguished from values known at decision time?
- Is the publication-time filter enabled for every historical retrieval that needs it?
- What happens when a source lacks a creation timestamp?

## Why this score for a trading system

Point-in-time feature filtering can prevent a trading decision from using late data, but this path is optional and backend coverage was not established.

**Scope of this review:** We inspected the pinned API contract and provider dispatch, not each offline-store backend's generated query. We did not run Feast or test a historical join. The review identifies a relevant contract and its preconditions, rather than certifying every backend implementation.
