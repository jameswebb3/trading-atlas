# Review methodology

## Purpose

The Atlas helps a builder decide which public repositories are worth inspecting for a specific problem in a data-driven trading system. Stars score **the practical trading-system value of the inspected mechanism**, not the entire repository, general software quality, GitHub popularity, expected returns, or readiness for live trading.

## Publication gate

A project receives a **rated review** only after we read its README or primary documentation, inspect relevant implementation code at a full commit SHA, write an original mechanism-and-limitation assessment, record the declared license, and check the public review for unsupported claims. A source review is not a runtime test, security audit, or replication of reported performance. We do not install or execute upstream code.

The separate [project ledger](PROJECTS.md) lists every repository encountered in the search, including code readings without a published assessment, documentation screens, scope screens and unresolved sources. These records carry **no trading-system rating** and are not recommendations. A public code link, when present, identifies a path consulted; it is not a substitute for a completed review. The discovery lens and area assignment aid browsing and do not certify the repository as a good fit. Historical GitHub star counts are discovery snapshots, not current popularity or quality scores. Suggestions may be submitted through [Contributing](CONTRIBUTING.md).

## Trading-system rating

First classify the inspected mechanism by its connection to trading:

| Fit | Meaning | Maximum score |
| --- | --- | ---: |
| **Direct** | The source addresses market data, causal signals, backtesting, order execution, portfolio accounting, or a trading-specific failure. | 5/5 |
| **Transferable** | A concrete engineering pattern can be adapted to trading research or operations, but the inspected path is not trading-specific. | 3/5 |
| **Adjacent** | The source is a useful caution or background reference with an indirect link to trading decisions. | 2/5 |

Then score the strength and limits of the evidence within that fit:

| Score | Editorial meaning |
| --- | --- |
| 1/5 | Little actionable value for a trading system or a critical path remains unclear. |
| 2/5 | An adjacent idea, narrow pattern, or cautionary example. Strong general software can still land here. |
| 3/5 | A useful trading mechanism with material limits, or a strong pattern that needs trading-specific adaptation. |
| 4/5 | A directly relevant trading mechanism, visible in code, with consequential boundaries explained. |
| 5/5 | Exceptional direct value supported across the relevant implementation and tests or an independent behavioral check. |

The rating is tied to the review's decision question and inspected commit. It is not a head-to-head ranking of every capability in competing products. A general engineering tool can be excellent at its own task while scoring lower here because its mechanism needs trading-specific adaptation. An excellent LLM evaluation library does not earn 4/5 here merely because its agent-evaluation design is good. A narrow exchange-state guard can score higher if it addresses a costly trading failure. Each full review gives its own trading-system reason; license and unverified behavior remain visible rather than being hidden in the stars.

## Evidence depth

| Depth | Material inspected |
| --- | --- |
| 2/3 | Documentation and relevant implementation code at a pinned commit. Required for publication. |
| 3/3 | Level 2 plus relevant test code or an independently specified behavioral check. |

Reading test code is not running it. We distinguish a documented claim, a behavior visible in source, and an inference from the source. Where an external project reports returns, we do not treat them as replicated.

## Practical assessment

The index summarizes a useful mechanism and its main condition, limitation, or unverified path. It does not turn an uninspected path into an alleged defect. Review questions depend on the claim: a market-data project needs timing and completeness checks; an order adapter needs request, acknowledgement, fill, and cancellation semantics; a strategy project needs causal inputs and honest result evaluation. A pure exchange SDK need not supply alpha.

## Honorable mentions

An area with at least eight completed reviews may highlight at most three. Each mention states what the project does and the practical capability that makes it worth inspecting. These affirmative descriptions use documented capabilities and source-backed findings, with the project overview linked in the full review. Selection favors distinct uses within the area. Every mention also appears in the full reviewed list. The homepage shows these editorial selections; category pages retain every reviewed project, sorted by rating and then alphabetically within equal ratings. A mention is chosen for a distinct use, not necessarily the highest score.

## Freshness and correction

Each review records its date and upstream commit. A later release can change its conclusion. Corrections identify the affected claim and new source. Public reviews use original prose and links to upstream files; they contain no private trading data, credentials, or unpublished strategies.

## Homepage findings and corrections

Recent findings summarize observations already supported by a published review; they do not claim a newly discovered vulnerability or defect. A correction must identify the previous claim, the revised conclusion and the public source supporting the change, with an entry in the change log. Reading more projects is an addition, not a correction. Highlight dates describe editorial updates, not certification of current upstream behavior.
