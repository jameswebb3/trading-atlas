# ArcticDB: pin several time-series symbols to one named snapshot

**Decision question:** Can a research run read a stable set of data versions across several symbols?

| Field | Review |
| --- | --- |
| Upstream | [man-group/ArcticDB](https://github.com/man-group/ArcticDB) |
| Primary area | Research & Reproducibility |
| Source commit | [7d30a6eefe709e5379f1dd7f38b03074750cf1be](https://github.com/man-group/ArcticDB/commit/7d30a6eefe709e5379f1dd7f38b03074750cf1be) |
| Reviewed | 2026-09-25 |
| Declared license | [Business Source License 1.1](https://github.com/man-group/ArcticDB/blob/7d30a6eefe709e5379f1dd7f38b03074750cf1be/LICENSE.txt) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Creates a named snapshot that pins versions of several time-series symbols. Its API warns that concurrent writes with pruning can damage a snapshot, and its source-available production terms require separate review. |

## Mechanism worth inspecting

The [README](https://github.com/man-group/ArcticDB/blob/7d30a6eefe709e5379f1dd7f38b03074750cf1be/README.md#L23-L42) describes a versioned DataFrame store for time series. The [snapshot tutorial](https://github.com/man-group/ArcticDB/blob/7d30a6eefe709e5379f1dd7f38b03074750cf1be/docs/mkdocs/docs/tutorials/snapshots.md#L1-L35) uses a named multi-symbol snapshot to tie factors to pricing data. The pinned [Library.snapshot API](https://github.com/man-group/ArcticDB/blob/7d30a6eefe709e5379f1dd7f38b03074750cf1be/python/arcticdb/version_store/library.py#L2689-L2733) accepts an explicit symbol-version map, preserves referenced versions after later writes, and rejects duplicate snapshot names. That is a concrete pattern for recording the exact market-data and feature versions used by a research run.

## Important limits

The same API [warns](https://github.com/man-group/ArcticDB/blob/7d30a6eefe709e5379f1dd7f38b03074750cf1be/python/arcticdb/version_store/library.py#L2697-L2706) that concurrent writes with prune-previous-versions can corrupt affected snapshot symbols. A named snapshot also does not prove decision-time availability or source completeness. The [README](https://github.com/man-group/ArcticDB/blob/7d30a6eefe709e5379f1dd7f38b03074750cf1be/README.md#L23-L28) and [Business Source License](https://github.com/man-group/ArcticDB/blob/7d30a6eefe709e5379f1dd7f38b03074750cf1be/LICENSE.txt#L1-L35) should be read together before considering use; this is a source review, not licensing advice.

## Questions to take into your own design

- Are all inputs pinned to explicit versions in one experiment receipt?
- Can pruning race with snapshot creation?
- Is snapshot identity kept separate from causal availability checks?

## Why this score for a trading system

Named multi-symbol snapshots directly support trading experiment provenance, but the concurrent-prune caveat and source-available terms constrain practical use.

**Scope of this review:** We read pinned documentation, snapshot API code, and the license. We did not install or run ArcticDB or verify its storage behavior.
