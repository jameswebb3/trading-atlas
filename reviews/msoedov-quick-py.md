# quick.py - Will a failing generated case be reduced to a useful minimal trace?

**Decision question:** Will a failing generated case be reduced to a useful minimal trace?

| Field | Review |
| --- | --- |
| Upstream | [msoedov/quick.py](https://github.com/msoedov/quick.py) |
| Primary area | Testing & Verification |
| Source commit | [5c89c11c7f6bc1fabbee757a8bb217dea08e359c](https://github.com/msoedov/quick.py/commit/5c89c11c7f6bc1fabbee757a8bb217dea08e359c) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its shrink loop varies one input, reruns the validator and returns a simplified failing schema. It caps attempts and uses a local greedy pass; the returned example need not be globally minimal or cover cross-field failure interactions. |

## What this project does

A Python property-testing library with shrinking.

## Mechanism inspected

Its shrink loop varies one input, reruns the validator and returns a simplified failing schema.

## Limitation that matters

It caps attempts and uses a local greedy pass; the returned example need not be globally minimal or cover cross-field failure interactions.

## Practical check for a trading system

Shrink failing event sequences and retain the original seed and complete trace.

## Why this score

2/5. It shows a concrete reduction loop, with bounded and greedy limits.

## Source trail

[README](https://github.com/msoedov/quick.py/blob/5c89c11c7f6bc1fabbee757a8bb217dea08e359c/Readme.md#L1); [quick/shrink.py](https://github.com/msoedov/quick.py/blob/5c89c11c7f6bc1fabbee757a8bb217dea08e359c/quick/shrink.py#L15); [quick/shrink.py](https://github.com/msoedov/quick.py/blob/5c89c11c7f6bc1fabbee757a8bb217dea08e359c/quick/shrink.py#L37); [quick/shrink.py](https://github.com/msoedov/quick.py/blob/5c89c11c7f6bc1fabbee757a8bb217dea08e359c/quick/shrink.py#L52).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
