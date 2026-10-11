# Co-Scientist - Completed review stages need content, not only a status flag

**Decision question:** When should a research-agent review count as completed?

| Field | Review |
| --- | --- |
| Upstream | [panjose/Co-Scientist](https://github.com/panjose/Co-Scientist) |
| Primary area | Agents & Decision Systems |
| Source commit | [31240805f7bcb3652765a008dd2eae36a638e398](https://github.com/panjose/Co-Scientist/commit/31240805f7bcb3652765a008dd2eae36a638e398) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Uses typed review-stage statuses and rejects some completed artifacts that lack substantive stage content. Presence and placeholder checks do not verify evidential support, and unknown fields are ignored by the inspected contract models. |

## What this project does

A file-first research-agent workflow that generates, reviews and ranks hypotheses. The inspected contracts and synchronization path map stage artifacts back to a canonical hypothesis.

## Mechanism inspected

Review stages have explicit pending, running, completed and failed states, with evidence bundle identifiers where relevant. The synchronizer rejects a completed full review with no preferences, constraints, retrieval result or evidence link; deep verification requires an assumption and summary requires content. Source tests exercise the completed-summary guard.

## Limitation that matters

The content guard checks presence and a small placeholder list, not scientific correctness or whether cited evidence actually supports the claim. Pydantic stage models also ignore extra fields in the inspected contracts, so an unrecognized field is not necessarily a schema failure. This is a source review, not a runtime or security test.

## Practical check for a trading system

For an automated trading study, do not equate a completed flag with a valid conclusion. Require stage-specific evidence fields, source identity and independent validity checks before a candidate enters a decision ledger.

## Why this score

3/5 because the source and tests provide a concrete transferable completion gate for research agents, with semantic truth still left to separate validation.

## Source trail

[README](https://github.com/panjose/Co-Scientist/blob/31240805f7bcb3652765a008dd2eae36a638e398/README.md#L45); [Stage contracts](https://github.com/panjose/Co-Scientist/blob/31240805f7bcb3652765a008dd2eae36a638e398/packages/agent_contracts/review.py#L64); [Content gate](https://github.com/panjose/Co-Scientist/blob/31240805f7bcb3652765a008dd2eae36a638e398/packages/run_artifacts/review_sync.py#L72); [Review sync tests](https://github.com/panjose/Co-Scientist/blob/31240805f7bcb3652765a008dd2eae36a638e398/tests/test_review_sync.py#L63); [License](https://github.com/panjose/Co-Scientist/blob/31240805f7bcb3652765a008dd2eae36a638e398/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
