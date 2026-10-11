# Hopsworks - Is point-in-time joining an explicit query decision?

**Decision question:** Is point-in-time joining an explicit query decision?

| Field | Review |
| --- | --- |
| Upstream | [logicalclocks/hopsworks](https://github.com/logicalclocks/hopsworks) |
| Primary area | Research & Reproducibility |
| Source commit | [2b1cb50ee5c8ab1395e54baa21511195bcd28e44](https://github.com/logicalclocks/hopsworks/commit/2b1cb50ee5c8ab1395e54baa21511195bcd28e44) |
| Reviewed | 2026-10-11 |
| Declared license | AGPL-3.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | FsQueryBuilder passes a PIT join enabled flag into query conversion and multiple construction branches. This wrapper shows a switch, not the full timestamp and available-at semantics of a historical join. |

## What this project does

A feature-store platform with query-building paths.

## Mechanism inspected

FsQueryBuilder passes a PIT join enabled flag into query conversion and multiple construction branches.

## Limitation that matters

This wrapper shows a switch, not the full timestamp and available-at semantics of a historical join.

## Practical check for a trading system

Expose and test the PIT-join mode at query construction, with separate availability-time assertions.

## Why this score

3/5. The explicit PIT flag is highly relevant to lookahead control, but it is only one layer of proof.

## Source trail

[README](https://github.com/logicalclocks/hopsworks/blob/2b1cb50ee5c8ab1395e54baa21511195bcd28e44/README.md#L1); [hopsworks-api/src/main/java/io/hops/hopsworks/api/featurestore/FsQueryBuilder.java](https://github.com/logicalclocks/hopsworks/blob/2b1cb50ee5c8ab1395e54baa21511195bcd28e44/hopsworks-api/src/main/java/io/hops/hopsworks/api/featurestore/FsQueryBuilder.java#L65); [hopsworks-api/src/main/java/io/hops/hopsworks/api/featurestore/FsQueryBuilder.java](https://github.com/logicalclocks/hopsworks/blob/2b1cb50ee5c8ab1395e54baa21511195bcd28e44/hopsworks-api/src/main/java/io/hops/hopsworks/api/featurestore/FsQueryBuilder.java#L98).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
