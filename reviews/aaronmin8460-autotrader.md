# autotrader - When is an unknown order outcome safe to clear?

**Decision question:** When is an unknown order outcome safe to clear?

| Field | Review |
| --- | --- |
| Upstream | [aaronmin8460/autotrader](https://github.com/aaronmin8460/autotrader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [2695109f7047e261acedcde88b034191035c1d66](https://github.com/aaronmin8460/autotrader/commit/2695109f7047e261acedcde88b034191035c1d66) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | The reconciler rechecks a broker not-found answer and keeps ambiguous UNKNOWN intents blocking until it can resolve them from broker truth. The safety result depends on the broker lookup contract and its eventual consistency; the repository has no verified root license in this review. |

## What this project does

A trading runtime with a read-only broker reconciliation phase.

## Mechanism inspected

The reconciler rechecks a broker not-found answer and keeps ambiguous UNKNOWN intents blocking until it can resolve them from broker truth.

## Limitation that matters

The safety result depends on the broker lookup contract and its eventual consistency; the repository has no verified root license in this review.

## Practical check for a trading system

Never resubmit an UNKNOWN intent or allow fresh entries from a single not-found response.

## Why this score

4/5. The explicit safe-to-trade status prevents an uncertain submission from being treated as failure.

## Source trail

[README](https://github.com/aaronmin8460/autotrader/blob/2695109f7047e261acedcde88b034191035c1d66/README.md#L1); [docs/SPEC.md](https://github.com/aaronmin8460/autotrader/blob/2695109f7047e261acedcde88b034191035c1d66/docs/SPEC.md#L1); [src/autotrader/reconciliation/engine.py](https://github.com/aaronmin8460/autotrader/blob/2695109f7047e261acedcde88b034191035c1d66/src/autotrader/reconciliation/engine.py#L144).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
