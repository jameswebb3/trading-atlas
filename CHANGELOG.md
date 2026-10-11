## 2026-10-11 — Fixed queue closed and publication wording audited

- Completed the frozen candidate queue after the first source-audit batch: 34 further full reviews and 411 documented exclusions. The current ledger has 1,066 completed reviews, 478 unrated records and no pending fixed-queue candidates among 1,544 projects considered.
- Corrected deliverator's recorded evidence depth from 2/3 to 3/3 after reading its pinned tests for degraded sub-dex order and position reads. Its 5/5 score and limitation on unverified live behavior remain; upstream tests were not run.
- Changed "examined" to "considered" where the broad ledger includes initial scope screens. The rated pages still count only completed source-backed reviews.
- Moved pzqpzq/Principia from a rated review to an unresolved ledger record because both its GitHub repository API and pinned implementation URL returned 404 on 2026-10-11. It can be reconsidered if the pinned source becomes publicly accessible again.

## 2026-10-11 — First fixed-queue source audit

- Read 20 queued projects at current source commits. Published five new mechanism-specific reviews; 14 were source-screened out with cited reasons, and one repository returned 404 and remains unrated.
- The complete review catalog now has 1,033 projects; the tracked ledger remains at 1,544. The fixed in-scope queue falls from 465 to 445.
- This tranche found a position-list parsing error in a copy bot, a supposed pairs strategy with one observed and traded leg, a trade-alert feed without gap recovery, and explicit truncation/coverage metadata in an agent data connector. No upstream code was installed or run.

## 2026-10-11 — 50 more source-backed trading reviews

- Published 50 new commit-pinned reviews from newly discovered projects. The rated catalog grows from 978 to 1,028; the wider project ledger grows from 1,494 to 1,544. The same ten areas remain.
- The strongest new source findings concern incomplete Hyperliquid reconciliation, strict sequence replay, private-stream fill channel naming, and state mutation before an illegal order transition. Low scores flag paper fills at mid, silent numeric fallbacks, hosted-data opacity and adjacent product scope.
- Reviews are source reading only. No upstream project was installed or run; no returns were measured.

## 2026-10-11 — 50 additional source-backed reviews

- Published 50 new commit-pinned reviews: 31 projects promoted from existing source pointers and 19 newly discovered projects. The rated catalog grows from 928 to 978; the broader project ledger grows from 1,475 to 1,494. One duplicate, ordersim, was removed from the selection because it already had a review.
- The batch covers execution uncertainty, replay fill assumptions, on-chain reorg bounds, point-in-time features, data-quality instrumentation, and thin hosted-data wrappers. Scores include low-rated negative patterns; a review is not an endorsement.
- Upstream README and relevant source were read only. No upstream code was installed or run, and no returns were measured.

## 2026-10-11 — 50 further code-backed reviews

- Published 50 pinned reviews after reading README and relevant implementation: 38 previously unreviewed source pointers and 12 newly discovered projects. The rated catalog grows from 878 to 928; the broader ledger grows from 1,463 to 1,475. Clone bot examples and a source-available project with a noncommercial-only license were screened out rather than described as open source.
- Findings cover interval-overlap purging, WebSocket sequence and backpressure behavior, a depth recorder that applies a delta after detecting a gap, agent evidence truncation, cumulative file hashes, and failed data-quality hooks that do not alter check status. Scores reflect trading usefulness, including low-rated negative examples.
- Upstream projects were read only. No upstream software was installed or run; no alpha or claimed return was measured.

## 2026-10-11 — 50 more source-backed reviews

- Published 50 commit-pinned reviews from the existing discovery ledger after reading each README and relevant implementation. The rated catalog grows from 828 to 878; the broader project ledger remains at 1,463. Forty-seven source pointers and three documentation screens now have full reviews.
- Findings include a queue-position reset in a LOB simulator, a Hyperliquid IOC result-handling failure path, explicit point-in-time query switches, gap-prone collector inserts, agent-evaluation provenance limits, and negative examples from generic observability tools. Scores follow trading-system relevance, including low scores for weak or distant implementations.
- Upstream projects were read only. No upstream software was installed or run; no trading alpha or reported return was measured.

## 2026-10-11 — visual homepage and guide refresh

- Merged the visual homepage into main with its banner, area chart, problem navigation and category cards, now generated from the 828 completed reviews and 1,463 project records.
- Updated the order-completion and on-chain data guides with recent source readings; clarified that the rated area pages and the broader discovery ledger have different publication gates. Corrected the banner wording for 4/5-or-higher reviews. No scores or upstream source assessments changed.

## 2026-10-11 — 30 newly discovered code-backed reviews

- Published 30 new commit-pinned assessments after screening 66 previously untracked repositories and reading implementation in 34. The rated catalog grows 798 to 828; the discovery ledger grows 1,397 to 1,463. Four code-read projects did not meet the editorial bar and remain unscored.
- Findings cover order retry identity, hedge reconciliation, feed invalidation, missing-block repair, a premature completion checkpoint, and backtests that cannot support their advertised result. The upstream projects were read only; no code was installed or executed.

## 2026-10-11 — thirty additional code-backed reviews

- Published 30 commit-pinned reviews across replay, execution, market data, risk and research verification. The rated catalog grows from 768 to 798; the project ledger grows from 1,367 to 1,397.
- New findings cover an optimistic maker-fill fallback, a cancel/fill race, missing-funding behavior and bounded gap repair. Several reviews deliberately score weak or incomplete implementations low. An editorial correction replaced three previously screened generic projects with source-backed trading projects; those screens remain unscored in the ledger. No upstream software was installed or run, and reported returns were not replicated.

## 2026-10-11 — seven additional mechanism reviews

- Published seven more commit-pinned reviews covering tape integrity, fast-kernel equivalence, maker fill assumptions, forward latency sensitivity, book resync, queue simulation and kill-switch evidence. The rated catalog grows from 761 to 768; the project ledger grows from 1,360 to 1,367.
- Public GitHub sources were read as data only; no upstream code or tests were run. The reviews do not certify returns or live safety.

## 2026-10-11 — thirteen source-backed trading reviews

- Published 13 commit-pinned reviews on trading replay, book capture, queue fills, order state, and agent risk gates. The rated catalog grows from 748 to 761; the project ledger grows from 1,345 to 1,360, including two source-read projects that did not pass the editorial gate.
- No upstream software was installed or run. Scores describe the inspected mechanism, including adverse findings; they do not certify returns or live execution.

## 2026-10-10 — four additional trading research reviews

- Published four full reviews for OptionChainAnalytics, StochVolModels, the Kalshi Bitcoin ML trading system, and vgi-kalshi, growing the catalog from 744 to 748 and the project ledger from 1,341 to 1,345. They cover point-in-time chain choice, numerical calibration acceptance, live-fill repricing and the moving live/archive boundary.
- Source files are pinned to exact commits. No upstream code or tests were run, and third-party performance claims were not independently replicated.

## 2026-10-10 — three trading-data and ledger reviews

- Published three source-backed reviews of Hyperliquid archive completeness, CoinJoin evaluation under partial labels, and settlement-aware fill-day accounting. The catalog grows from 741 to 744.
- These repositories were already present in the discovery ledger; the new work is a full public assessment at pinned commits. No upstream software was installed or run.

## 2026-10-10 — four further source reviews

- Published four additional commit-pinned reviews after the 19-review batch, bringing the catalog from 737 to 741. They cover partial-fill cancellation status, bulk-cancel result accounting, row-level schema provenance, and incident-event dispatch evidence.
- Each conclusion is limited to the cited implementation. No upstream software was installed or run.

## 2026-10-10 — 19 additional source reviews

- Added 19 commit-pinned reviews after inspecting relevant README and implementation; the catalog grows from 718 to 737. The new reviews include code-backed checks of webhook idempotency, buffered acknowledgements, multi-region health transitions, order cancellation, statistical resampling and agent-evaluation failure paths.
- The wider 300-review request remains in progress. Screened candidates without a publishable mechanism remain outside the full-review count. No upstream software was installed or run.

# What changed

## 2026-10-10 - seven direct trading-system reviews

- Added seven new commit-pinned reviews, raising the completed catalog from **711 to 718** and the tracked inventory from **1,334 to 1,341**. The homepage layout and ten-area navigation are unchanged.
- New direct references include CleoLOB's data-capability gate, ordersim's replay-equivalence comparison, QuantReplay's market-state failure path, TickForge's rejected-event accounting, a Hyperliquid raw-frame spool, retrospective L4 timestamp provenance, and Kalshi print-fill upper bounds.
- Rechecked the pinned source files of 300 previously screened candidates. They remain unscored: prior editorial notes had already ruled all 300 out as duplicate, too generic, or insufficiently tied to trading decisions. A source pointer is not a completed review. The seven published projects came from fresh discovery and full source reading.
- No upstream code was installed or executed. Source-visible tests were read in four of the new reviews; their behavior was not independently run. Missing or conditional license information is stated in the affected reviews.

## 2026-10-10 - 81 more complete source reviews

- Published 81 additional commit-pinned reviews, bringing the Atlas from **630 to 711**. Each new page identifies an inspected mechanism, a concrete limitation, its trading-system relevance, and source links. The homepage and all ten area inventories retain their existing layout.
- New findings include order/fill reconciliation in hyperopen, a risk-check failure path in perp-cli, and a lineage parser failure that can masquerade as an empty result. No upstream code was installed or executed.
- Corrected the broader ledger's evidence labels: **711 completed reviews, 17 substantial source notes, 355 pinned source pointers, 200 documentation screens, 46 scope screens, and five unresolved sources**. A pointer does not receive a rating or count as a completed review.
- The remaining pointers and screens stay visible in the project ledger. The published review count will grow only when each candidate receives its own code-backed analysis.

## 2026-10-10 - complete research ledger

- Added a browsable record for all 1,334 repositories encountered in the expedition. The 630 completed reviews retain ratings and full analyses; 71 substantial source notes and 382 source pointers, 200 documentation screens, 46 scope screens, and five unresolved sources are marked separately without ratings.
- The ten curated review areas and their scores are unchanged. Historic star counts and discovery lenses in the broader ledger are labelled as such. No private research notes or operational details were exported.


## 2026-10-10 - pending candidate queue closed

- Finished the accessible pending candidate queue: eight new source-backed reviews are published; documentation-only screens remain in the private research log. Four GitHub paths returned 404 and remain unresolved.
- New reviews cover event alignment, source-bound evidence, column lineage, target leakage, agent proof, and workflow test coverage.
- No upstream project was installed or run; no strategy return was measured.

## 2026-10-10 - fifth pending-queue source review

- Read README and implementation at pinned commits for 50 more candidates; screened 25 more by scope. Five candidates remain pending, including Deep Lake whose claimed version/replay mechanism was not established in the inspected public source.
- Twelve reviews passed the publication gate; the catalog grows from 610 to 622. Findings cover input preflight, exact retry identity, attempt-aware outcomes, agent-evaluation denominators, run reconciliation, and capture completeness.
- No upstream code was installed or run; no strategy returns were measured.

## 2026-10-10 - fourth pending-queue source review

- Read README and implementation at pinned commits for 50 more candidates; screened 30 more by scope. Two candidates remain pending because the public source was inaccessible or insufficient to verify the claimed mechanism.
- Ten reviews passed the publication gate; the catalog grows from 600 to 610. Findings cover partial-seed evaluation, source snapshots, conflicting lineage labels, source progress, collector configuration handover, and redaction failure.
- No upstream code was installed or run; no strategy returns were measured.

## 2026-10-10 - third pending-queue source review

- Read README and relevant code at pinned commits for 53 additional candidates; screened 14 more by scope. Two candidates remain pending, including one whose public tree did not establish the claimed mechanism.
- Ten reviews passed the publication gate; the catalog grows from 590 to 600. Findings include explicit loss counts, incomplete-lineage states, replay snapshots, HA recovery fencing, and schema-gated ingestion.
- No upstream code was installed or run, and no strategy returns were measured.

## 2026-10-10 - second pending-queue source review

- Inspected 67 pending candidates: 57 README-plus-code readings and ten screens without a relevant implementation. Fourteen reviews passed the publication gate; the catalog grows from 576 to 590.
- New findings cover bounded held-out access, multi-mode agent evaluation, durable stream acknowledgements, rejected-input reasons, and trading API documentation drift.
- No upstream code was installed, run or adopted. No strategy returns were measured.

## 2026-10-10 - pending-queue source review

- Inspected 57 pending candidates: 51 README-plus-code readings and six screens without pertinent implementation. Eleven source-backed reviews passed the editorial filter; the catalog grows from 565 to 576.
- New findings cover failed inputs absent from a catalog, ambiguous agent-trace replay, structural data checks, explicit epoch units, and synthetic write/read verification.
- No upstream software was installed, run or adopted; no strategy returns were measured.

## 2026-10-09 — second source-review batch

- Reviewed 209 pending candidates: 201 code-backed readings and eight preliminary screens. Fifty-three passed the public editorial filter; the catalog grows from 512 to 565 pinned reviews.
- New findings cover Hyperliquid universe/context cardinality, agent search under matched budgets, UNKNOWN for missing metrics, and uncertain order-side effects.
- No upstream software was installed, run or adopted; no strategy returns were measured.

## 2026-10-09

- Added 50 commit-pinned source reviews from the existing private pending queue; the catalog grows from 462 to 512. Every added review reads a README and relevant implementation. Source tests are cited where inspected; none were run.
- New findings cover provisional indicator state, malformed Hyperliquid L2 levels, a grid runner that sends orders despite an out-of-range hold, broker submission uncertainty, synthetic bar replay and temporal drift calibration.
- Low-fit and unsupported performance claims remain visible as cautions with low ratings. No upstream software was installed, executed or adopted.
- Refreshed recent findings; the public repository remains a GitLab staging surface, not a GitHub publication.

## 2026-10-06

- Added 50 commit-pinned, source-backed reviews from the private pending queue, bringing the catalog from **412 to 462**. Rating distribution: {1: 13, 2: 21, 3: 16}; low-fit examples are scored 1/5 rather than endorsed.
- Findings include a gap detector that reconstruction does not automatically invoke, separate approval and submission states, strict order-rejection tests, lossy catalog identifiers, time-window leakage, trial-key collisions and interrupted-agent outcomes.
- Four relevant upstream test files were read without execution. Missing root license files, a custom EULA, restricted redistribution and mixed copyleft terms are stated in the affected reviews. No upstream software was installed or adopted.
- Updated recent findings and added OmniScientist as a third Agents & Decision Systems honorable mention.

This log records substantive review additions and corrections. GitHub star-count changes alone do not count as editorial updates.

## 2026-09-27

- Added 50 source-backed reviews from the existing candidate queue, bringing the catalog from **362 to 412**. The batch focuses on trading inputs, quality contracts, experiment identity and adversarial verification; scores apply only to the inspected mechanisms.
- New findings cover recovery during timeouts, failed versus absent data, initial-wealth drawdown, zero-selection ranking, equal-time window boundaries, per-key freshness, cache ownership and constrained trace reduction.
- Seven reviews include relevant test-code reading. No upstream project or test was installed or executed. Restricted app licensing in ModelFox, Elastic License 2.0 in Swiple, missing root license texts and obsolete or experimental components are explicit.
- Refreshed recent findings with QuickFIX/Go recovery, SparkDQ freshness scope and a Blueshift ranking boundary. Existing honorable mentions remain selected for distinct uses.

- Added another 40 commit-pinned source reviews, bringing the catalog from **322 to 362**. Four receive 4/5, 25 receive 3/5 and 11 receive 2/5; no 5/5 is assigned.
- This batch inspects retry eligibility, uncertain delivery, asynchronous commissions, simulated partial fills, order-book checksums, late-window corrections, backpressure-aware idleness, checkpoint coverage, worker-loss recovery, solver-result validity, indicator initialization and experiment-cache identity.
- The scikit-survival review includes relevant boundary-test reading; no upstream code or tests were executed. Legacy SDKs, a missing root license text and narrow delegated-code scopes remain explicit.
- Refreshed recent findings with Binance retry policy, TA-Lib's provisional-versus-committed stream interface and Beam's late-window trigger. Existing honorable mentions remain selected for distinct uses.

- Added 40 commit-pinned source reviews, bringing the catalog to **322** across ten areas. One receives 4/5, 30 receive 3/5 and nine receive 2/5; no 5/5 is assigned.
- New reviews inspect delayed labels, retrospective state inference, factor-cleaning population loss, multiplicity families, rolling-window validity, annualization clocks, expected failures, snapshot acceptance, run recovery, cache identity, binary decoding, RPC observation identity and per-order batch outcomes.
- The rust-bitcoin review also reads a relevant witness-identity test. Upstream code and tests were not executed. Ratings assess the described source mechanism, not the whole project.
- Expanded the on-chain comparison with RPC observation identity, durable watcher checkpoints, transaction hashes, branch reversals and binary framing/ABI checks; restored the continuous comparison-table formatting.
- Refreshed recent findings with Alphalens, River and Bybit.Net. Existing honorable mentions remain selected for distinct uses; the full area inventories include every completed addition.

## 2026-09-26

- Simplified the homepage to three recent source findings, area navigation and at most three honorable mentions per area. Full inventories and their ratings remain on the area pages.
- Replaced the broad "in-depth" count with "source-backed reviews" and clarified that ratings assess a specific inspected mechanism. Source reading and test reading are distinguished from runtime evaluation. No project scores changed.

- Added 40 further commit-pinned source reviews, bringing the catalog to **282**. Four receive 4/5, 30 receive 3/5 and six receive 2/5; no 5/5 is assigned. Relevant tests were read in four reviews, without executing upstream code.
- Additions cover feed continuity and RPC completeness, execution timeouts and remote signing boundaries, portfolio trade feasibility, indicator warm-up, numerical and statistical assumptions, dataset retention and idempotent commits, bounded concurrency exploration and operational evidence.
- Expanded the on-chain comparison with retained history, RPC range limits, replay checkpoints and oracle valuation units. Deprecated source locations and mixed licensing remain explicit.

- Added the remaining 40 commit-pinned source reviews, bringing the catalog to 242. Five receive 4/5, 18 receive 3/5, 16 receive 2/5 and one receives 1/5. Every addition identifies a specific implementation, a practical limitation and a trading-system reason for its score.
- New execution and replay references cover missing fill-price evidence, accounting epochs, broker-state fingerprints and queue diagnostics. Research-agent reviews distinguish structural checks from valid evidence, provisional outcomes from settled labels, and tool hints from authorization.

- Added 50 commit-pinned source reviews, bringing the catalog to 202 across ten areas. The additions inspect on-chain feed recovery, data-quality scope and metric revisions, reproducible artifacts, feature preprocessing, simulated fills, broker events, and numerical parity.
- Six additions receive 4/5, 23 receive 3/5, 18 receive 2/5, and three receive 1/5. Low scores retain concrete findings and limitations; a completed review is not an implementation recommendation. Generic agent references remain at 2/5.
- Expanded the [on-chain comparison](guides/on-chain-data.md) with Bitcoin notifications, mempool reconciliation, Ethereum log removals, index checks, retained stream replay, and DeFi metric definitions. Source-visible commercial restrictions and absent or conflicting license declarations are explicit in individual reviews.

- Added 12 pinned on-chain source reviews, bringing the catalog to 152. The new comparison guide covers extraction, reorg handling, empty-block coverage, historical entity state, and metric vintages. Ponder joins the market-data honorable mentions.
- Recorded zero block hashes and decimal-to-float conversion in the inspected Squid SDK fills normalizer, height-only checkpoint limits in both ETL streamers, and the limits of historical enrichment in Graph Node and Spellbook. Spellbook is identified as source-available under BSL 1.1; DefiLlama's ISC declaration is distinguished from an absent root license text.

- Rewrote all 28 honorable mentions as factual project descriptions under "What it offers". Each full review now includes a short project overview linked to pinned documentation.
- Added 40 commit-pinned source reviews, bringing the catalog to 140 across ten areas. Every area now has at least eight completed reviews.
- Execution and simulation reviews distinguish cancel-request acceptance from confirmed completion, inspect native adapter capability checks, and expose full-fill, order-precedence, and market-impact assumptions.
- Signals and portfolio reviews inspect future-price perturbation, historical versus developing higher-timeframe bars, and the mapping from allocation decisions to trade dates.
- Data and research reviews examine disconnected feed intervals, calendar coverage, overlapping validation populations, publication delays, reference-only artifact hashes, and cache dependencies.
- Agent and testing reviews examine prompt-only position limits, unknown-exposure allowances, disabled runtime contracts, and a contract-test example that reports a mismatch without an explicit failing assertion.
- Recorded restrictive terms in DQX and StockSharp, and unclear licensing in QTrader; visible source is not treated as permission to reuse code.
- Added distinct honorable mentions in Market Data & Ingestion, Portfolio & Risk, Operations & Observability, and Agents & Decision Systems. Signals & Models gains a future-perturbation reference.

## 2026-09-25

- Added 30 commit-pinned source reviews, bringing the catalog to 100 across ten areas. Every entry names a concrete mechanism, a limitation, a license, and its relevance to a trading system.
- Exchange and replay findings include a Hyperliquid WebSocket acknowledgement timeout followed by client-ID reconciliation in NexusTrader, order-state handling in QuantTrader, and a calendar intersection that can hide missing sessions in GS Quant.
- Data and research findings include a feature join that checks event time but needs an independent publication-time condition, deterministic checks for numerical claims, and a source-visible mlfinlab splitter stub with restrictive license terms.
- Signals & Models now has two honorable mentions: historical model availability and the denominator of multiple-testing correction.
- Added six pinned source reviews: Zipline Reloaded, VectorBT, Backtrader, Backtesting.py, Barter, and Vibe-Trading. The Zipline review records an as-of bundle documentation/code mismatch; VectorBT license and community-edition limits are explicit.
- Backtesting & Simulation now has nine complete reviews and three distinct honorable mentions: data vintage, backtest/live order timing, and dual event clocks.
- Added ArcticDB, Kedro, lakeFS, TSCV, and Rapid reviews. Source-available terms and exact failure conditions are visible in the relevant reviews.
- Research & Reproducibility and Testing & Verification now each have eight completed reviews and three selected honorable mentions.
- Added five source-backed reviews: nktkas/hyperliquid, fast-check, dbt, Soda Core, and data-diff. The Soda review records its Elastic License 2.0 terms; the data-diff review records that active development stopped in 2024.
- Data Quality & Lineage now has eight reviews and three distinct honorable mentions: decision-time feature availability, sample loss during validation, and the limits of declared lineage.
- Limited the public Atlas to 54 projects with complete, commit-pinned source reviews. Discovery candidates no longer appear in the public catalog or area pages.
- Recalibrated every rating for practical value to a data-driven trading system. Direct trading mechanisms, transferable engineering patterns, and adjacent references now have explicit scoring limits. Generic LLM evaluation projects no longer receive a high trading-system score on general software merit.
- Kept at most three honorable mentions, only in areas with at least eight completed reviews.
- Published source reviews across all ten areas, with an observed mechanism, main limit, license, review depth, and exact upstream commit in each.
- Added [Order completion and fill evidence](guides/order-completion.md), a comparison of acceptance, terminal state, fill completeness, and execution reporting.

Corrections to a review will identify the affected claim and source in this log.
