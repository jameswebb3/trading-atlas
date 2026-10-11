# TestGen: learn refresh cadence only after enough completed intervals

**Decision question:** Can freshness monitoring distinguish an irregular refresh schedule from an actual delay?

| Field | Review |
| --- | --- |
| Upstream | [DataOps TestGen](https://github.com/DataKitchen/dataops-testgen) |
| Primary area | Data Quality & Lineage |
| Source commit | [98acd8ad37314abeacda65d7f10cf61b997f5c3a](https://github.com/DataKitchen/dataops-testgen/commit/98acd8ad37314abeacda65d7f10cf61b997f5c3a) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/DataKitchen/dataops-testgen/blob/98acd8ad37314abeacda65d7f10cf61b997f5c3a/LICENSE) |
| Review depth | 3/3: README, configuration, freshness source and selected unit tests read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Generates data-quality tests from profiles and tracks refresh behavior. Its freshness estimator requires completed update gaps, uses a bounded recent history, and applies schedule exclusions only after an inferred schedule becomes active. |

## Project overview

A data-quality platform profiles datasets, generates checks, and monitors subsequent refreshes and anomalies. [Project documentation](https://github.com/DataKitchen/dataops-testgen/blob/98acd8ad37314abeacda65d7f10cf61b997f5c3a/README.md#L4-L26).

## Mechanism worth inspecting

The [freshness contract](https://github.com/DataKitchen/dataops-testgen/blob/98acd8ad37314abeacda65d7f10cf61b997f5c3a/testgen/common/freshness_service.py#L16-L37) separates threshold values from schedule stages. [Gap estimation](https://github.com/DataKitchen/dataops-testgen/blob/98acd8ad37314abeacda65d7f10cf61b997f5c3a/testgen/common/freshness_service.py#L76-L112) requires five completed gaps and retains at most forty, with explicit calendar exclusions and a maximum-gap floor. [Schedule gating](https://github.com/DataKitchen/dataops-testgen/blob/98acd8ad37314abeacda65d7f10cf61b997f5c3a/testgen/common/freshness_service.py#L125-L144) applies learned exclusions only when the schedule is active. The [window test](https://github.com/DataKitchen/dataops-testgen/blob/98acd8ad37314abeacda65d7f10cf61b997f5c3a/tests/unit/common/test_freshness_service.py#L61-L79) checks that an old outlier ages out.

## Important limit

The estimator learns observed cadence, including poor cadence. Its upper bound includes the largest retained gap, so persistent degradation can loosen the monitor. Calendar exclusions require the dataset's actual schedule; continuously traded markets should not inherit weekday assumptions. Configuration and profiling do not establish missing-row completeness.

## Questions to take into your own design

- Does an adaptive alert sit beside a fixed contractual maximum data age?
- Are training, tentative, active, and irregular schedule states visible to consumers?

## Why this score for a trading system

3/5: specific reusable cadence estimation and insufficient-history handling, supported by test source. It remains a generic data monitor requiring market-specific limits.

**Scope of this review:** README, configuration documentation, freshness estimator and schedule gating, and selected window tests; no generated tests executed.
