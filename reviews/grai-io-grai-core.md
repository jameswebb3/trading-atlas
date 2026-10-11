# Grai — Lineage carries preservation rules

**Decision question:** Which downstream constraints should a type change invalidate?

| Field | Review |
| --- | --- |
| Upstream | [Grai](https://github.com/grai-io/grai-core) |
| Primary area | Data Quality & Lineage |
| Source commit | [a24e9d4c2506cb00b786b23339c43db752c5116f](https://github.com/grai-io/grai-core/commit/a24e9d4c2506cb00b786b23339c43db752c5116f) |
| Reviewed | 2026-09-27 |
| Declared license | [Permissive custom license; see text](https://github.com/grai-io/grai-core/blob/a24e9d4c2506cb00b786b23339c43db752c5116f/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | GraphAnalyzer traverses column successors, consults edge metadata indicating whether type or uniqueness is preserved, and returns paths with compatibility results. The impact result depends on captured nodes and edge semantics. |

## Project overview

Data-lineage tools connecting schemas and testing the impact of upstream metadata changes. [Documentation](https://github.com/grai-io/grai-core/blob/a24e9d4c2506cb00b786b23339c43db752c5116f/README.md).

## Mechanism worth inspecting

GraphAnalyzer traverses column successors, consults edge metadata indicating whether type or uniqueness is preserved, and returns paths with compatibility results. [Source](https://github.com/grai-io/grai-core/blob/a24e9d4c2506cb00b786b23339c43db752c5116f/grai-graph/src/grai_graph/analysis.py#L15-L45).

## Important limit

The impact result depends on captured nodes and edge semantics. The simpler downstream_nodes accessor returns the first BFS successor group, so it should not be assumed to enumerate every transitive descendant. [Evidence 1](https://github.com/grai-io/grai-core/blob/a24e9d4c2506cb00b786b23339c43db752c5116f/grai-graph/src/grai_graph/analysis.py#L15-L45). [Evidence 2](https://github.com/grai-io/grai-core/blob/a24e9d4c2506cb00b786b23339c43db752c5116f/grai-graph/src/grai_graph/analysis.py#L61-L127). [Evidence 3](https://github.com/grai-io/grai-core/blob/a24e9d4c2506cb00b786b23339c43db752c5116f/grai-graph/src/grai_graph/analysis.py#L144-L168).

## Questions to take into your own design

- Are transformation edges explicit about which properties they preserve?
- Does an impact query test a three-hop chain and a node with no successors?

## Why this score for a trading system

A concrete lineage-testing mechanism useful to research evidence; graph completeness and accessor scope need explicit tests.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
