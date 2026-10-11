# Marmot — Can a lineage graph explain a particular failed pipeline run

**Decision question:** Can a lineage graph explain a particular failed pipeline run?

| Field | Review |
| --- | --- |
| Upstream | [Marmot](https://github.com/marmotdata/marmot) |
| Primary area | Data Quality & Lineage |
| Source commit | [7f049494e5abe00d4b46df146db231ebe30847a4](https://github.com/marmotdata/marmot/commit/7f049494e5abe00d4b46df146db231ebe30847a4) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/marmotdata/marmot/blob/7f049494e5abe00d4b46df146db231ebe30847a4/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Connects dataset lineage with run history. Useful for tracing how an asset was produced, while run completion must remain separate evidence. |

## Project overview

Data catalog supporting asset discovery, lineage, ownership and metadata access for agents. [Project documentation](https://github.com/marmotdata/marmot/blob/7f049494e5abe00d4b46df146db231ebe30847a4/README.md#L14-L36).

## Mechanism worth inspecting

OpenLineage ingestion records run IDs, inputs, outputs and event types, then processes assets and relationships before saving run history. [Docs](https://github.com/marmotdata/marmot/blob/7f049494e5abe00d4b46df146db231ebe30847a4/web/docs/docs/open-lineage.md#L26-L49), [event model and ingestion](https://github.com/marmotdata/marmot/blob/7f049494e5abe00d4b46df146db231ebe30847a4/internal/core/lineage/openlineage.go#L55-L131).

## Important limit

The documentation calls OpenLineage compatibility experimental. The inspected service performs several sequential operations; a graph edge alone should not be interpreted as proof of a completed run. [Compatibility](https://github.com/marmotdata/marmot/blob/7f049494e5abe00d4b46df146db231ebe30847a4/web/docs/docs/open-lineage.md#L22-L24), [processing sequence](https://github.com/marmotdata/marmot/blob/7f049494e5abe00d4b46df146db231ebe30847a4/internal/core/lineage/openlineage.go#L101-L131).

## Questions to take into your own design

- Can a lineage graph explain a particular failed pipeline run?
- Can lineage ingestion be distinguished from a completed and verified experiment run?

## Why this score for a trading system

3/5: transferable run-aware lineage; a generic catalog does not establish causal availability of market data.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
