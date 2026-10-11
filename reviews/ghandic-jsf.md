# jsf - Generate schema-shaped inputs, then validate them

**Decision question:** How can contract tests avoid a handful of hand-written happy-path fixtures?

| Field | Review |
| --- | --- |
| Upstream | [ghandic/jsf](https://github.com/ghandic/jsf) |
| Primary area | Testing & Verification |
| Source commit | [39729926bd5be3354c00d6da4acaa4d89dc4c78c](https://github.com/ghandic/jsf/commit/39729926bd5be3354c00d6da4acaa4d89dc4c78c) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/ghandic/jsf/blob/39729926bd5be3354c00d6da4acaa4d89dc4c78c/jsf/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The parser expands local or external references and a generate_and_validate path checks a generated instance against its source schema. Passing the schema proves shape, not valid market time, exchange sequence, or causal availability; external references also need controlled resolution. |

## What this project does

jsf parses JSON Schema definitions and generates sample JSON objects. [README](https://github.com/ghandic/jsf/blob/39729926bd5be3354c00d6da4acaa4d89dc4c78c/jsf/README.md).

## Mechanism inspected

The parser expands local or external references and a generate_and_validate path checks a generated instance against its source schema. [Implementation](https://github.com/ghandic/jsf/blob/39729926bd5be3354c00d6da4acaa4d89dc4c78c/jsf/parser.py#L296-L366).

## Limitation that matters

Passing the schema proves shape, not valid market time, exchange sequence, or causal availability; external references also need controlled resolution. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

Generate shape-valid and intentionally broken market-event fixtures, then assert domain invariants and fail-closed behavior separately.

## Why this score

The parser expands local or external references and a generate_and_validate path checks a generated instance against its source schema. Passing the schema proves shape, not valid market time, exchange sequence, or causal availability; external references also need controlled resolution.

## Source trail

[README](https://github.com/ghandic/jsf/blob/39729926bd5be3354c00d6da4acaa4d89dc4c78c/jsf/README.md) - [Implementation](https://github.com/ghandic/jsf/blob/39729926bd5be3354c00d6da4acaa4d89dc4c78c/jsf/parser.py#L296-L366) - [License](https://github.com/ghandic/jsf/blob/39729926bd5be3354c00d6da4acaa4d89dc4c78c/jsf/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
