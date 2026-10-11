# DML - What if a failed numeric conversion becomes a valid-looking empty field?

**Decision question:** What if a failed numeric conversion becomes a valid-looking empty field?

| Field | Review |
| --- | --- |
| Upstream | [voltraco/dml](https://github.com/voltraco/dml) |
| Primary area | Data Quality & Lineage |
| Source commit | [06dae44cb68f28ea17c1fd6bfd3032a722aaf26b](https://github.com/voltraco/dml/commit/06dae44cb68f28ea17c1fd6bfd3032a722aaf26b) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its Number caster parses an integer and returns an empty string when conversion yields NaN. The converted value loses the original malformed input; a downstream schema may mistake blank for missing rather than invalid numeric data. |

## What this project does

A declarative JavaScript data-model validator.

## Mechanism inspected

Its Number caster parses an integer and returns an empty string when conversion yields NaN.

## Limitation that matters

The converted value loses the original malformed input; a downstream schema may mistake blank for missing rather than invalid numeric data.

## Practical check for a trading system

Reject invalid numeric values with the raw field and error reason retained.

## Why this score

2/5. A clear example of lossy coercion at the data boundary.

## Source trail

[README](https://github.com/voltraco/dml/blob/06dae44cb68f28ea17c1fd6bfd3032a722aaf26b/README.md#L1); [validator.js](https://github.com/voltraco/dml/blob/06dae44cb68f28ea17c1fd6bfd3032a722aaf26b/validator.js#L40); [validator.js](https://github.com/voltraco/dml/blob/06dae44cb68f28ea17c1fd6bfd3032a722aaf26b/validator.js#L50); [Root license](https://github.com/voltraco/dml/blob/06dae44cb68f28ea17c1fd6bfd3032a722aaf26b/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
