# Reflekt - Does a generated model retain the schema version of each source event?

**Decision question:** Does a generated model retain the schema version of each source event?

| Field | Review |
| --- | --- |
| Upstream | [GClunies/reflekt](https://github.com/GClunies/reflekt) |
| Primary area | Data Quality Lineage |
| Source commit | [9b3f0ff9e22da1b9f9ac669715c616f72d064b0f](https://github.com/GClunies/reflekt/commit/9b3f0ff9e22da1b9f9ac669715c616f72d064b0f) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Builds dbt views and documentation from versioned JSON schemas, adding source and schema identifiers to the generated columns. The generated schema_id is a constant from the selected schema file; without a row-version filter it does not prove that each source row used that schema. |

## What this project does

A warehouse-first event-data governance tool. It reads versioned JSON schemas and generates dbt source, model and documentation artifacts.

## Mechanism inspected

The builder reads each schema file, derives a versioned model filename, checks for expected warehouse columns and emits a dbt view. The view includes source_schema, source_table and schema_id constants, making the chosen schema visible in downstream queries.

## Limitation that matters

The model CTE selects every row from the source table, with a filter only when one is supplied through configuration. The schema_id column is inserted as a literal for the generated model, not read from each event. If a source table mixes event versions, a view can label rows with a schema they did not use. This is an inference from the generated SQL path, not a runtime check of a real warehouse.

## Practical check for a trading system

For market events, carry producer schema or decoder version per record and validate it against the selected model. A generated view should reject or isolate rows whose actual version is unknown rather than stamp all rows with its own build-time version.

## Why this score

3/5 because versioned schema-to-model generation is a concrete transferable lineage pattern, and the source exposes an important distinction between model provenance and row provenance.

## Source trail

[README](https://github.com/GClunies/reflekt/blob/9b3f0ff9e22da1b9f9ac669715c616f72d064b0f/README.md#L1); [Versioned model name](https://github.com/GClunies/reflekt/blob/9b3f0ff9e22da1b9f9ac669715c616f72d064b0f/reflekt/builder/dbt.py#L148); [Source selection and optional filter](https://github.com/GClunies/reflekt/blob/9b3f0ff9e22da1b9f9ac669715c616f72d064b0f/reflekt/builder/dbt.py#L164); [Injected schema ID](https://github.com/GClunies/reflekt/blob/9b3f0ff9e22da1b9f9ac669715c616f72d064b0f/reflekt/builder/dbt.py#L289); [Schema iteration](https://github.com/GClunies/reflekt/blob/9b3f0ff9e22da1b9f9ac669715c616f72d064b0f/reflekt/builder/dbt.py#L545); [License](https://github.com/GClunies/reflekt/blob/9b3f0ff9e22da1b9f9ac669715c616f72d064b0f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
