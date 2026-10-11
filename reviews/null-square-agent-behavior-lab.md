# Agent-Behavior-Lab — Agent failure rates must display unevaluated trials

**Decision question:** Can an agent look safe when most trials errored?

| Field | Review |
| --- | --- |
| Upstream | [Null-Square/Agent-Behavior-Lab](https://github.com/Null-Square/Agent-Behavior-Lab) |
| Primary area | Agents & Decision Systems |
| Source commit | [7c6585dfb358b14111f1a11ae8cc651d7ee0b552](https://github.com/Null-Square/Agent-Behavior-Lab/commit/7c6585dfb358b14111f1a11ae8cc651d7ee0b552) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/Null-Square/Agent-Behavior-Lab/blob/7c6585dfb358b14111f1a11ae8cc651d7ee0b552/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Breakdown buckets keep PASS, FAIL and ERROR counts; failureRate divides FAIL only by PASS plus FAIL and computes a Wilson interval on that evaluated subset. When all trials error, the displayed failureRate becomes zero while evaluatedTrials is zero; errors must remain visible beside any rate. |

## What this project does

Controlled-experiment workbench for behavior of tool-using agents. [README](https://github.com/Null-Square/Agent-Behavior-Lab/blob/7c6585dfb358b14111f1a11ae8cc651d7ee0b552/README.md).

## Mechanism inspected

Breakdown buckets keep PASS, FAIL and ERROR counts; failureRate divides FAIL only by PASS plus FAIL and computes a Wilson interval on that evaluated subset. [Implementation](https://github.com/Null-Square/Agent-Behavior-Lab/blob/7c6585dfb358b14111f1a11ae8cc651d7ee0b552/backend/src/routes/results.ts#L387-L429).

## Limitation that matters

When all trials error, the displayed failureRate becomes zero while evaluatedTrials is zero; errors must remain visible beside any rate. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For agent assessments, publish denominator, error count and completion rate with every failure percentage.

## Why this score

Breakdown buckets keep PASS, FAIL and ERROR counts; failureRate divides FAIL only by PASS plus FAIL and computes a Wilson interval on that evaluated subset. When all trials error, the displayed failureRate becomes zero while evaluatedTrials is zero; errors must remain visible beside any rate.

## Source trail

[README](https://github.com/Null-Square/Agent-Behavior-Lab/blob/7c6585dfb358b14111f1a11ae8cc651d7ee0b552/README.md) · [Implementation](https://github.com/Null-Square/Agent-Behavior-Lab/blob/7c6585dfb358b14111f1a11ae8cc651d7ee0b552/backend/src/routes/results.ts#L387-L429) · [License](https://github.com/Null-Square/Agent-Behavior-Lab/blob/7c6585dfb358b14111f1a11ae8cc651d7ee0b552/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
