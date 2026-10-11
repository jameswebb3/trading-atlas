# Keep future-shifted labels out of the tradable feature graph

**Decision question:** Can an indicator intended for model training enter a causal backtest?

| Field | Review |
| --- | --- |
| Upstream | [Hikyuu](https://github.com/fasiondog/hikyuu) |
| Primary area | Signals & Models |
| Source commit | [5a1dedbd6934c48278cd23bb36fc838da8e67439](https://github.com/fasiondog/hikyuu/commit/5a1dedbd6934c48278cd23bb36fc838da8e67439) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/fasiondog/hikyuu/blob/5a1dedbd6934c48278cd23bb36fc838da8e67439/LICENSE) |
| Review depth | 3/3: documentation, relevant source, and focused tests read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Hikyuu explicitly marks REFX as unsafe for backtesting and permits negative shifts that move future values into earlier rows. Its tests demonstrate that behavior. This is a useful feature-versus-label boundary: support for an operation does not make it eligible for a live signal. |

## Mechanism worth inspecting

The [README](https://github.com/fasiondog/hikyuu/blob/5a1dedbd6934c48278cd23bb36fc838da8e67439/readme.md#L26-L33) describes a research-oriented framework. The [REFX API note](https://github.com/fasiondog/hikyuu/blob/5a1dedbd6934c48278cd23bb36fc838da8e67439/hikyuu_cpp/hikyuu/indicator/crt/REFX.h#L14-L20) excludes it from backtests. The [implementation](https://github.com/fasiondog/hikyuu/blob/5a1dedbd6934c48278cd23bb36fc838da8e67439/hikyuu_cpp/hikyuu/indicator/imp/IRefX.cpp#L45-L64) handles negative shifts; the [tests](https://github.com/fasiondog/hikyuu/blob/5a1dedbd6934c48278cd23bb36fc838da8e67439/hikyuu_cpp/unit_test/hikyuu/indicator/test_REFX.cpp#L58-L74) expect future values shifted to earlier indices.

## Important limit

Future data is legitimate in target construction after the evaluation horizon ends. The inspected operator is intentionally unsafe; the missing application-level question is whether a pipeline separates labels from eligible decision inputs.

## Questions to take into your own design

- Does the feature registry distinguish backward-looking transforms from future-reading target builders?
- Can a target-only operator be rejected before the backtest starts?

## Why this score for a trading system

3/5: The explicit unsafe operator and fixtures are useful references for preventing target construction from leaking into trading features.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
