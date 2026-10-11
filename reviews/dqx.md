# Valid and quarantined rows are not always disjoint

**Decision question:** Can warning rows appear in both accepted and rejected data outputs?

| Field | Review |
| --- | --- |
| Upstream | [DQX](https://github.com/databrickslabs/dqx) |
| Primary area | Data Quality & Lineage |
| Source commit | [ad87066c912e948f0df6d08a00ed2118f7bd1031](https://github.com/databrickslabs/dqx/commit/ad87066c912e948f0df6d08a00ed2118f7bd1031) |
| Reviewed | 2026-09-26 |
| Declared license | [Databricks License (service-restricted)](https://github.com/databrickslabs/dqx/blob/ad87066c912e948f0df6d08a00ed2118f7bd1031/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | DQX treats warning rows as valid for downstream use and also includes them in the invalid output for inspection. Summing those outputs can double-count records. The split semantics are valuable to inspect, but the pinned license limits use to Databricks services. |

## Mechanism worth inspecting

The [README](https://github.com/databrickslabs/dqx/blob/ad87066c912e948f0df6d08a00ed2118f7bd1031/README.md#L20-L34) distinguishes check levels and reactions, and the [application guide](https://github.com/databrickslabs/dqx/blob/ad87066c912e948f0df6d08a00ed2118f7bd1031/docs/dqx/docs/guide/quality_checks_apply.mdx#L24-L45) documents split outputs and skipped checks. The [filters](https://github.com/databrickslabs/dqx/blob/ad87066c912e948f0df6d08a00ed2118f7bd1031/src/databricks/labs/dqx/engine.py#L372-L399) include warnings in get_invalid while get_valid excludes only errors. [License scope](https://github.com/databrickslabs/dqx/blob/ad87066c912e948f0df6d08a00ed2118f7bd1031/LICENSE#L14-L23) restricts use to the service context.

## Important limit

The two output populations are intentionally overlapping, not a partition. Warning detail is dropped from the valid output. A self-hosted trading stack should build its own explicit status contract rather than assume unrestricted reuse of this implementation.

## Questions to take into your own design

- Are counts reconciled through exclusive status classes or overlapping output sets?
- Does downstream research retain warning evidence after accepting a row?

## Why this score for a trading system

2/5: The warning-versus-error contract is a useful pattern and caution, but the service-restricted license and platform coupling reduce its utility for a self-hosted trading stack.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
