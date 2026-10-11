# Apache Hamilton: validate the graph before the run

**Decision question:** Can a research run expose missing or mismatched inputs before computing a result?

| Field | Review |
| --- | --- |
| Upstream | [apache/hamilton](https://github.com/apache/hamilton) |
| Primary area | Research & Reproducibility |
| Source commit | [661aa88802b9a53d9b1a6feb45b426f44b65ba0b](https://github.com/apache/hamilton/commit/661aa88802b9a53d9b1a6feb45b426f44b65ba0b) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/apache/hamilton/blob/661aa88802b9a53d9b1a6feb45b426f44b65ba0b/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Turns function parameters into a transformation DAG and checks required runtime inputs and their types before execution. A run ID and valid DAG do not identify the exact dataset snapshot; reproducibility needs that identity separately. |

## Mechanism worth inspecting

Hamilton's [README](https://github.com/apache/hamilton/blob/661aa88802b9a53d9b1a6feb45b426f44b65ba0b/README.md#L54-L66) describes a DAG defined by ordinary Python function dependencies. The executor receives requested outputs, overrides, inputs, and a run ID ([interface](https://github.com/apache/hamilton/blob/661aa88802b9a53d9b1a6feb45b426f44b65ba0b/hamilton/driver.py#L91-L112); [default execution](https://github.com/apache/hamilton/blob/661aa88802b9a53d9b1a6feb45b426f44b65ba0b/hamilton/driver.py#L152-L172)). Before execution, [`validate_inputs`](https://github.com/apache/hamilton/blob/661aa88802b9a53d9b1a6feb45b426f44b65ba0b/hamilton/driver.py#L472-L529) rejects missing required inputs and type mismatches. That is a practical preflight for a reproducible transformation graph.

## Important limit

The inspected validation checks graph inputs and types. It does not, by itself, pin the bytes, version, or availability window of a mutable data source. A run manifest must still attach dataset identity and transformation version to the graph result.

## Questions to take into your own design

- Which inputs are required for the requested outputs?
- Does a missing input fail before a result is produced?
- Which dataset version and transform revision produced each output?

## Why this score for a trading system

Preflight input checks and a transformation DAG support reproducible trading research; the graph does not identify input data bytes.

**Scope of this review:** We read the pinned README and driver validation/execution code. We did not run Hamilton, inspect every adapter, or test data-version integrations.
