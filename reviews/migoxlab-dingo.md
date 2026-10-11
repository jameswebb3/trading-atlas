# Dingo — Does a fact-check summary preserve claim-level evidence

**Decision question:** Does a fact-check summary preserve claim-level evidence?

| Field | Review |
| --- | --- |
| Upstream | [Dingo](https://github.com/MigoXLab/dingo) |
| Primary area | Agents & Decision Systems |
| Source commit | [816aaae942746233851844a3f28ecb078c68a06b](https://github.com/MigoXLab/dingo/commit/816aaae942746233851844a3f28ecb078c68a06b) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/MigoXLab/dingo/blob/816aaae942746233851844a3f28ecb078c68a06b/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Useful for studying evidence records and unknown states. Prefer claim-level sources over aggregate accuracy numbers parsed from generated prose. |

## Project overview

A data-quality toolkit with agent-assisted article fact checking. [Project documentation](https://github.com/MigoXLab/dingo/blob/816aaae942746233851844a3f28ecb078c68a06b/docs/article_fact_checking_guide.md).

## Mechanism worth inspecting

The [claim error record](https://github.com/MigoXLab/dingo/blob/816aaae942746233851844a3f28ecb078c68a06b/dingo/model/llm/agent/agent_article_fact_checker.py#L1203-L1215) explicitly marks a claim unverifiable with no sources. The [legacy summary parser](https://github.com/MigoXLab/dingo/blob/816aaae942746233851844a3f28ecb078c68a06b/dingo/model/llm/agent/agent_article_fact_checker.py#L1620-L1685) separately extracts aggregate counts from text using regular expressions.

## Important limit

Aggregate counts parsed from model output are not independently verified claims. Preserve the structured claim, source and uncertainty records instead of treating an accuracy field as evidence.

## Questions to take into your own design

- Does a fact-check summary preserve claim-level evidence?
- Can every verified claim resolve to a source record rather than a parsed aggregate count?

## Why this score for a trading system

2/5: transferable evidence bookkeeping, with limited direct trading relevance and a summary path that depends on model-generated counts.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
