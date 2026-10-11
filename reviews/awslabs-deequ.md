# Deequ — Can incremental quality checks merge batches without averaging averages

**Decision question:** Can incremental quality checks merge batches without averaging averages?

| Field | Review |
| --- | --- |
| Upstream | [Deequ](https://github.com/awslabs/deequ) |
| Primary area | Data Quality & Lineage |
| Source commit | [d7f778310cadcfaf7ad641bdfe07368416cc7c64](https://github.com/awslabs/deequ/commit/d7f778310cadcfaf7ad641bdfe07368416cc7c64) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/awslabs/deequ/blob/d7f778310cadcfaf7ad641bdfe07368416cc7c64/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful data-quality reference for mergeable metrics. Keeping sum and count avoids averaging batch means, but duplicates, revisions and changed filters require a separate dataset-identity contract. |

## Project overview

Deequ separates dataset analyzers, retained intermediate states and checks, allowing multiple quality metrics to share scans. [Project documentation](https://github.com/awslabs/deequ/blob/d7f778310cadcfaf7ad641bdfe07368416cc7c64/docs/key-concepts.md#L4-L25).

## Mechanism worth inspecting

MeanState stores a sum and a count, merges those sufficient statistics, and returns NaN for an empty count. The analyzer applies the same selection condition to both aggregates. [Mergeable metric](https://github.com/awslabs/deequ/blob/d7f778310cadcfaf7ad641bdfe07368416cc7c64/src/main/scala/com/amazon/deequ/analyzers/Mean.scala#L25-L53).

## Important limit

Addition is valid for compatible nonoverlapping contributions. The inspected state merge does not detect replayed batches, revised rows or a changed filter; identity and replacement semantics belong in the surrounding pipeline.

## Questions to take into your own design

- Can incremental quality checks merge batches without averaging averages?
- How do batch identity and replacement rules prevent double-counting retained metric state?

## Why this score for a trading system

3/5: precise transferable quality-state arithmetic; adopting its Spark stack adds little to a small existing ingestion system.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
