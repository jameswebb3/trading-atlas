# ResearchClawBench: retain criterion-level evidence behind an agent score

**Decision question:** Can a research-agent rating expose each criterion rather than only a total?

| Field | Review |
| --- | --- |
| Upstream | [ResearchClawBench](https://github.com/InternScience/ResearchClawBench) |
| Primary area | Agents & Decision Systems |
| Source commit | [01bc2371f698f755892935ef2965a95a790ff0db](https://github.com/InternScience/ResearchClawBench/commit/01bc2371f698f755892935ef2965a95a790ff0db) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/InternScience/ResearchClawBench/blob/01bc2371f698f755892935ef2965a95a790ff0db/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Evaluates scientific-agent reports against weighted paper-derived checklists. The inspected scorer retains per-item reasoning and distinguishes missing evaluation responses, making it a reporting reference while leaving objective verification dependent on an LLM judge. |

## Project overview

A benchmark asks agents to conduct research and compares their reports with reference studies. [Project documentation](https://github.com/InternScience/ResearchClawBench/blob/01bc2371f698f755892935ef2965a95a790ff0db/README.md#L29-L42).

## Mechanism worth inspecting

[Evaluation documentation](https://github.com/InternScience/ResearchClawBench/blob/01bc2371f698f755892935ef2965a95a790ff0db/README.md#L183-L218) defines criterion weights and text/image types. [Scoring](https://github.com/InternScience/ResearchClawBench/blob/01bc2371f698f755892935ef2965a95a790ff0db/evaluation/score.py#L149-L180) stores score and reasoning for each item, with an explicit parse-failure reason. [Aggregation](https://github.com/InternScience/ResearchClawBench/blob/01bc2371f698f755892935ef2965a95a790ff0db/evaluation/score.py#L253-L280) retains the item list and denominator alongside the weighted total.

## Important limit

The [prompt builder](https://github.com/InternScience/ResearchClawBench/blob/01bc2371f698f755892935ef2965a95a790ff0db/evaluation/score.py#L97-L119) supplies agent report text to a model; it does not execute a numerical verification. A [failed evaluation](https://github.com/InternScience/ResearchClawBench/blob/01bc2371f698f755892935ef2965a95a790ff0db/evaluation/score.py#L175-L180) becomes score zero, so evaluator availability must remain distinct from a scientific failure. Report content is untrusted input to the judge.

## Questions to take into your own design

- Are computed checks separated from narrative judgments?
- Does evaluator failure remain distinguishable from failed scientific evidence?

## Why this score for a trading system

2/5: a useful adjacent checklist-report pattern, constrained by subjective judging and no independent numerical replication.

**Scope of this review:** README evaluation documentation, full scorer inputs/per-item handling/aggregation source; benchmark not run.
