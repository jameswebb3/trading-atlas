# Amazon Deequ Glue Sample — Started is not completed

**Decision question:** Does launching a crawler prove that quality checks ran?

| Field | Review |
| --- | --- |
| Upstream | [aws-samples/amazon-deequ-glue](https://github.com/aws-samples/amazon-deequ-glue) |
| Primary area | Data Quality & Lineage |
| Source commit | [bd171732b446cb466a79d4683e71959023730a0c](https://github.com/aws-samples/amazon-deequ-glue/commit/bd171732b446cb466a79d4683e71959023730a0c) |
| Reviewed | 2026-10-10 |
| Declared license | Amazon permissive license text ([source](https://github.com/aws-samples/amazon-deequ-glue/blob/bd171732b446cb466a79d4683e71959023730a0c/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The inspected Lambda starts a Glue crawler and returns 200 immediately, also treating an already-running crawler as nonfatal. That return value confirms launch or preexisting activity, not crawler completion or a passing data-quality result. |

## What this project does

An AWS sample combining Glue crawling and Deequ-style data-quality processing. [Project README](https://github.com/aws-samples/amazon-deequ-glue/blob/bd171732b446cb466a79d4683e71959023730a0c/README.md#L1).

## Mechanism inspected

The inspected Lambda starts a Glue crawler and returns 200 immediately, also treating an already-running crawler as nonfatal. [Implementation](https://github.com/aws-samples/amazon-deequ-glue/blob/bd171732b446cb466a79d4683e71959023730a0c/src/main/utils/crawl-data/src/lambda_function.py#L24-L34).

## Limitation that matters

That return value confirms launch or preexisting activity, not crawler completion or a passing data-quality result. This is a source review, not a runtime or security test.

## Practical check for a trading system

Require terminal crawler status and validation artifacts before promoting a dataset to research use.

## Why this score

A small but concrete asynchronous-completion warning; the AWS sample stack is not needed for the pattern.

## Source trail

[README](https://github.com/aws-samples/amazon-deequ-glue/blob/bd171732b446cb466a79d4683e71959023730a0c/README.md#L1); [Implementation](https://github.com/aws-samples/amazon-deequ-glue/blob/bd171732b446cb466a79d4683e71959023730a0c/src/main/utils/crawl-data/src/lambda_function.py#L24-L34) - [License](https://github.com/aws-samples/amazon-deequ-glue/blob/bd171732b446cb466a79d4683e71959023730a0c/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
