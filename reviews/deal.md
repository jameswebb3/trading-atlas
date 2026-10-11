# Deal: check whether contracts are active where they matter

**Decision question:** Could a documented invariant disappear when the production interpreter is configured differently?

| Field | Review |
| --- | --- |
| Upstream | [Deal](https://github.com/life4/deal) |
| Primary area | Testing & Verification |
| Source commit | [751c0a7ebdf8527c8231b15038e4656d2a6a75c6](https://github.com/life4/deal/commit/751c0a7ebdf8527c8231b15038e4656d2a6a75c6) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/life4/deal/blob/751c0a7ebdf8527c8231b15038e4656d2a6a75c6/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Expresses preconditions, postconditions, and side-effect expectations as executable contracts. Useful for making research assumptions inspectable, but runtime enforcement can be disabled; critical order and data checks need a deliberate deployment policy. |

## Mechanism worth inspecting

The [README](https://github.com/life4/deal/blob/751c0a7ebdf8527c8231b15038e4656d2a6a75c6/README.md#L9-L26) describes value, exception, and side-effect contracts. The [runtime guide](https://github.com/life4/deal/blob/751c0a7ebdf8527c8231b15038e4656d2a6a75c6/docs/basic/runtime.md#L7-L36) explains their enable/disable lifecycle. The [state implementation](https://github.com/life4/deal/blob/751c0a7ebdf8527c8231b15038e4656d2a6a75c6/deal/_state.py#L31-L42) resets enforcement from __debug__. The [synchronous wrapper](https://github.com/life4/deal/blob/751c0a7ebdf8527c8231b15038e4656d2a6a75c6/deal/_runtime/_contracts.py#L111-L150) either calls the function directly or runs preconditions, the function, and postconditions. This makes the deployment state part of the contract's meaning.

## Important limit

A decorator in source is not evidence that a check runs in deployment. The [wrapper](https://github.com/life4/deal/blob/751c0a7ebdf8527c8231b15038e4656d2a6a75c6/deal/_runtime/_contracts.py#L111-L119) explicitly bypasses checks when disabled, and [permanent disabling](https://github.com/life4/deal/blob/751c0a7ebdf8527c8231b15038e4656d2a6a75c6/docs/basic/runtime.md#L30-L36) changes decoration behaviour. Contracts only test the declared predicates; they do not supply exchange-specific position, timestamp, or order invariants.

## Questions to take into your own design

- Which invariants must run regardless of interpreter optimisation or test configuration?
- Can deployment checks prove that mandatory validators are active before processing orders or publishing a research result?

## Why this score for a trading system

3/5: a transferable testing pattern with a source-visible enforcement boundary. It does not provide trading semantics, and its configurable runtime checks should not silently become the only money-protecting gate.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
