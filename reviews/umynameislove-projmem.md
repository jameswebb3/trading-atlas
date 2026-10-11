# Projmem: Can an experiment recommendation cite evidence that does not exist?

**Decision question:** Can an experiment recommendation cite evidence that does not exist?

| Field | Review |
| --- | --- |
| Upstream | [umynameislove/projmem](https://github.com/umynameislove/projmem) |
| Primary area | Research & Reproducibility |
| Source commit | [d684d7d172792344c4d31f9ec74067a23cc023e3](https://github.com/umynameislove/projmem/commit/d684d7d172792344c4d31f9ec74067a23cc023e3) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/umynameislove/projmem/blob/d684d7d172792344c4d31f9ec74067a23cc023e3/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The evidence linker rejects duplicate or missing graph node IDs, type mismatches and provenance absent from SQLite; related failures must be observed in a run. The avoid generator groups failures by config feature and suppresses the candidate when a strong successful counterexample is present. Confidence is a function of evidence count and the candidate logic is observational; many correlated runs from a sweep do not constitute independent causal support. Metadata links establish existence and type, not validity of the metric, time split or strategy conclusion. |

## What this project does

Generates local recommendation candidates from run and failure metadata, links supporting and opposing evidence to graph nodes and SQLite rows, and suppresses broad avoid claims when strong successful counterexamples exist. It does not prove causality.

## Mechanism inspected

The evidence linker rejects duplicate or missing graph node IDs, type mismatches and provenance absent from SQLite; related failures must be observed in a run. The avoid generator groups failures by config feature and suppresses the candidate when a strong successful counterexample is present.

## Limitation that matters

Confidence is a function of evidence count and the candidate logic is observational; many correlated runs from a sweep do not constitute independent causal support. Metadata links establish existence and type, not validity of the metric, time split or strategy conclusion.

## Practical check for a trading system

For any automatically surfaced research pattern, resolve each supporting and opposing item to an immutable run, protocol and data cut. Add multiple-testing and independent-cell controls before treating a pattern as actionable.

## Why this score

3/5 transferable: source-verified support/opposition is a useful discipline for research memory, but the house already has a ledger and the count-based confidence should not be copied.

## Source trail

[README.md](https://github.com/umynameislove/projmem/blob/d684d7d172792344c4d31f9ec74067a23cc023e3/README.md#L10); [src/pmem/recommendations/evidence.py](https://github.com/umynameislove/projmem/blob/d684d7d172792344c4d31f9ec74067a23cc023e3/src/pmem/recommendations/evidence.py#L119); [src/pmem/recommendations/evidence.py](https://github.com/umynameislove/projmem/blob/d684d7d172792344c4d31f9ec74067a23cc023e3/src/pmem/recommendations/evidence.py#L162); [src/pmem/recommendations/generator.py](https://github.com/umynameislove/projmem/blob/d684d7d172792344c4d31f9ec74067a23cc023e3/src/pmem/recommendations/generator.py#L304); [src/pmem/recommendations/generator.py](https://github.com/umynameislove/projmem/blob/d684d7d172792344c4d31f9ec74067a23cc023e3/src/pmem/recommendations/generator.py#L667)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
