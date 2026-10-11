# Provlake - Can provenance validation disappear in an optimized Python process?

**Decision question:** Can provenance validation disappear in an optimized Python process?

| Field | Review |
| --- | --- |
| Upstream | [IBM/multi-data-lineage-capture-py](https://github.com/IBM/multi-data-lineage-capture-py) |
| Primary area | Data Quality & Lineage |
| Source commit | [bc17b0ecc86bd23eb9e7223d027c612bf31be388](https://github.com/IBM/multi-data-lineage-capture-py/commit/bc17b0ecc86bd23eb9e7223d027c612bf31be388) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The task request object stores input/output type, status, timestamps and arbitrary values. It uses assert for allowed type and status, so Python optimization can remove those validations; many evidence fields remain optional. |

## What this project does

A provenance model for task and workflow records.

## Mechanism inspected

The task request object stores input/output type, status, timestamps and arbitrary values.

## Limitation that matters

It uses assert for allowed type and status, so Python optimization can remove those validations; many evidence fields remain optional.

## Practical check for a trading system

Validate provenance contracts with explicit exceptions and required fields.

## Why this score

2/5. The record shape is useful, but its enforcement is too weak for durable trading evidence.

## Source trail

[README](https://github.com/IBM/multi-data-lineage-capture-py/blob/bc17b0ecc86bd23eb9e7223d027c612bf31be388/README.md#L1); [src/provlake/model/task_prov_obj.py](https://github.com/IBM/multi-data-lineage-capture-py/blob/bc17b0ecc86bd23eb9e7223d027c612bf31be388/src/provlake/model/task_prov_obj.py#L7); [src/provlake/model/task_prov_obj.py](https://github.com/IBM/multi-data-lineage-capture-py/blob/bc17b0ecc86bd23eb9e7223d027c612bf31be388/src/provlake/model/task_prov_obj.py#L38); [Root license](https://github.com/IBM/multi-data-lineage-capture-py/blob/bc17b0ecc86bd23eb9e7223d027c612bf31be388/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
