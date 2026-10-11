# thanos - Verify that every expected block reached storage

**Decision question:** Does a successful shipper call mean every local block was uploaded?

| Field | Review |
| --- | --- |
| Upstream | [thanos-io/thanos](https://github.com/thanos-io/thanos) |
| Primary area | Operations & Observability |
| Source commit | [c0ba8a66ae74fc130fd0977dd5de0c9ce679f7ea](https://github.com/thanos-io/thanos/commit/c0ba8a66ae74fc130fd0977dd5de0c9ce679f7ea) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/thanos-io/thanos/blob/c0ba8a66ae74fc130fd0977dd5de0c9ce679f7ea/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | AreAllBlocksUploaded enumerates local block metadata and compares every block ID against the persisted uploaded-ID set. It verifies metadata membership, not remote payload bytes or downstream query visibility; those require separate checks. |

## What this project does

A Prometheus companion ships immutable metric blocks to object storage. [README](https://github.com/thanos-io/thanos/blob/c0ba8a66ae74fc130fd0977dd5de0c9ce679f7ea/README.md).

## Mechanism inspected

AreAllBlocksUploaded enumerates local block metadata and compares every block ID against the persisted uploaded-ID set. [Implementation](https://github.com/thanos-io/thanos/blob/c0ba8a66ae74fc130fd0977dd5de0c9ce679f7ea/pkg/shipper/shipper.go#L306-L335).

## Limitation that matters

It verifies metadata membership, not remote payload bytes or downstream query visibility; those require separate checks. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

For archive/backfill partitions, compare the expected manifest IDs with uploaded IDs and then spot-check query readability.

## Why this score

AreAllBlocksUploaded enumerates local block metadata and compares every block ID against the persisted uploaded-ID set. It verifies metadata membership, not remote payload bytes or downstream query visibility; those require separate checks.

## Source trail

[README](https://github.com/thanos-io/thanos/blob/c0ba8a66ae74fc130fd0977dd5de0c9ce679f7ea/README.md) - [Implementation](https://github.com/thanos-io/thanos/blob/c0ba8a66ae74fc130fd0977dd5de0c9ce679f7ea/pkg/shipper/shipper.go#L306-L335) - [License](https://github.com/thanos-io/thanos/blob/c0ba8a66ae74fc130fd0977dd5de0c9ce679f7ea/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
