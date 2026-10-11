# sanderling - A property test needs coverage gates on its trace

**Decision question:** Did a fuzz run exercise the intended states before being declared clean?

| Field | Review |
| --- | --- |
| Upstream | [priyanshujain/sanderling](https://github.com/priyanshujain/sanderling) |
| Primary area | Testing & Verification |
| Source commit | [9ab59365b2dd73a4b512340b675a906b7821a1fd](https://github.com/priyanshujain/sanderling/commit/9ab59365b2dd73a4b512340b675a906b7821a1fd) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Scores recorded fuzz-run traces against explicit exit, error, state-observation and latency gates using fixed reproducible seeds. The inspected gates are app-specific and cannot prove unvisited order or data states are safe. |

## What this project does

A property-based explorer for mobile and web interfaces. Its conformance script evaluates recorded fuzz-run traces against multiple behavioral and operational gates.

## Mechanism inspected

The script runs fixed seeds and scores five gates across exit status, unexpected error lines, expected initial hierarchy, doubled text after an input action, and step latency or orphan processes. A missing hierarchy is a failure rather than an empty success.

## Limitation that matters

The gates are tailored to a login form and mobile runtime. Passing these five checks does not establish that all important states were reached; only the specified trace conditions are checked. They do not substitute for exchange-order sequence and restart properties. This is a source review, not a runtime or security test.

## Practical check for a trading system

In trading state-machine fuzzing, require evidence that target states and transitions were exercised, not merely zero exceptions. Store the failing seed, action stream and minimized trace for replay.

## Why this score

2/5 because explicit trace coverage gates transfer to trading test design, but the inspected script tests mobile UI behavior rather than trading logic.

## Source trail

[README](https://github.com/priyanshujain/sanderling/blob/9ab59365b2dd73a4b512340b675a906b7821a1fd/README.md#L1); [Conformance gates](https://github.com/priyanshujain/sanderling/blob/9ab59365b2dd73a4b512340b675a906b7821a1fd/conformance/gates.sh#L1); [Missing hierarchy gate](https://github.com/priyanshujain/sanderling/blob/9ab59365b2dd73a4b512340b675a906b7821a1fd/conformance/gates.sh#L133); [Gate aggregation](https://github.com/priyanshujain/sanderling/blob/9ab59365b2dd73a4b512340b675a906b7821a1fd/conformance/gates.sh#L408); [License](https://github.com/priyanshujain/sanderling/blob/9ab59365b2dd73a4b512340b675a906b7821a1fd/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
