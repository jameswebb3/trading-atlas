# CLI Agentic Workflow: Can an iterative agent run be resumed without rewriting its evidence?

**Decision question:** Can an iterative agent run be resumed without rewriting its evidence?

| Field | Review |
| --- | --- |
| Upstream | [aigengame/cli-agentic-workflow](https://github.com/aigengame/cli-agentic-workflow) |
| Primary area | Agents & Decision Systems |
| Source commit | [d092b42661605aae843c8e2f0209a9f89d012d91](https://github.com/aigengame/cli-agentic-workflow/commit/d092b42661605aae843c8e2f0209a9f89d012d91) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/aigengame/cli-agentic-workflow/blob/d092b42661605aae843c8e2f0209a9f89d012d91/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The controller materializes each iteration as a distinct run and substitutes a prior structured output into a named input rather than templating text. A group.json carries authoritative loop state; SQLite records run, node, attempt and group membership for inspection. The README calls the project pre-release with implementation in progress. The group JSON and SQLite membership are two views with an explicit authority rule; no trading or scientific validity check is supplied. |

## What this project does

Runs each loop iteration as an immutable child run, stores group control state separately, and passes feedback through structured fields. This preserves an auditable sequence; the project is pre-release and does not validate trading decisions.

## Mechanism inspected

The controller materializes each iteration as a distinct run and substitutes a prior structured output into a named input rather than templating text. A group.json carries authoritative loop state; SQLite records run, node, attempt and group membership for inspection.

## Limitation that matters

The README calls the project pre-release with implementation in progress. The group JSON and SQLite membership are two views with an explicit authority rule; no trading or scientific validity check is supplied.

## Practical check for a trading system

For a research agent, persist one input/output/feedback record per attempt and a separate controller decision. On resume, verify the previous attempt identity and prevent a new attempt from silently replacing its evidence.

## Why this score

3/5 transferable: explicit immutable attempts and authority of state are useful for research provenance, but the tool is a pre-release agent orchestrator rather than a validated trading research system.

## Source trail

[README.md](https://github.com/aigengame/cli-agentic-workflow/blob/d092b42661605aae843c8e2f0209a9f89d012d91/README.md#L13); [src/caw/controller.py](https://github.com/aigengame/cli-agentic-workflow/blob/d092b42661605aae843c8e2f0209a9f89d012d91/src/caw/controller.py#L1); [src/caw/state.py](https://github.com/aigengame/cli-agentic-workflow/blob/d092b42661605aae843c8e2f0209a9f89d012d91/src/caw/state.py#L1); [src/caw/state.py](https://github.com/aigengame/cli-agentic-workflow/blob/d092b42661605aae843c8e2f0209a9f89d012d91/src/caw/state.py#L25)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
