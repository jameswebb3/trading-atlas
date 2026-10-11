# dbt Doctor — A declared unique key is not uniqueness evidence

**Decision question:** What does a unique-key lint check actually prove?

| Field | Review |
| --- | --- |
| Upstream | [dbt Doctor](https://github.com/northgraindata/dbt-doctor) |
| Primary area | Data Quality & Lineage |
| Source commit | [be424bd145a6e58b1017b117ff18e9e575a9dcc3](https://github.com/northgraindata/dbt-doctor/commit/be424bd145a6e58b1017b117ff18e9e575a9dcc3) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/northgraindata/dbt-doctor/blob/be424bd145a6e58b1017b117ff18e9e575a9dcc3/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The incremental-unique-key rule detects a declared unique_key using SQL-config and YAML patterns, then reports a missing declaration. This rule checks configuration presence, not actual uniqueness in data. |

## Project overview

Static analysis and health checks for dbt project definitions. [Documentation](https://github.com/northgraindata/dbt-doctor/blob/be424bd145a6e58b1017b117ff18e9e575a9dcc3/packages/dbt-doctor/README.md).

## Mechanism worth inspecting

The incremental-unique-key rule detects a declared unique_key using SQL-config and YAML patterns, then reports a missing declaration. [Source](https://github.com/northgraindata/dbt-doctor/blob/be424bd145a6e58b1017b117ff18e9e575a9dcc3/packages/dbt-doctor-rules/src/rules/incremental-unique-key.ts#L1-L37).

## Important limit

This rule checks configuration presence, not actual uniqueness in data. Its pass cannot substitute for duplicate-key or revision-identity checks on the produced dataset. [Evidence 1](https://github.com/northgraindata/dbt-doctor/blob/be424bd145a6e58b1017b117ff18e9e575a9dcc3/packages/dbt-doctor-rules/src/rules/incremental-unique-key.ts#L1-L37). [Evidence 2](https://github.com/northgraindata/dbt-doctor/blob/be424bd145a6e58b1017b117ff18e9e575a9dcc3/packages/dbt-doctor/README.md#L11-L49).

## Questions to take into your own design

- Is static configuration evidence labeled separately from data validation?
- Is the declared key actually unique at the dataset's intended grain?

## Why this score for a trading system

A narrow lint/data-contract distinction; bringing in dbt or a health-score CLI would add little to this use.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
