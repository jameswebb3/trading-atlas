<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="Trading Systems Atlas by James Webb 3: 1,066 source-backed reviews and 478 unrated projects among 1,544 considered" src="assets/hero-light.svg" width="100%">
</picture>

<p align="center"><strong>By James Webb 3</strong></p>

<p align="center">
  <a href="#start-with-your-problem"><b>Start with your problem</b></a> ·
  <a href="#top-rated"><b>Top-rated</b></a> ·
  <a href="#explore-by-area"><b>Browse by area</b></a> ·
  <a href="PROJECTS.md"><b>All 1,544 projects</b></a> ·
  <a href="METHODOLOGY.md"><b>How we rate</b></a>
</p>

**Which open-source trading tools get the hard parts right?** For each rated review, we inspect the source code to see how the project handles lookahead, fills, disconnects, chain reorganizations and the other places where a trading system quietly loses money.

Built for **systematic crypto trading**: perpetual futures, on-chain DEX venues such as Hyperliquid, and on-chain data. Stock, forex and general engineering tools are included when their mechanisms transfer, and are rated for what they offer a crypto trading system.

## Why this Atlas is different

<table>
<tr>
<td valign="top" width="50%"><b>🔍 Source, not stars</b><br>Every review links to the exact lines of code behind it, at a pinned commit you can open yourself.</td>
<td valign="top" width="50%"><b>⚠️ Every review names the catch</b><br>Next to the mechanism worth copying, you get the limitation that bites when real money is involved.</td>
</tr>
<tr>
<td valign="top"><b>⚖️ Rated for trading, not popularity</b><br>An excellent general-purpose library can score 2/5 if it does not touch a trading risk. A 4/5 needs a trading-specific mechanism visible in code.</td>
<td valign="top"><b>🚫 Nothing to sell</b><br>No sponsored listings, no affiliate links, no backtest screenshots. We do not measure or promise returns.</td>
</tr>
</table>

## What a review gives you

Every review asks one engineering question, answers it from the source code, and states the limit.

> **[Kerosene](https://github.com/nilesjarvis/kerosene)** · ★★★★☆ (4/5) · Execution & Exchange Integration
>
> **The question.** What evidence is needed to close a chase order and report its actual fill price?
>
> **What it gets right.** Waits for complete fill and open-order evidence before closing a repriced order.
>
> **The catch.** Its own metrics audit says archived average price can be the last limit, not the fill-weighted price.
>
> [Read the full review, with links to the exact lines →](reviews/kerosene.md)

<a id="start-with-your-problem"></a>
## Start with your problem

Common ways trading systems go wrong, and the reviews that show how real projects handle them.

<table>
<tr>
<td valign="top" width="33%"><b>My backtest looks great. Is it using information it could not have had?</b><br><br><a href="reviews/freqtrade.md">Freqtrade</a> 4/5<br><a href="reviews/spectre.md">Spectre</a> 4/5<br><a href="reviews/machine-learning-for-trading.md">Machine Learning for Trading</a> 4/5<br><a href="reviews/pinets.md">PineTS</a> 4/5</td>
<td valign="top" width="33%"><b>Will my simulated fills hold up against a real order book?</b><br><br><a href="reviews/nautilustrader.md">NautilusTrader</a> 4/5<br><a href="reviews/hftbacktest.md">HftBacktest</a> 4/5<br><a href="reviews/flox.md">FLOX</a> 4/5<br><a href="reviews/lean.md">LEAN</a> 4/5</td>
<td valign="top" width="33%"><b>Is my order really filled, and at what price?</b><br><br><a href="reviews/kerosene.md">Kerosene</a> 4/5<br><a href="reviews/hummingbot.md">Hummingbot</a> 4/5<br><a href="reviews/nexustrader.md">NexusTrader</a> 4/5<br><a href="reviews/aat.md">AAT</a> 4/5<br><a href="guides/order-completion.md">Comparison guide</a></td>
</tr>
<tr>
<td valign="top" width="33%"><b>Which exchange client can I trust with a live account?</b><br><br><a href="reviews/ccxt.md">CCXT</a> 4/5<br><a href="reviews/nktkas-hyperliquid.md">nktkas/hyperliquid</a> 4/5<br><a href="reviews/barter-rs.md">Barter</a> 4/5</td>
<td valign="top" width="33%"><b>Am I validating a strategy without fooling myself?</b><br><br><a href="reviews/stefan-jansen-alphalens-reloaded.md">Alphalens Reloaded</a> 4/5<br><a href="reviews/tscv.md">TSCV</a> 3/5<br><a href="reviews/skfolio.md">skfolio</a> 3/5<br><a href="reviews/statsmodels.md">Statsmodels</a> 3/5</td>
<td valign="top" width="33%"><b>Do my P&L and drawdown match what actually happened?</b><br><br><a href="reviews/quantinveststrats.md">QuantInvestStrats (qis)</a> 4/5<br><a href="reviews/enarjord-passivbot.md">Passivbot</a> 4/5<br><a href="reviews/quantstats.md">QuantStats</a> 3/5</td>
</tr>
<tr>
<td valign="top" width="33%"><b>How do I keep on-chain data correct through chain reorganizations?</b><br><br><a href="reviews/ponder.md">Ponder</a> 4/5<br><a href="reviews/squid-sdk.md">Squid SDK</a> 4/5<br><a href="reviews/alloy.md">Alloy</a> 4/5<br><a href="reviews/graph-node.md">Graph Node</a> 4/5<br><a href="guides/on-chain-data.md">Comparison guide</a></td>
<td valign="top" width="33%"><b>How do I notice when a feed or a job silently stops?</b><br><br><a href="reviews/healthchecks-healthchecks.md">Healthchecks</a> 3/5<br><a href="reviews/datacontract-cli.md">Data Contract CLI</a> 3/5<br><a href="reviews/dagster.md">Dagster</a> 3/5<br><a href="reviews/prometheus-alertmanager.md">Alertmanager</a> 3/5</td>
<td valign="top" width="33%"><b>Can an AI agent research or trade without going off the rails?</b><br><br><a href="reviews/monarchjuno-tradingcodex.md">tradingcodex</a> 4/5<br><a href="reviews/openalice.md">OpenAlice</a> 3/5<br><a href="reviews/anti-autoresearch.md">Anti-Autoresearch</a> 3/5</td>
</tr>
</table>

## Why 478 projects are unrated

**A rating is a claim we should be able to defend.** It says that a specific mechanism in the code is useful for a trading-system decision, and it names the condition or limitation that matters. We publish that claim only when we can trace it to relevant implementation at a pinned commit. GitHub stars, a feature list, or a plausible README are not enough.

A project stays in the [search ledger](PROJECTS.md) without a score if it is a reading list or tutorial rather than an inspectable mechanism; its useful pattern is generic or already covered more directly; the available source does not substantiate its interesting claim; or its scope is too far from the trading decisions covered here. This preserves useful leads without implying a completed review or a trading endorsement.

**How far the 478 records got:** 123 had source reading but no complete published assessment; 302 were screened from documentation; 46 stopped at an initial fit check; and 7 lacked verifiable source or implementation. These are evidence states, not software-quality scores. [See every project and its status](PROJECTS.md) · [Read the publication gate](METHODOLOGY.md#publication-gate).

## The Atlas at a glance

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/areas-dark.svg">
  <img alt="Completed reviews per area, split by review rating. The same counts are listed under Explore by area." src="assets/areas-light.svg" width="100%">
</picture>

84% of reviews land at 2 or 3: a useful pattern with real limits. The last segment of each bar counts its share of the 90 reviews rated 4/5.

<a id="top-rated"></a>
## Top-rated: 90 reviews scored 4/5 or higher

Directly relevant trading mechanisms, visible in code, with their limits stated. Only 8% of reviews reach this score.

<details>
<summary><b>Market Data & Ingestion</b> · 21 projects</summary>

- **[Alloy](reviews/alloy.md)** — Emits removed log batches before replacement batches and includes blocks with no matching logs. A useful reference for canonical event streams and measurable block coverage.
- **[Bitcoin Core](reviews/bitcoin-core.md)** — Provides canonical Bitcoin node data and read-only event notifications. Its ZeroMQ feed has separate transport and mempool sequence numbers, plus distinct block connect/disconnect and transaction add/remove events; recovery remains the collector's responsibility.
- **[CCXWS](reviews/altangent-ccxws.md)** — Preserves raw level strings and implements an exchange-specific checksum over the top of a reconstructed book. Useful for book-integrity diagnostics, provided mismatch detection and resnapshot policy are implemented separately.
- **[Cryptofeed](reviews/bmoscon-cryptofeed.md)** — A strong reference for exchange-feed normalization and book recovery. Its Binance sequence gate discards a broken local book; inspect each venue adapter before relying on the same continuity guarantee.
- **[Erigon](reviews/erigontech-erigon.md)** — A strong on-chain ingestion reference for failing explicitly when evidence is missing. The inspected log path rejects unavailable headers, with a regression test that prevents an incomplete scan from looking like a valid result.
- **[evm-indexer](reviews/eabz-evm-indexer.md)** — The reorg guard compares a stored block hash with the incoming chain and raises an error when the rollback depth exceeds a configured maximum. The bound protects against destructive automatic rewrites, but data inside the confirmation window is still delayed and consumers need epoch-aware validity.
- **[Flint](reviews/sohan-shingade-flint.md)** — Records asserted tick coverage separately from observed rows, preserving quiet markets without hiding recorder gaps.
- **[Geth](reviews/go-ethereum.md)** — An Ethereum execution client with RPC queries and live subscriptions. Its log event system forwards both added and removed logs through the same matching path, giving consumers explicit reversal evidence after a reorg.
- **[Hyperliquid Avellaneda Research Bot](reviews/djienne-avellaneda-market-making-freqtrade.md)** — Publishes validated Hyperliquid tape parts and blocks entries on stale books or invalid parameters.
- **[hyperliquid-data](reviews/bond-labs-dev-hyperliquid-data.md)** — Requires all 24 hourly archive objects before writing a daily trade or L2 Parquet file and keeps exchange and node timestamps separate.
- **[hyperliquid-data-pipeline](reviews/giri-aayush-hyperliquid-data-pipeline.md)** — Its raw-frame spool receives websocket frames before parsing and independently of a drop-oldest processing queue, preserving a separate archive path with receive timestamps and overflow counts.
- **[hyperliquid_microstructure](reviews/kimsoo7261-hyperliquid-microstructure.md)** — It reconstructs missing diff times from order-status and trade anchors, records the source of each assigned time, and marks re-emitted history after collector restarts.
- **[Kalshi Python SDK](reviews/texascoding-kalshi-python-sdk.md)** — Its sequence tracker drops duplicates and gap/reset frames; the queue raises a labelled backpressure error for stateful channels and delivers it after already buffered messages. The caller must still clear book state and resubscribe on the gap callback; a complete fill ledger is outside this path.
- **[Mempool](reviews/mempool.md)** — Tracks Bitcoin mempool transactions and fee conditions. Its cache temporarily delays mass deletion after a large contraction, reducing restart-induced false changes, and excludes catch-up traffic from live arrival-rate counters.
- **[Polymarket C++ Client](reviews/sebastianboehler-polymarket-cpp-client.md)** — Invalidates cached books and rejects callbacks from an old WebSocket generation.
- **[Ponder](reviews/ponder.md)** — Indexes EVM events into queryable tables and uses a database change log to undo forked state. The same handlers serve backfills and live indexing.
- **[predmarket-arb](reviews/cyriljoby-predmarket-arb.md)** — Tracks Kalshi sequence numbers across control and book frames, then reconnects for a fresh snapshot on a true gap.
- **[Squid SDK](reviews/squid-sdk.md)** — Separates finalized and reversible block state, and checks consecutive heights in its Hyperliquid fill archive reader. Useful references for backfill continuity and database progress.
- **[Substreams](reviews/substreams.md)** — Pairs row-change history with a transactional cursor update during SQL rollback. Also exposes block-hash undo notifications to cancel work based on invalidated blocks.
- **[TrueBlocks chifra](reviews/trueblocks-chifra.md)** — Indexes address appearances and exposes separate checks for chunk coverage, manifest fields, and Bloom-filter consistency. The distinction is useful when validating a large local index: a well-formed manifest alone proves little about its contents.
- **[Yellowstone gRPC](reviews/yellowstone-grpc.md)** — Streams Solana slots, transactions, account updates, and blocks with explicit commitment levels. Its replay path rejects requests older than retained history, while slow consumers are disconnected instead of receiving an apparently continuous stream.

</details>

<details>
<summary><b>Data Quality & Lineage</b> · 4 projects</summary>

- **[ChainIndexor](reviews/goran-ethernal-chainindexor.md)** — It compares incoming headers and logs with stored hashes inside a DB transaction and returns an explicit reorg error. Detection alone does not retract already derived features.
- **[CNEquity](reviews/rootsunc-cnequity.md)** — Its strict point-in-time filter checks announcement, availability, source publication and local observation against as_of, and rejects reconstructed/backfill sources; best-effort keeps them with pit_is_exact=false. A test contrasts both modes.
- **[Graph Node](reviews/graph-node.md)** — Stores mutable entity versions over block ranges and filters historical queries by the requested block. Useful for reconstructing chain state without substituting today's entity value.
- **[Point-in-Time Feature Store](reviews/datawizard1394-point-in-time-feature-store.md)** — The eligibility filter includes a transaction only if its event_time and available_at are both no later than the as-of time. The fixture is synthetic and does not model corrected source revisions or uncertainty in the recorded availability clock.

</details>

<details>
<summary><b>Research & Reproducibility</b> · 4 projects</summary>

- **[Alphalens Reloaded](reviews/stefan-jansen-alphalens-reloaded.md)** — A valuable factor-reporting reference with two concrete checks: account for sample loss at each cleaning stage and inspect future-return filtering. The convenience defaults differ from the lower-level API and can change the evaluated population.
- **[cherries](reviews/liblaf-cherries.md)** — At run start it records each scoped repository’s HEAD, working-tree patch, status, submodule topology and allowed untracked source files, with hashes in a source manifest. It also captures the entrypoint and environment before calling the experiment.
- **[go-trader](reviews/richkuo-go-trader.md)** — The comparison classifies closed-bar versus forming-bar decisions and refuses to claim parity when historical decision inputs were not recorded. Even closed-bar mode can read bars later corrected by the venue and the scheduled check may lag the simulated boundary.
- **[TradeSight](reviews/rmbell09-lang-tradesight.md)** — Separates legacy P&L from broker-supported results and preserves the evidence behind each classification. Inspect the local-price fallback before treating that classification as fully verified accounting.

</details>

<details>
<summary><b>Signals & Models</b> · 6 projects</summary>

- **[Machine Learning for Trading](reviews/machine-learning-for-trading.md)** — Shifts premium bars from open time to publication time before a backward join, then measures matched-value age.
- **[PineTS](reviews/pinets.md)** — PineTS selects a completed higher-timeframe bar for historical lookahead-off requests, but can return the developing bar in real time. That difference matters when porting indicators to automated trading. The inspected edge-case test checks output existence and length, not numerical equivalence between modes.
- **[pm-calibration](reviews/crollila-pm-calibration.md)** — Tests forecast calibration with event clusters and converts candidate trades to depth-capped, fee-adjusted outcomes.
- **[polyvol](reviews/rohanrcode1-polyvol.md)** — Tests reversion at bid/ask with both fees and clusters statistical inference by market.
- **[Spectre](reviews/spectre.md)** — Spectre computes factors over full arrays and includes a lookahead probe that replaces future OHLCV values, reruns the engine, and compares earlier outputs. This is a useful causal regression pattern for vectorized research. One cut and one perturbation do not establish all feature, universe, or publication-time semantics.
- **[vibe-astock](reviews/simonlin1212-vibe-astock.md)** — Its preflight calls the same getters used by analysts, blocks a run before the day settles or when a core input is empty or degraded, and records missing optional inputs as warnings.

</details>

<details>
<summary><b>Backtesting & Simulation</b> · 26 projects</summary>

- **[ABIDES JPMC](reviews/jpmorganchase-abides-jpmc-public.md)** — Models a crossing order as successive partial executions against resting prices, then retains the unmatched remainder. A useful fill-accounting oracle, with synthetic-book and integral-unit assumptions.
- **[AlphaTrade](reviews/kangoxford-alphatrade.md)** — Implements price-time book matching and delayed execution-agent actions.
- **[CleoLOB](reviews/damraka-cleolob.md)** — Its analysis registry specifies required data capabilities and returns NOT_AVAILABLE with missing fields rather than weakening an exact-fill study silently.
- **[Cvxportfolio](reviews/cvxgrp-cvxportfolio.md)** — A strong portfolio-simulation reference that preserves the gap between intended weights and executable trades. Liquidity caps, rounding and cash are explicit; order-book fills and derivatives accounting require a different execution model.
- **[Finance](reviews/shashankvemuri-finance.md)** — Makes next-open signal timing and cash reconciliation explicit, with hand-calculated tests. A useful bar-replay reference whose share-based accounting needs adaptation for derivatives.
- **[FLOX](reviews/flox.md)** — Cancels a non-crossing IOC and tracks visible quantity ahead of a passive limit order in its simulated executor.
- **[HftBacktest](reviews/hftbacktest.md)** — Rejects decreasing exchange timestamps and decreasing local timestamps on their respective event streams.
- **[HFTENGINE](reviews/mirkovicdev-hftengine.md)** — Makes a replay's queue, latency and order decisions inspectable frame by frame. A useful execution-debugging reference whose modeled queue and latency remain explicit assumptions.
- **[honest-backtest](reviews/johanalvarado-honest-backtest.md)** — Regrades paper buys against the ask seen after order latency and, when available, a corroborating execution tape.
- **[Hyperliquid Backtest Toolkit](reviews/yifanxie-hyperliquid-backtest.md)** — Models a USDC-margined perpetual ledger and defaults to next-bar fills, while explicitly leaving partial fills and L2 impact outside the simulation.
- **[Jesse](reviews/jesse.md)** — Tests stop and take-profit fills across price gaps in both step and fast replay modes.
- **[Kalshi Bitcoin ML Trading System](reviews/rawanalytics-kalshi-bitcoin-ml-trading-system.md)** — Reprices recorded paper and live fills against bid/ask candles, counts missing and empty quote states, then evaluates forward folds at quote-side prices and fees.
- **[kalshi-stack](reviews/agiprolabs-kalshi-stack.md)** — Its print-replay module explicitly labels passive-fill EV an upper bound; the paper exchange adds queue-ahead depletion, trade-ID deduplication and one-time print-volume spending.
- **[KORE](reviews/cole-godfrey-kore.md)** — Walks displayed binary-book depth, checks cash and positions, and records orders that expire before their latency elapses.
- **[LEAN](reviews/lean.md)** — Documents separate transaction processing for backtest and live, and processes pending backtest requests synchronously with the algorithm loop.
- **[limit-order-book-sim](reviews/matr1xow-limit-order-book-sim.md)** — Simulates passive queue position under cancellation bounds and checks reconstructed books against separate snapshots.
- **[lobster](reviews/s4nngr10r-lobster.md)** — Replay rejects invalid, out-of-order, duplicate-live and noncontiguous sequence events. The check cannot recreate events absent before capture; sequence meaning is source-specific.
- **[mm-lab](reviews/batuhanboztepe0-mm-lab.md)** — Defines a readable fill oracle for a fast kernel, fingerprints cached research cells, and checks fill-log accounting against engine state.
- **[NautilusTrader](reviews/nautilustrader.md)** — Makes the simulated venue book type explicit and rejects unsupported time-in-force paths.
- **[OKX Perp Backtest](reviews/leandrocolombo111-okx-perp-backtest.md)** — Raises on unavailable funding and preserves indicator warmup outside each scored walk-forward window.
- **[order_book_server](reviews/hyperliquid-dex-order-book-server.md)** — It stores per-price ordered order IDs and refuses insertion when the referenced resting order is absent, detecting divergence from a diff. This local reconstruction is not proof of exchange matching priority or a fill model for a user account.
- **[orderbook-replay-lab](reviews/ozankenangungor-orderbook-replay-lab.md)** — The reader checks record headers and payload lengths, raising UnexpectedEof on a truncated prefix, header or payload. Binary integrity does not itself prove that all venue events were captured before the file was written.
- **[ordersim](reviews/tradingexpert-ordersim.md)** — Its equivalence helper replays the same canonical events through reference and candidate engines, then compares fills, positions, resting orders, summaries, equity and order events.
- **[PineForge](reviews/pineforge-4pass-pineforge-engine.md)** — Records broker-state fingerprints across batch and streaming paths, with prefix-invariance tests. Useful for finding the first execution divergence rather than comparing only final P&L.
- **[polymarket-microstructure-lab](reviews/hugompt-polymarket-microstructure-lab.md)** — Replays the same forward paper decision across a latency grid and computes fee-aware break-even thresholds.
- **[PurgedCV](reviews/landtml-purgedcv.md)** — It converts event end times to positions, removes interval-overlapping training rows and applies a forward embargo from a declared anchor. Correct interval splitting does not establish that each input feature was published by its decision time or that holdout selection stayed untouched.

</details>

<details>
<summary><b>Execution & Exchange Integration</b> · 22 projects</summary>

- **[deliverator](reviews/erickuhn19-deliverator.md)** — It refuses an authoritative diff if sub-dex open orders or position snapshots are degraded, then compares account and audit state. A clean diff still depends on complete fills and audit retention; the live path was not run here.
- **[AAT](reviews/aat.md)** — Records the order and strategy before sending, so an early fill can still be attributed.
- **[autotrader](reviews/aaronmin8460-autotrader.md)** — The reconciler rechecks a broker not-found answer and keeps ambiguous UNKNOWN intents blocking until it can resolve them from broker truth. The safety result depends on the broker lookup contract and its eventual consistency; the repository has no verified root license in this review.
- **[Banbot](reviews/banbot.md)** — Banbot defines an adapter capability for client-ID parsing, event order identity, and timestamp normalization. In strict mode it rejects adapters that do not implement that capability. This is a useful boundary for exchange integration; capability presence still needs behavioral conformance tests.
- **[Barter](reviews/barter-rs.md)** — Replicates engine state from a snapshot and sequenced audit stream, rejecting sequence gaps. Order types separate local in-flight open and cancel requests from confirmed states.
- **[Binance Python Connectors](reviews/binance-binance-connector-python.md)** — Restricts automatic retries by HTTP method and error class rather than retrying every failed call. A strong reference for keeping query recovery separate from uncertain trading actions.
- **[bytex](reviews/bytex-trade-bytex.md)** — The private-stream handler subscribes to userEvents but reads fills from messages whose reply channel is user; it also separates order updates and private errors. The comment reports observed channel behavior, but this review did not independently replay venue messages or prove all terminal statuses.
- **[CCXT](reviews/ccxt.md)** — In its Hyperliquid adapter, a market order becomes a protected IOC limit with venue-specific fields.
- **[Chainstack Hyperliquid Trading Bot](reviews/chainstacklabs-hyperliquid-trading-bot.md)** — Checks a live position for vanished protective orders and attempts to re-arm them.
- **[Cross-Venue Arbitrage Decision Core](reviews/max0514-polymarket-bot.md)** — Uses a replayable reducer and logs rejected opportunities with fee and risk reasons.
- **[Hummingbot](reviews/hummingbot.md)** — Tracks open and lost orders and deduplicates fills by trade ID.
- **[hyperliquid-python-ml-to-rust-layer](reviews/londrwus-hyperliquid-python-ml-to-rust-layer.md)** — Its ADR gives Fill and OrderUpdate distinct types, uses absolute remaining size, and places the venue client behind a GuardedClient risk gate.
- **[hyperopen](reviews/thegeronimo-hyperopen.md)** — A documented fix overlays live fills and open orders onto a frozen submission ledger, using exchange order IDs and client-order ownership to identify the order.
- **[HyperTrade](reviews/davassi-hypertrade.md)** — Queries a deterministic Hyperliquid client order ID before retrying an uncertain send.
- **[ib_async](reviews/ib-api-reloaded-ib-async.md)** — Separates order completion, individual executions and subsequent commission reports. Useful for execution accounting that must remain provisional until costs arrive; the inspected deduplication path is in memory.
- **[Kerosene](reviews/kerosene.md)** — Waits for complete fill and open-order evidence before closing a repriced order.
- **[NexusTrader](reviews/nexustrader.md)** — After a Hyperliquid WebSocket ACK timeout, it queries order status by client ID through REST with cache bypass before declaring failure. A confirmed order returns a distinct timeout-confirmed result; an unconfirmed request raises. This narrows one duplicate-order race but does not prove complete fill reconciliation.
- **[nktkas/hyperliquid](reviews/nktkas-hyperliquid.md)** — Serializes exchange requests per wallet and network before signing, then checks top-level and per-order error responses.
- **[QuantDinger](reviews/openbyteinc-quantdinger.md)** — A strong reference for fill accounting: requested prices never substitute for observed execution. Regression tests explicitly prevent incomplete fills from updating positions or the ledger.
- **[QuickFIX/Go](reviews/quickfixgo-quickfix.md)** — The resend state wraps itself in a pending-timeout state instead of discarding recovery.
- **[Tickwright](reviews/marcosach-tickwright.md)** — A failed send freezes the reconciliation cycle, while an unreadable response body is charged to the affected order and escalated on repeated failure. The code establishes an internal safety policy, not proof that a specific venue reports all delayed fills or terminal states.
- **[XEMM Pacifica–Hyperliquid](reviews/djienne-xemm-cross-exchange-market-making-pacifica-hyperliquid.md)** — Reconciles maker exposure against in-flight hedges before declaring a cycle complete.

</details>

<details>
<summary><b>Portfolio & Risk</b> · 2 projects</summary>

- **[Passivbot](reviews/enarjord-passivbot.md)** — A useful perpetual-trading reference for hard-stop and restart policies. Its risk logic separates cooldown from permanent restart veto, with explicit limits around missing history and account transfers.
- **[QuantInvestStrats (qis)](reviews/quantinveststrats.md)** — Maps dated allocation decisions onto executable price observations and rejects negative implementation lags or colliding trade dates. Useful for portfolio accounting; interior price gaps still require an explicit marking policy, and this is not an exchange fill simulator.

</details>

<details>
<summary><b>Testing & Verification</b> · 4 projects</summary>

- **[Freqtrade](reviews/freqtrade.md)** — Compares full and sliced backtests to expose lookahead in signals the test actually exercises.
- **[OoplesFinance.StockIndicators](reviews/ooples-finance-llc-ooplesfinance-stockindicators.md)** — The rolling-deviation state evaluates a provisional value without storing it until isFinal; a source test compares preview, final and clean paths across more than 700 public streaming states.
- **[scholar-loop](reviews/tenorleibniz832-scholar-loop.md)** — It hashes the frozen scorer, refuses scoring if the file changes or vanishes, restricts source edits to the train entrypoint and records per-seed results and failures. A fully failed seed set becomes a killed run.
- **[Stock Indicators for .NET](reviews/stock-indicators-dotnet.md)** — Implements financial indicators in batch, buffered, and streaming forms. The inspected EMA regression suite compares all three against the same stored baseline, while the EMA source and documentation expose warm-up and initialization semantics.

</details>

<details>
<summary><b>Agents & Decision Systems</b> · 1 projects</summary>

- **[tradingcodex](reviews/monarchjuno-tradingcodex.md)** — A database transaction binds an approval receipt and exact order hash to one idempotent reservation before provider submission; uncertain outcomes become `needs_review` and a test asserts retry is blocked.

</details>

<a id="recent-findings-and-corrections"></a>
## Recent findings & corrections

**Updated 2026-10-11.** Selected observations from new and updated reviews.

- **[Coinversa Pulse MCP Server](reviews/coinversaa-mcp-server.md)** — Agent results declare totalCount and truncated; dataset coverage keeps unknown window starts null instead of inventing dates.
- **[Hyperliquid Copy Trader](reviews/maxisontosomething-hyperliquid-copy-trader.md)** — A position-update handler calls .get on the positions list, so the exception path can log a failed event while the WebSocket stays connected.
- **[Hyperliquid Statistical Arbitrage Bot](reviews/aopunya4332-hyperliquid-stat-arb-bot.md)** — The claimed pairs strategy computes its second price from the first by default and orders only one leg.
- **[OBaI](reviews/sixteen-dev-obai.md)** — Correction: Backtest jobs have terminal result files, but a crash before completion leaves no persisted record of the accepted in-flight job.
- **[vectorbt Backtesting Skills](reviews/marketcalls-vectorbt-backtesting-skills.md)** — The quarterly winner is shifted, yet missing open prices can be backward-filled from later dates before the execution replay.

[See all additions and corrections](CHANGELOG.md).

## Explore by area

**1066 source-backed reviews across 10 areas.** Each area page lists its reviews ordered by rating. Ratings apply to the mechanism covered in each review; [see the scoring criteria](METHODOLOGY.md).

<table>
<tr>
<td valign="top" width="50%"><a id="market-data-ingestion"></a><h3><a href="areas/market-data-ingestion.md">Market Data & Ingestion</a></h3>Exchange feeds, on-chain indexing, backfills, stream gaps, and recovery.<br><br><b>124 reviews</b> · <a href="explored/market-data-ingestion.md">126 projects considered</a><br>Editor's picks: <a href="reviews/sqd-pipes-sdk.md">SQD Pipes SDK</a> · <a href="reviews/zabor.md">zaBor</a> · <a href="reviews/ponder.md">Ponder</a><br>Guide: <a href="guides/on-chain-data.md">On-chain data: from blocks to usable observations</a></td>
<td valign="top" width="50%"><a id="data-quality-lineage"></a><h3><a href="areas/data-quality-lineage.md">Data Quality & Lineage</a></h3>Whether a value was complete, traceable, and available when a decision was made.<br><br><b>185 reviews</b> · <a href="explored/data-quality-lineage.md">294 projects considered</a><br>Editor's picks: <a href="reviews/feast.md">Feast</a> · <a href="reviews/pandera.md">Pandera</a> · <a href="reviews/openlineage.md">OpenLineage</a></td>
</tr>
<tr>
<td valign="top" width="50%"><a id="research-reproducibility"></a><h3><a href="areas/research-reproducibility.md">Research & Reproducibility</a></h3>The data, code, parameters, and lineage needed to reproduce an experiment.<br><br><b>137 reviews</b> · <a href="explored/research-reproducibility.md">299 projects considered</a><br>Editor's picks: <a href="reviews/dvc.md">DVC</a> · <a href="reviews/mlflow.md">MLflow</a> · <a href="reviews/metaflow.md">Metaflow</a></td>
<td valign="top" width="50%"><a id="signals-models"></a><h3><a href="areas/signals-models.md">Signals & Models</a></h3>Signal timing, feature construction, validation, and retirement when evidence changes.<br><br><b>69 reviews</b> · <a href="explored/signals-models.md">94 projects considered</a><br>Editor's picks: <a href="reviews/darts.md">Darts</a> · <a href="reviews/statsmodels.md">Statsmodels</a> · <a href="reviews/spectre.md">Spectre</a></td>
</tr>
<tr>
<td valign="top" width="50%"><a id="backtesting-simulation"></a><h3><a href="areas/backtesting-simulation.md">Backtesting & Simulation</a></h3>Event clocks, market mechanics, costs, fills, and gaps between replay and live behavior.<br><br><b>114 reviews</b> · <a href="explored/backtesting-simulation.md">132 projects considered</a><br>Editor's picks: <a href="reviews/zipline-reloaded.md">Zipline Reloaded</a> · <a href="reviews/lean.md">LEAN</a> · <a href="reviews/hftbacktest.md">HftBacktest</a></td>
<td valign="top" width="50%"><a id="execution-exchange-integration"></a><h3><a href="areas/execution-exchange-integration.md">Execution & Exchange Integration</a></h3>Request translation, acknowledgements, fills, cancellation, and reconciliation.<br><br><b>136 reviews</b> · <a href="explored/execution-exchange-integration.md">164 projects considered</a><br>Editor's picks: <a href="reviews/aat.md">AAT</a> · <a href="reviews/ccxt.md">CCXT</a> · <a href="reviews/kerosene.md">Kerosene</a><br>Guide: <a href="guides/order-completion.md">Order completion and fill evidence</a></td>
</tr>
<tr>
<td valign="top" width="50%"><a id="portfolio-risk"></a><h3><a href="areas/portfolio-risk.md">Portfolio & Risk</a></h3>Sizing, exposure, limits, fees, drawdowns, and portfolio accounting.<br><br><b>45 reviews</b> · <a href="explored/portfolio-risk.md">59 projects considered</a><br>Editor's picks: <a href="reviews/quantinveststrats.md">QuantInvestStrats (qis)</a> · <a href="reviews/skfolio.md">skfolio</a> · <a href="reviews/quantlib.md">QuantLib</a></td>
<td valign="top" width="50%"><a id="testing-verification"></a><h3><a href="areas/testing-verification.md">Testing & Verification</a></h3>Lookahead, edge cases, event races, and failures that pass silently.<br><br><b>95 reviews</b> · <a href="explored/testing-verification.md">126 projects considered</a><br>Editor's picks: <a href="reviews/freqtrade.md">Freqtrade</a> · <a href="reviews/hypothesis.md">Hypothesis</a> · <a href="reviews/tscv.md">TSCV</a></td>
</tr>
<tr>
<td valign="top" width="50%"><a id="operations-observability"></a><h3><a href="areas/operations-observability.md">Operations & Observability</a></h3>Feed health, alerts, restarts, and evidence needed to explain an incident.<br><br><b>69 reviews</b> · <a href="explored/operations-observability.md">108 projects considered</a><br>Editor's picks: <a href="reviews/dagster.md">Dagster</a> · <a href="reviews/dagu.md">Dagu</a> · <a href="reviews/maestro.md">Netflix Maestro</a></td>
<td valign="top" width="50%"><a id="agents-decision-systems"></a><h3><a href="areas/agents-decision-systems.md">Agents & Decision Systems</a></h3>Evidence, permissions, evaluation, and failure handling for automated decisions.<br><br><b>92 reviews</b> · <a href="explored/agents-decision-systems.md">142 projects considered</a><br>Editor's picks: <a href="reviews/anti-autoresearch.md">Anti-Autoresearch</a> · <a href="reviews/openalice.md">OpenAlice</a> · <a href="reviews/omni-scientist-omniscientist.md">OmniScientist</a></td>
</tr>
</table>

<details>
<summary><b>Why these picks?</b> What each editor's pick offers</summary>

**Market Data & Ingestion**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [SQD Pipes SDK](https://github.com/subsquid/pipes-sdk) · [Review](reviews/sqd-pipes-sdk.md) | ★★★☆☆ (3/5) | TypeScript toolkit for streaming SQD Portal blockchain data into your own storage. Separates streams, decoders, and storage targets, with cursor tracking and chain-reorganization handling. |
| [zaBor](https://github.com/zabor-crypto/zaBor) · [Review](reviews/zabor.md) | ★★★☆☆ (3/5) | Market-engineering toolkit with data recording, risk-control modules, and research utilities. Its recorder preserves raw exchange payloads and local receipt times, supplying capture evidence for microstructure research. |
| [Ponder](https://github.com/ponder-sh/ponder) · [Review](reviews/ponder.md) | ★★★★☆ (4/5) | TypeScript framework for EVM data indexing into PostgreSQL, with SQL and GraphQL access. Records reversible table changes to roll back forked state and replay the canonical chain through the same event handlers. |

**Data Quality & Lineage**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [Feast](https://github.com/feast-dev/feast) · [Review](reviews/feast.md) | ★★★☆☆ (3/5) | Feature store for historical training datasets and online inference. Its timestamp-aware joins provide an explicit place to control which feature values are eligible at each observation time. |
| [Pandera](https://github.com/unionai-oss/pandera) · [Review](reviews/pandera.md) | ★★★☆☆ (3/5) | Dataframe validation library for schemas, types, and custom checks. Collects row-level failure details, helping research pipelines identify invalid inputs before building features or evaluating strategies. |
| [OpenLineage](https://github.com/OpenLineage/OpenLineage) · [Review](reviews/openlineage.md) | ★★★☆☆ (3/5) | Open standard for recording jobs, runs, and dataset relationships. Gives data pipelines a common way to report how inputs and outputs connect across tools. |

**Research & Reproducibility**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [DVC](https://github.com/treeverse/dvc) · [Review](reviews/dvc.md) | ★★★☆☆ (3/5) | Git-connected versioning for data, models, and experiments. Links inputs, parameters, and outputs to pipeline steps, making research changes and their reproduction requirements visible. |
| [MLflow](https://github.com/mlflow/mlflow) · [Review](reviews/mlflow.md) | ★★★☆☆ (3/5) | Experiment tracking platform for recording parameters, metrics, datasets, and model artifacts. Organizes runs and their supporting evidence so research results can be compared and investigated. |
| [Metaflow](https://github.com/Netflix/metaflow) · [Review](reviews/metaflow.md) | ★★★☆☆ (3/5) | Python framework for data and ML workflows with versioned runs and artifacts. Its branch-and-join model supports parallel experiments and explicit resolution when branch outputs disagree. |

**Signals & Models**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [Darts](https://github.com/unit8co/darts) · [Review](reviews/darts.md) | ★★★☆☆ (3/5) | Time-series forecasting and anomaly detection library with a common fit/predict interface across statistical and neural models. Supports historical evaluation, ensembles, and external covariates for model comparison. |
| [Statsmodels](https://github.com/statsmodels/statsmodels) · [Review](reviews/statsmodels.md) | ★★★☆☆ (3/5) | Statistical modelling library for regression, time-series analysis, and inference. Includes diagnostics and multiple-testing corrections for research that compares many signals or models. |
| [Spectre](https://github.com/Heerozh/spectre) · [Review](reviews/spectre.md) | ★★★★☆ (4/5) | PyTorch-based factor engine with GPU execution for cross-sectional trading research. Includes a future-data perturbation check to investigate lookahead in factor outputs. |

**Backtesting & Simulation**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [Zipline Reloaded](https://github.com/stefan-jansen/zipline-reloaded) · [Review](reviews/zipline-reloaded.md) | ★★★☆☆ (3/5) | Python event-driven backtesting engine with historical data bundles and pandas-based inputs and outputs. A reference for organizing strategy simulations, data ingestion, and performance analysis. |
| [LEAN](https://github.com/QuantConnect/Lean) · [Review](reviews/lean.md) | ★★★★☆ (4/5) | Algorithmic trading engine with pluggable data feeds, transaction handling, and event timing. A reference for structuring backtesting and live execution around a shared system architecture. |
| [HftBacktest](https://github.com/nkaz001/hftbacktest) · [Review](reviews/hftbacktest.md) | ★★★★☆ (4/5) | Market replay backtester for high-frequency and market-making strategies. Models feed latency, order latency, and queue position using order-book and trade data. |

**Execution & Exchange Integration**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [AAT](https://github.com/AsyncAlgoTrading/aat) · [Review](reviews/aat.md) | ★★★★☆ (4/5) | Asynchronous trading framework using the same strategy class for backtesting and live trading. Separates trading, risk, and execution engines, and tracks pending intent before an order send completes. |
| [CCXT](https://github.com/ccxt/ccxt) · [Review](reviews/ccxt.md) | ★★★★☆ (4/5) | API library for 100+ cryptocurrency exchanges and prediction markets. Provides common methods for market data, orders, and account access, plus normalized data for cross-exchange analysis. |
| [Kerosene](https://github.com/nilesjarvis/kerosene) · [Review](reviews/kerosene.md) | ★★★★☆ (4/5) | Rust desktop terminal for Hyperliquid with charts, order entry, and client-side Chase and TWAP automation. Its execution code is a useful reference for order repricing and fill reconciliation. |

**Portfolio & Risk**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [QuantInvestStrats (qis)](https://github.com/ArturSepp/QuantInvestStrats) · [Review](reviews/quantinveststrats.md) | ★★★★☆ (4/5) | Portfolio analytics and backtesting library that turns prices and target weights into holdings, costs, and performance reports. Makes allocation timing and weight drift explicit. |
| [skfolio](https://github.com/skfolio/skfolio) · [Review](reviews/skfolio.md) | ★★★☆☆ (3/5) | Portfolio optimization and risk library with a scikit-learn-compatible interface. Combines model selection, cross-validation, and stress testing to compare portfolio construction choices. |
| [QuantLib](https://github.com/lballabio/QuantLib) · [Review](reviews/quantlib.md) | ★★☆☆☆ (2/5) | Quantitative finance library for financial modelling and risk calculations. Offers numerical building blocks and explicit input checks, including rejection of tail estimates with no supporting observations. |

**Testing & Verification**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [Freqtrade](https://github.com/freqtrade/freqtrade) · [Review](reviews/freqtrade.md) | ★★★★☆ (4/5) | Python crypto trading bot combining backtesting, strategy optimization, and dry-run trading. Includes lookahead analysis for investigating whether strategy decisions depend on future data. |
| [Hypothesis](https://github.com/HypothesisWorks/hypothesis) · [Review](reviews/hypothesis.md) | ★★★☆☆ (3/5) | Property-based testing for Python that generates edge cases and reduces failures to small counterexamples. State-machine tests make it useful for exercising order, inventory, and ledger transitions. |
| [TSCV](https://github.com/WenjieZ/TSCV) · [Review](reviews/tscv.md) | ★★★☆☆ (3/5) | Scikit-learn extension for time-series cross-validation with configurable gaps and rolling-forward windows. Provides explicit control over the separation between training and evaluation samples. |

**Operations & Observability**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [Dagster](https://github.com/dagster-io/dagster) · [Review](reviews/dagster.md) | ★★★☆☆ (3/5) | Data orchestrator organized around assets such as datasets, models, and reports. Combines scheduling, lineage, and freshness checks to show how research inputs are produced and updated. |
| [Dagu](https://github.com/dagucloud/dagu) · [Review](reviews/dagu.md) | ★★★☆☆ (3/5) | Self-hosted workflow engine for scheduling existing scripts with dependencies, retries, and run history. Its single-binary, file-backed design needs no external database or message broker. |
| [Netflix Maestro](https://github.com/Netflix/maestro) · [Review](reviews/maestro.md) | ★★★☆☆ (3/5) | Workflow orchestrator from Netflix for data and ML pipelines. Provides step dependencies, execution history, and separate retry policies for user, platform, and timeout failures. |

**Agents & Decision Systems**

| Project | Review rating | What it offers |
| --- | --- | --- |
| [Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch) · [Review](reviews/anti-autoresearch.md) | ★★★☆☆ (3/5) | Research audit toolkit that connects numerical claims to source spans and deterministic checks. Produces traceable findings that help reviewers spot inconsistent tables, percentages, and reported arithmetic. |
| [OpenAlice](https://github.com/TraderAlice/OpenAlice) · [Review](reviews/openalice.md) | ★★★☆☆ (3/5) | Agent workspace for market research, scheduled follow-ups, and staged trading operations. Combines research history with a broker interface and deterministic pre-trade guards. |
| [OmniScientist](https://github.com/Omni-Scientist/OmniScientist) · [Review](reviews/omni-scientist-omniscientist.md) | ★★★☆☆ (3/5) | Separates user-stopped, truncated and normally completed research runs, with tests for round-limit exhaustion. |

</details>

## What the reviews cover

The [complete project ledger](PROJECTS.md) tracks all 1,544 discoveries with their evidence status. Only the 1,066 completed reviews carry a rating.

Each completed review examines a specific mechanism at a pinned commit, with links to the documentation and code behind the assessment. It records the review date, declared license, and limits of the inspected path. Some also examine relevant tests; we do not run upstream software.

**Review ratings describe the usefulness of that inspected mechanism to a trading system.** They do not score every feature of a project. Trading-specific mechanisms and general engineering tools have different scoring criteria, explained in the [methodology](METHODOLOGY.md).

**Not financial advice.** The Atlas reviews software engineering, not strategies. A good rating is not a recommendation to trade, to use a project with real money, or a claim about any project's returns. The reviewed projects are independent and not affiliated with the Atlas.

## Keep the Atlas useful

⭐ Star the Atlas to keep these reviews handy when choosing your trading stack.

Found a project worth reviewing or a claim we should correct? [Suggest a project or correction](CONTRIBUTING.md).

[Review methodology](METHODOLOGY.md) · [Area definitions](CATEGORIES.md) · [All updates](CHANGELOG.md)

Text and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with credit to Trading Systems Atlas — James Webb 3. Scripts: MIT. See [LICENSE](LICENSE).
