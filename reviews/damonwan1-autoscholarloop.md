# AutoScholarLoop — Can a progress index serve as an immutable experiment ledger

**Decision question:** Can a progress index serve as an immutable experiment ledger?

| Field | Review |
| --- | --- |
| Upstream | [AutoScholarLoop](https://github.com/damonwan1/AutoScholarLoop) |
| Primary area | Agents & Decision Systems |
| Source commit | [8206c7581049a78cab9cf20723d70a846b43e7df](https://github.com/damonwan1/AutoScholarLoop/commit/8206c7581049a78cab9cf20723d70a846b43e7df) |
| Reviewed | 2026-09-26 |
| Declared license | [AI Scientist Source Code License (custom; disclosure conditions)](https://github.com/damonwan1/AutoScholarLoop/blob/8206c7581049a78cab9cf20723d70a846b43e7df/LICENSE.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Provides a readable staged workflow. Its overwrite and interrupted-write behavior must be checked before reusing the progress index as a research ledger. |

## Project overview

A staged research-agent workflow with checkpoints, canonical artifacts and a progress index. [Project documentation](https://github.com/damonwan1/AutoScholarLoop/blob/8206c7581049a78cab9cf20723d70a846b43e7df/docs/WORKFLOW_CONTRACT.md).

## Mechanism worth inspecting

[Checkpoint writes](https://github.com/damonwan1/AutoScholarLoop/blob/8206c7581049a78cab9cf20723d70a846b43e7df/src/open_research_agent/core/checkpoints.py#L35-L63) save a stage/round artifact, append progress and update state in separate operations. Canonical outputs are written to reusable paths; the [state update](https://github.com/damonwan1/AutoScholarLoop/blob/8206c7581049a78cab9cf20723d70a846b43e7df/src/open_research_agent/core/checkpoints.py#L66-L87) is another file write.

## Important limit

Repeated keys can overwrite artifacts, and separate writes do not establish a transaction. The workflow contract specifies outputs, but checkpoint presence alone does not prove experiment validity.

## Questions to take into your own design

- Can a progress index serve as an immutable experiment ledger?
- Can a crash between artifact, progress and state writes leave a false completion entry?

## Why this score for a trading system

2/5: useful output contracts, but basic checkpoint storage is already common and does not establish immutable evidence.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
