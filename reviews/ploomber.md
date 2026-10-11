# Ploomber: incremental builds need a trustworthy product record

**Decision question:** When should a research pipeline reuse a previous task output?

| Field | Review |
| --- | --- |
| Upstream | [Ploomber](https://github.com/ploomber/ploomber) |
| Primary area | Research & Reproducibility |
| Source commit | [0659c8a030f3a439dd606f2aaa7f5352717dd2d0](https://github.com/ploomber/ploomber/commit/0659c8a030f3a439dd606f2aaa7f5352717dd2d0) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/ploomber/ploomber/blob/0659c8a030f3a439dd606f2aaa7f5352717dd2d0/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Stores product creation time, source code, and processed task parameters after a successful task run to support incremental builds. The inspected fetch path has a FIXME for deeper metadata validation; reuse should also bind actual input artifacts and failure state. |

## Mechanism worth inspecting

The [overview](https://github.com/ploomber/ploomber/blob/0659c8a030f3a439dd606f2aaa7f5352717dd2d0/README.md#L78-L91) promises reuse of unchanged pipeline results. The [metadata model](https://github.com/ploomber/ploomber/blob/0659c8a030f3a439dd606f2aaa7f5352717dd2d0/src/ploomber/products/metadata.py#L1-L53) exposes creation time, stored source, and task parameters. The [update path](https://github.com/ploomber/ploomber/blob/0659c8a030f3a439dd606f2aaa7f5352717dd2d0/src/ploomber/products/metadata.py#L219-L255) saves those fields after a successful run and hashes parameters declared as resources. This is a useful pattern for making cache decisions reviewable.

## Important limit

The [fetch path carries a FIXME](https://github.com/ploomber/ploomber/blob/0659c8a030f3a439dd606f2aaa7f5352717dd2d0/src/ploomber/products/metadata.py#L205-L217) to validate returned metadata shape and types. Timestamp and source text alone do not identify a corrected dataset or an untracked external input. Cache reuse should fail closed when input identity is unknown.

## Questions to take into your own design

- Does each cached product bind exact upstream artifact hashes?
- What happens if stored metadata is absent or malformed?

## Why this score for a trading system

Its product metadata suggests a compact pipeline cache contract, but input hashes and metadata validation need explicit treatment.

**Scope of this review:** We read the pinned README and product metadata implementation. We did not run a pipeline or evaluate every product backend.
