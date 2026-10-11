# robin_stocks - Retrying with a stable order reference

**Decision question:** If a crypto order POST times out, what identifies a retry as the same intention?

| Field | Review |
| --- | --- |
| Upstream | [jmfernandes/robin_stocks](https://github.com/jmfernandes/robin_stocks) |
| Primary area | Execution & Exchange Integration |
| Source commit | [1b4ef98be36d1df127886889c843256799a1dfea](https://github.com/jmfernandes/robin_stocks/commit/1b4ef98be36d1df127886889c843256799a1dfea) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/jmfernandes/robin_stocks/blob/1b4ef98be36d1df127886889c843256799a1dfea/LICENSE.txt)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The crypto order helper creates one ref_id before posting and sends the same payload for up to three attempts when the call returns None. The comment asserts server-side duplicate protection, but this source does not verify exchange idempotency or reconcile an ambiguous first response; it is not a Hyperliquid adapter. |

## What this project does

robin_stocks wraps Robinhood crypto and stock order endpoints with simple Python order helpers. [README](https://github.com/jmfernandes/robin_stocks/blob/1b4ef98be36d1df127886889c843256799a1dfea/README.rst).

## Mechanism inspected

The crypto order helper creates one ref_id before posting and sends the same payload for up to three attempts when the call returns None. [Implementation](https://github.com/jmfernandes/robin_stocks/blob/1b4ef98be36d1df127886889c843256799a1dfea/robin_stocks/robinhood/orders.py#L1500-L1522).

## Limitation that matters

The comment asserts server-side duplicate protection, but this source does not verify exchange idempotency or reconcile an ambiguous first response; it is not a Hyperliquid adapter. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

For a live adapter, retain a stable client order ID across retries and reconcile by that ID before deciding whether to send again.

## Why this score

The crypto order helper creates one ref_id before posting and sends the same payload for up to three attempts when the call returns None. The comment asserts server-side duplicate protection, but this source does not verify exchange idempotency or reconcile an ambiguous first response; it is not a Hyperliquid adapter.

## Source trail

[README](https://github.com/jmfernandes/robin_stocks/blob/1b4ef98be36d1df127886889c843256799a1dfea/README.rst) - [Implementation](https://github.com/jmfernandes/robin_stocks/blob/1b4ef98be36d1df127886889c843256799a1dfea/robin_stocks/robinhood/orders.py#L1500-L1522) - [License](https://github.com/jmfernandes/robin_stocks/blob/1b4ef98be36d1df127886889c843256799a1dfea/LICENSE.txt).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
