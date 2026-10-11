# Alpha Forge: keep prediction labels out of daily PnL accounting

**Decision question:** Can a multi-day prediction target accidentally become a daily realized return?

| Field | Review |
| --- | --- |
| Upstream | [Alpha Forge](https://github.com/Liu-Ming-Yu/alpha-forge) |
| Primary area | Research & Reproducibility |
| Source commit | [922d8d3443afb1518428ed9360318efd934e3c33](https://github.com/Liu-Ming-Yu/alpha-forge/commit/922d8d3443afb1518428ed9360318efd934e3c33) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/Liu-Ming-Yu/alpha-forge/blob/922d8d3443afb1518428ed9360318efd934e3c33/LICENSE) |
| Review depth | 3/3: documentation, accounting source, and regression test read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Documents and tests a correction that separates multi-day training labels from one-day portfolio returns. The design also versions the evidence semantics, so corrected accounting can be distinguished from historical artifacts with different meanings. |

## Project overview

A quantitative research platform combines model campaigns, evidence artifacts, and trading components. [Project documentation](https://github.com/Liu-Ming-Yu/alpha-forge/blob/922d8d3443afb1518428ed9360318efd934e3c33/README.md#L94-L120).

## Mechanism worth inspecting

The [return-accounting ADR](https://github.com/Liu-Ming-Yu/alpha-forge/blob/922d8d3443afb1518428ed9360318efd934e3c33/docs/architecture/adr-003-return-accounting-separation.md#L8-L68) separates label returns, daily realized returns, and horizon-aware purge boundaries. The [new daily accounting path](https://github.com/Liu-Ming-Yu/alpha-forge/blob/922d8d3443afb1518428ed9360318efd934e3c33/src/quant_platform/services/research_service/campaigns/metrics/ranker_metrics.py#L164-L223) marks held weights against daily returns. A [regression fixture](https://github.com/Liu-Ming-Yu/alpha-forge/blob/922d8d3443afb1518428ed9360318efd934e3c33/tests/unit/research_service/campaigns/test_return_accounting_fix.py#L102-L137) uses deliberately different label and realized values.

## Important limit

The [legacy branch](https://github.com/Liu-Ming-Yu/alpha-forge/blob/922d8d3443afb1518428ed9360318efd934e3c33/src/quant_platform/services/research_service/campaigns/metrics/ranker_metrics.py#L140-L163) still compounds forward labels when realized returns are absent. The [new path](https://github.com/Liu-Ming-Yu/alpha-forge/blob/922d8d3443afb1518428ed9360318efd934e3c33/src/quant_platform/services/research_service/campaigns/metrics/ranker_metrics.py#L182-L190) also substitutes zero for missing daily returns. These are material reasons to audit the path selected by each report.

## Questions to take into your own design

- Are training targets and accounting returns separate typed fields?
- Does a report fail explicitly when daily accounting evidence is absent?

## Why this score for a trading system

3/5: a directly relevant correction backed by a readable regression fixture; retained legacy semantics and zero substitution prevent a stronger score.

**Scope of this review:** README, accounting ADR, ranker metrics, and regression tests read; reported performance not replicated.
