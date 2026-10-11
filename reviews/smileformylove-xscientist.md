# XScientist - Can a generated research report pass structural checks yet remain wrong?

**Decision question:** Can a generated research report pass structural checks yet remain wrong?

| Field | Review |
| --- | --- |
| Upstream | [smileformylove/XScientist](https://github.com/smileformylove/XScientist) |
| Primary area | Agents & Decision Systems |
| Source commit | [f6c1ec2065bf9902fbcc9686ecbcb94ef621ee2a](https://github.com/smileformylove/XScientist/commit/f6c1ec2065bf9902fbcc9686ecbcb94ef621ee2a) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The guardrail returns machine-readable findings for missing sections, references and markers, and blocks required-section failures. Those text and format checks do not validate statistical claims or result provenance. |

## What this project does

An AI scientist workflow with write-up guardrails.

## Mechanism inspected

The guardrail returns machine-readable findings for missing sections, references and markers, and blocks required-section failures.

## Limitation that matters

Those text and format checks do not validate statistical claims or result provenance.

## Practical check for a trading system

Use structural checks as a publication gate alongside independent evidence review.

## Why this score

2/5. The guardrail output is reusable, but it cannot certify a trading finding.

## Source trail

[README](https://github.com/smileformylove/XScientist/blob/f6c1ec2065bf9902fbcc9686ecbcb94ef621ee2a/README.md#L1); [ai_scientist/writeup_guardrails.py](https://github.com/smileformylove/XScientist/blob/f6c1ec2065bf9902fbcc9686ecbcb94ef621ee2a/ai_scientist/writeup_guardrails.py#L318); [ai_scientist/writeup_guardrails.py](https://github.com/smileformylove/XScientist/blob/f6c1ec2065bf9902fbcc9686ecbcb94ef621ee2a/ai_scientist/writeup_guardrails.py#L413).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
