# A lineage graph needs schema metadata to resolve wildcard columns

**Decision question:** Can SELECT-star lineage tell you which features changed after a schema revision?

| Field | Review |
| --- | --- |
| Upstream | [SQLLineage](https://github.com/reata/sqllineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [a10d47e7368d0b6658a69f7be51dce6a95d9c286](https://github.com/reata/sqllineage/commit/a10d47e7368d0b6658a69f7be51dce6a95d9c286) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/reata/sqllineage/blob/a10d47e7368d0b6658a69f7be51dce6a95d9c286/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | SQLLineage derives table and column dependencies from SQL, but wildcard expansion and unqualified joins require schema metadata. Its default metadata provider is empty. Useful for change-impact review; a dependency graph is not evidence of consumed data bytes or historical feature availability. |

## Mechanism worth inspecting

The [README](https://github.com/reata/sqllineage/blob/a10d47e7368d0b6658a69f7be51dce6a95d9c286/README.md#L14-L21) describes AST-based lineage. The [metadata guide](https://github.com/reata/sqllineage/blob/a10d47e7368d0b6658a69f7be51dce6a95d9c286/docs/gear_up/metadata.rst#L5-L39) shows unresolved wildcard output when metadata is missing. The [runner defaults](https://github.com/reata/sqllineage/blob/a10d47e7368d0b6658a69f7be51dce6a95d9c286/sqllineage/runner.py#L40-L73) accept a dummy provider, and the [column-path output](https://github.com/reata/sqllineage/blob/a10d47e7368d0b6658a69f7be51dce6a95d9c286/sqllineage/runner.py#L170-L199) returns ordered dependency paths.

## Important limit

Parsed dependency is declared structure, not a run receipt. Dynamic SQL, unsupported statements, dialect choice, catalog vintage, and actual dataset identity need separate evidence.

## Questions to take into your own design

- Which schema version resolved every wildcard and unqualified column?
- Can the dependency graph be joined to an actual run's data manifest?

## Why this score for a trading system

3/5: Schema-aware SQL impact analysis is useful for feature-pipeline review, provided it is not mistaken for runtime or point-in-time provenance.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
