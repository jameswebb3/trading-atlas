# PonyCheck - Can asynchronous test results be matched to the run that produced them?

**Decision question:** Can asynchronous test results be matched to the run that produced them?

| Field | Review |
| --- | --- |
| Upstream | [ponylang/ponycheck](https://github.com/ponylang/ponycheck) |
| Primary area | Testing & Verification |
| Source commit | [155d145d7641c1ae8f94cc88bc7567058601186e](https://github.com/ponylang/ponycheck/commit/155d145d7641c1ae8f94cc88bc7567058601186e) |
| Reviewed | 2026-10-11 |
| Declared license | BSD-2-Clause |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It tracks expected run numbers and rejects out-of-order completion messages during test and shrink phases. The ordering guard is internal to the runner and does not model partial fills or venue event IDs. |

## What this project does

A property-testing runner for Pony.

## Mechanism inspected

It tracks expected run numbers and rejects out-of-order completion messages during test and shrink phases.

## Limitation that matters

The ordering guard is internal to the runner and does not model partial fills or venue event IDs.

## Practical check for a trading system

Label each asynchronous replay action and assert that ACK and fill callbacks belong to the intended attempt.

## Why this score

2/5. The run-token pattern transfers to stateful tests, though the implementation is language-specific.

## Source trail

[README](https://github.com/ponylang/ponycheck/blob/155d145d7641c1ae8f94cc88bc7567058601186e/README.md#L1); [ponycheck/property_runner.pony](https://github.com/ponylang/ponycheck/blob/155d145d7641c1ae8f94cc88bc7567058601186e/ponycheck/property_runner.pony#L70); [ponycheck/property_runner.pony](https://github.com/ponylang/ponycheck/blob/155d145d7641c1ae8f94cc88bc7567058601186e/ponycheck/property_runner.pony#L91); [Root license](https://github.com/ponylang/ponycheck/blob/155d145d7641c1ae8f94cc88bc7567058601186e/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
