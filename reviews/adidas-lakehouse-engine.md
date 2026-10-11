# Lakehouse Engine — Row failures and run failures stay separate

**Decision question:** Can an unflagged row belong to a failed validation run?

| Field | Review |
| --- | --- |
| Upstream | [Lakehouse Engine](https://github.com/adidas/lakehouse-engine) |
| Primary area | Data Quality & Lineage |
| Source commit | [ea0b8f3509666b001faaeabdd26d06e663da6afe](https://github.com/adidas/lakehouse-engine/commit/ea0b8f3509666b001faaeabdd26d06e663da6afe) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/adidas/lakehouse-engine/blob/ea0b8f3509666b001faaeabdd26d06e663da6afe/LICENSE.txt) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The validator joins unexpected-row evidence by the configured source key while carrying run success and raised-exception fields alongside row-level failures. A row without a recorded row failure is not proof that the whole run passed. |

## Project overview

Configuration-driven Spark framework for data loading, quality validation and lakehouse workflows. [Documentation](https://github.com/adidas/lakehouse-engine/blob/ea0b8f3509666b001faaeabdd26d06e663da6afe/README.md).

## Mechanism worth inspecting

The validator joins unexpected-row evidence by the configured source key while carrying run success and raised-exception fields alongside row-level failures. [Source](https://github.com/adidas/lakehouse-engine/blob/ea0b8f3509666b001faaeabdd26d06e663da6afe/lakehouse_engine/dq_processors/validator.py#L72-L109).

## Important limit

A row without a recorded row failure is not proof that the whole run passed. Exceptions and aggregate failures need their own admission policy, and failure joins depend on a suitable source key. [Evidence 1](https://github.com/adidas/lakehouse-engine/blob/ea0b8f3509666b001faaeabdd26d06e663da6afe/lakehouse_engine/dq_processors/validator.py#L72-L109). [Evidence 2](https://github.com/adidas/lakehouse-engine/blob/ea0b8f3509666b001faaeabdd26d06e663da6afe/lakehouse_engine/dq_processors/validator.py#L135-L227).

## Questions to take into your own design

- Can downstream consumers see both row validity and run validity?
- Is a keyless or exception-only failure represented without inventing good rows?

## Why this score for a trading system

A useful separation for evidence-bearing data pipelines; the Spark stack and its deployment assumptions are not needed to apply it.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
