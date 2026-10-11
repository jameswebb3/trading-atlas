# PhysGym: Can a research agent bypass its declared hidden-truth test quota?

**Decision question:** Can a research agent bypass its declared hidden-truth test quota?

| Field | Review |
| --- | --- |
| Upstream | [principia-ai/PhysGym](https://github.com/principia-ai/PhysGym) |
| Primary area | Agents & Decision Systems |
| Source commit | [fe68079c0921029dde679ed44bc3192dd3b270ab](https://github.com/principia-ai/PhysGym/commit/fe68079c0921029dde679ed44bc3192dd3b270ab) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/principia-ai/PhysGym/blob/fe68079c0921029dde679ed44bc3192dd3b270ab/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | run_experiment rejects sample batches above sample_quota and records observations. test_hypothesis evaluates a candidate against the true environment and saves the result. A separate orchestration path decrements test_quota. The benchmark studies physics, not trading. Direct ResearchInterface access appears to bypass the test budget; no runtime test or agent-performance claim was made here. |

## What this project does

Provides sample and test quotas for physics discovery. The direct test_hypothesis method queries the true equation without debiting test_quota, so budget enforcement must sit at the callable boundary.

## Mechanism inspected

run_experiment rejects sample batches above sample_quota and records observations. test_hypothesis evaluates a candidate against the true environment and saves the result. A separate orchestration path decrements test_quota.

## Limitation that matters

The benchmark studies physics, not trading. Direct ResearchInterface access appears to bypass the test budget; no runtime test or agent-performance claim was made here.

## Practical check for a trading system

Hide the target from the agent, enforce quota at every test entry point and persist the balance through resume.

## Why this score

2/5 transferable: explicit budgets matter for honest agent evaluations, but the shown boundary is bypassable.

## Source trail

[README.md](https://github.com/principia-ai/PhysGym/blob/fe68079c0921029dde679ed44bc3192dd3b270ab/README.md#L1); [physgym/interface.py](https://github.com/principia-ai/PhysGym/blob/fe68079c0921029dde679ed44bc3192dd3b270ab/physgym/interface.py#L99); [physgym/interface.py](https://github.com/principia-ai/PhysGym/blob/fe68079c0921029dde679ed44bc3192dd3b270ab/physgym/interface.py#L257); [physgym/interface.py](https://github.com/principia-ai/PhysGym/blob/fe68079c0921029dde679ed44bc3192dd3b270ab/physgym/interface.py#L334); [physgym/interface.py](https://github.com/principia-ai/PhysGym/blob/fe68079c0921029dde679ed44bc3192dd3b270ab/physgym/interface.py#L688); [physgym/utils/metrics.py](https://github.com/principia-ai/PhysGym/blob/fe68079c0921029dde679ed44bc3192dd3b270ab/physgym/utils/metrics.py#L110)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
