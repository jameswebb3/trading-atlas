# AgentOS: Can an agent evaluation be tied to the exact code and model input it used?

**Decision question:** Can an agent evaluation be tied to the exact code and model input it used?

| Field | Review |
| --- | --- |
| Upstream | [agentos-project/agentos](https://github.com/agentos-project/agentos) |
| Primary area | Agents & Decision Systems |
| Source commit | [51c320b4c6a969a0287d73edbcc96d4cecdde17e](https://github.com/agentos-project/agentos/commit/51c320b4c6a969a0287d73edbcc96d4cecdde17e) |
| Reviewed | 2026-10-11 |
| Declared license | [Apache-2.0](https://github.com/agentos-project/agentos/blob/51c320b4c6a969a0287d73edbcc96d4cecdde17e/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | AgentRun tags learn versus evaluate, the agent and environment identities, parent run and model-input run. The freeze command traverses component dependencies and pins repository commits; its git manager checks origin and uncommitted changes unless force is requested. The freeze path assumes GitHub origins and can be forced past checks. The repository depends on MLflow and broader component machinery; no agent evaluation was executed in this review. |

## What this project does

Separates learning and evaluation runs in MLflow, links a run to its model input and parent, and freezes component repositories to commits when clean and remote. A useful provenance pattern, with a large framework and GitHub/MLflow assumptions.

## Mechanism inspected

AgentRun tags learn versus evaluate, the agent and environment identities, parent run and model-input run. The freeze command traverses component dependencies and pins repository commits; its git manager checks origin and uncommitted changes unless force is requested.

## Limitation that matters

The freeze path assumes GitHub origins and can be forced past checks. The repository depends on MLflow and broader component machinery; no agent evaluation was executed in this review.

## Practical check for a trading system

For a research agent conclusion, bind the prompt and tool configuration, code commit, input data and model or policy version to the result; make force and missing provenance visible.

## Why this score

3/5 transferable: explicit model-input and code links improve reproducibility of agent experiments, but the framework is broader than trading and tied to MLflow/GitHub conventions.

## Source trail

[README.rst](https://github.com/agentos-project/agentos/blob/51c320b4c6a969a0287d73edbcc96d4cecdde17e/README.rst#L1); [agentos/agent_run.py](https://github.com/agentos-project/agentos/blob/51c320b4c6a969a0287d73edbcc96d4cecdde17e/agentos/agent_run.py#L72); [agentos/cli.py](https://github.com/agentos-project/agentos/blob/51c320b4c6a969a0287d73edbcc96d4cecdde17e/agentos/cli.py#L250); [pcs/git_manager.py](https://github.com/agentos-project/agentos/blob/51c320b4c6a969a0287d73edbcc96d4cecdde17e/pcs/git_manager.py#L33); [pcs/git_manager.py](https://github.com/agentos-project/agentos/blob/51c320b4c6a969a0287d73edbcc96d4cecdde17e/pcs/git_manager.py#L168)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
