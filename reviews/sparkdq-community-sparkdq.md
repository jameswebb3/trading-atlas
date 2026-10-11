# SparkDQ — A fresh maximum can hide stale partitions

**Decision question:** Does one recent timestamp establish that the whole feed is fresh?

| Field | Review |
| --- | --- |
| Upstream | [SparkDQ](https://github.com/sparkdq-community/sparkdq) |
| Primary area | Data Quality & Lineage |
| Source commit | [27265a62171fd54b9c01663eee8982942f5bfc28](https://github.com/sparkdq-community/sparkdq/commit/27265a62171fd54b9c01663eee8982942f5bfc28) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/sparkdq-community/sparkdq/blob/27265a62171fd54b9c01663eee8982942f5bfc28/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation, and relevant test code read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The freshness check takes the maximum timestamp and compares it with a lower age threshold. This aggregate does not require every instrument to be fresh and does not impose an upper bound on future timestamps. |

## Project overview

Declarative row-level and aggregate data-quality checks for PySpark. [Documentation](https://github.com/sparkdq-community/sparkdq/blob/27265a62171fd54b9c01663eee8982942f5bfc28/README.md).

## Mechanism worth inspecting

The freshness check takes the maximum timestamp and compares it with a lower age threshold. Tests cover recent, stale and null-only inputs. [Source](https://github.com/sparkdq-community/sparkdq/blob/27265a62171fd54b9c01663eee8982942f5bfc28/sparkdq/checks/aggregate/freshness_checks/freshness_check.py#L28-L95).

## Important limit

This aggregate does not require every instrument to be fresh and does not impose an upper bound on future timestamps. The review concerns this check, not every validation in SparkDQ. [Evidence 1](https://github.com/sparkdq-community/sparkdq/blob/27265a62171fd54b9c01663eee8982942f5bfc28/sparkdq/checks/aggregate/freshness_checks/freshness_check.py#L28-L95). [Evidence 2](https://github.com/sparkdq-community/sparkdq/blob/27265a62171fd54b9c01663eee8982942f5bfc28/tests/unit/checks/aggregate/freshness/test_freshness_check.py#L14-L108).

## Questions to take into your own design

- Is freshness checked per required instrument and source?
- Are future timestamps rejected separately from excessive age?

## Why this score for a trading system

A highly applicable data-quality boundary with focused tests, but a passing global maximum is weaker than trading-universe coverage.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. Relevant tests were read, not executed.
