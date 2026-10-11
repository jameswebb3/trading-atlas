# QuantDinger — Can a requested price become a recorded fill price

**Decision question:** Can a requested price become a recorded fill price?

| Field | Review |
| --- | --- |
| Upstream | [QuantDinger](https://github.com/OpenByteInc/QuantDinger) |
| Primary area | Execution & Exchange Integration |
| Source commit | [7da255c1e754daf939e1c58066ca2e44eb701b43](https://github.com/OpenByteInc/QuantDinger/commit/7da255c1e754daf939e1c58066ca2e44eb701b43) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/OpenByteInc/QuantDinger/blob/7da255c1e754daf939e1c58066ca2e44eb701b43/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | A strong reference for fill accounting: requested prices never substitute for observed execution. Regression tests explicitly prevent incomplete fills from updating positions or the ledger. |

## Project overview

A trading platform with explicit separation between order instructions and execution evidence. [Project documentation](https://github.com/OpenByteInc/QuantDinger/blob/7da255c1e754daf939e1c58066ca2e44eb701b43/docs/architecture/API_CONVENTIONS.md).

## Mechanism worth inspecting

The [fill-evidence helper](https://github.com/OpenByteInc/QuantDinger/blob/7da255c1e754daf939e1c58066ca2e44eb701b43/backend_api_python/app/services/live_trading/fill_evidence.py#L7-L28) requires positive finite execution quantities and prices; Binance averages come from execution fields. The [snapshot completion path](https://github.com/OpenByteInc/QuantDinger/blob/7da255c1e754daf939e1c58066ca2e44eb701b43/backend_api_python/app/services/execution_streams/fill_snapshot.py#L57-L94) consults REST when evidence is missing and rejects quantity regression. [Regression tests](https://github.com/OpenByteInc/QuantDinger/blob/7da255c1e754daf939e1c58066ca2e44eb701b43/backend_api_python/tests/test_execution_price_evidence.py#L18-L64) reject missing averages and prevent position or ledger writes.

## Important limit

The inspected paths cover specific venue fields and snapshot rules, not every exchange or fee model. A filled quantity with no execution average remains incomplete evidence.

## Questions to take into your own design

- Can a requested price become a recorded fill price?
- Can incomplete execution averages or regressing cumulative quantities mutate the ledger?

## Why this score for a trading system

4/5: concrete execution safeguards plus regression cases for missing prices, reference-price substitution and ledger mutation.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
