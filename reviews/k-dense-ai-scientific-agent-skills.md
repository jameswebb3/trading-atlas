# Scientific Agent Skills — Does a leakage audit distinguish missing evidence from a clean scan

**Decision question:** Does a leakage audit distinguish missing evidence from a clean scan?

| Field | Review |
| --- | --- |
| Upstream | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| Primary area | Data Quality & Lineage |
| Source commit | [49c6e97775eaa18ba791bebe23162a70ae601c18](https://github.com/K-Dense-AI/scientific-agent-skills/commit/49c6e97775eaa18ba791bebe23162a70ae601c18) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/49c6e97775eaa18ba791bebe23162a70ae601c18/LICENSE.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The useful part is the audit result contract: report what was checked, what was truncated and what could not be assessed. Interpret overlap using the experiment's actual information boundary. |

## Project overview

A collection of scientific workflow skills and supporting audit scripts. [Project documentation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/49c6e97775eaa18ba791bebe23162a70ae601c18/docs/skills.md).

## Mechanism worth inspecting

The [tabular audit](https://github.com/K-Dense-AI/scientific-agent-skills/blob/49c6e97775eaa18ba791bebe23162a70ae601c18/skills/exploratory-data-analysis/scripts/_tabular.py#L838-L899) records interval and entity overlap, parsing failures and scan truncation. It distinguishes missing split information from no findings in the rows scanned.

## Important limit

Entity overlap is not automatically leakage: repeated assets across trading folds can be legitimate. A bounded scan also cannot clear unscanned rows.

## Questions to take into your own design

- Does a leakage audit distinguish missing evidence from a clean scan?
- Are scan truncation, parser failures and missing split keys preserved in the audit result?

## Why this score for a trading system

3/5: explicit coverage and unknown states are transferable; the broad scientific skill collection is not itself a trading evaluation framework.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
