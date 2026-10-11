# Binance Futures Connector Python — Can request-budget metadata be retained alongside market data

**Decision question:** Can request-budget metadata be retained alongside market data?

| Field | Review |
| --- | --- |
| Upstream | [Binance Futures Connector Python](https://github.com/binance/binance-futures-connector-python) |
| Primary area | Execution & Exchange Integration |
| Source commit | [a6bfbbf10fe2c1b4eb76fc24ffb82eb94bf9df89](https://github.com/binance/binance-futures-connector-python/commit/a6bfbbf10fe2c1b4eb76fc24ffb82eb94bf9df89) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/binance/binance-futures-connector-python/blob/a6bfbbf10fe2c1b4eb76fc24ffb82eb94bf9df89/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Can preserve exchange request-weight and order-count headers beside response data. Useful for collection-budget diagnostics, but this deprecated wrapper should be treated as a historical reference. |

## Project overview

A deprecated connector for Binance USDT-M and coin-margined futures REST and WebSocket interfaces. [Project documentation](https://github.com/binance/binance-futures-connector-python/blob/a6bfbbf10fe2c1b4eb76fc24ffb82eb94bf9df89/README.md#L1-L16).

## Mechanism worth inspecting

The response path optionally collects used-weight and order-count headers and returns them with the payload. The wrapper changes shape when metadata options are enabled. [Response envelope](https://github.com/binance/binance-futures-connector-python/blob/a6bfbbf10fe2c1b4eb76fc24ffb82eb94bf9df89/binance/api.py#L116-L145).

## Important limit

This repository is deprecated in favor of the modular connectors. Header budgets describe the remote request limit, not dataset coverage or collection completeness. [Migration notice](https://github.com/binance/binance-futures-connector-python/blob/a6bfbbf10fe2c1b4eb76fc24ffb82eb94bf9df89/README.md#L1-L5).

## Questions to take into your own design

- Can a collector distinguish quota exhaustion from an empty data interval?
- Does enabling metadata preserve the downstream payload contract?

## Why this score for a trading system

2/5: a practical request-budget pattern, with little reason to adopt a deprecated SDK.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
