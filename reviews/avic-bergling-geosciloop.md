# GeoSciLoop: Does a report claim follow from the inspected data and protocol?

**Decision question:** Does a report claim follow from the inspected data and protocol?

| Field | Review |
| --- | --- |
| Upstream | [avic-bergling/geosciloop](https://github.com/avic-bergling/geosciloop) |
| Primary area | Research & Reproducibility |
| Source commit | [dc21498ea02c04fc1512c6a969c79a496172157b](https://github.com/avic-bergling/geosciloop/commit/dc21498ea02c04fc1512c6a969c79a496172157b) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/avic-bergling/geosciloop/blob/dc21498ea02c04fc1512c6a969c79a496172157b/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The evaluator expects benchmark and data manifests. Metadata validators inspect spatial alignment, no-data handling and split strategy. ConclusionSupport flags causal wording without design support and compares claimed association direction with coefficient or correlation sign. A coefficient sign can be noisy, confounded or selected after many tries. Matching it does not validate an effect. The project is a geospatial synthetic demo, not a trading experiment. |

## What this project does

Links reports to source manifests and validation results, including split strategy and claim support. Its claim checker is a text-and-sign heuristic, so passing it is triage rather than statistical proof.

## Mechanism inspected

The evaluator expects benchmark and data manifests. Metadata validators inspect spatial alignment, no-data handling and split strategy. ConclusionSupport flags causal wording without design support and compares claimed association direction with coefficient or correlation sign.

## Limitation that matters

A coefficient sign can be noisy, confounded or selected after many tries. Matching it does not validate an effect. The project is a geospatial synthetic demo, not a trading experiment.

## Practical check for a trading system

Map each claim to immutable data, protocol and result, then check uncertainty, multiplicity and availability independently.

## Why this score

3/5 transferable: claim-to-artifact and split checks improve hygiene, but the support heuristic cannot certify market conclusions.

## Source trail

[README.md](https://github.com/avic-bergling/geosciloop/blob/dc21498ea02c04fc1512c6a969c79a496172157b/README.md#L1); [docs/evaluation.md](https://github.com/avic-bergling/geosciloop/blob/dc21498ea02c04fc1512c6a969c79a496172157b/docs/evaluation.md#L1); [geosciloop/validators/metadata.py](https://github.com/avic-bergling/geosciloop/blob/dc21498ea02c04fc1512c6a969c79a496172157b/geosciloop/validators/metadata.py#L21); [geosciloop/validators/conclusion_support.py](https://github.com/avic-bergling/geosciloop/blob/dc21498ea02c04fc1512c6a969c79a496172157b/geosciloop/validators/conclusion_support.py#L32); [geosciloop/adapters/provenance.py](https://github.com/avic-bergling/geosciloop/blob/dc21498ea02c04fc1512c6a969c79a496172157b/geosciloop/adapters/provenance.py#L36)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
