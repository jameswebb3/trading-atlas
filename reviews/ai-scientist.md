# AI Scientist: Autonomous experiments need an execution and review boundary

**Decision question:** Who checks an agent’s experiment before its result becomes evidence?

| Field | Review |
| --- | --- |
| Upstream | [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) |
| Primary area | Agents & Decision Systems |
| Source commit | [1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb](https://github.com/SakanaAI/AI-Scientist/commit/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb) |
| Reviewed | 2026-09-25 |
| Declared license | [AI Scientist Source Code License 1.0 (custom)](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Copies each experiment script to a run-specific file and captures a bounded subprocess result. The upstream README explicitly warns that it executes LLM-written code; a generated review is not independent verification. |

## Mechanism worth inspecting

The experiment runner snapshots experiment.py as run_N.py before invoking it and captures exit status and stderr under a timeout. A separate review module asks an LLM for a structured paper assessment. These are distinct evidence and judgment stages worth examining.

**Source trail:** [project overview](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md) · [documentation](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L27-L36) · [implementation](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/ai_scientist/perform_experiments.py#L29-L60) · [additional source](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/ai_scientist/perform_review.py#L27-L60).

## Important limit

The repository explicitly warns about autonomous execution of generated code. We did not run it. Its custom source license requires separate review, and neither a saved script nor an LLM review proves methodological validity.

## Questions to take into your own design

- Is every agent-generated experiment approved before execution?
- Can the final claim be traced to frozen code, data, run output, and an independent check?

## Why this score for a trading system

Saved scripts and bounded runs inform agent research design, but autonomous code execution and self-review limit direct trading use.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
