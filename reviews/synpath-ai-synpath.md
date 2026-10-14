# Synpath — Keep gaps and unresolved orders explicit

**Decision question:** Which missing facts must remain unknown in historical replay and account reconciliation?

| Field | Review |
| --- | --- |
| Upstream | [Synpath-ai/synpath](https://github.com/Synpath-ai/synpath) |
| Primary area | Execution & Exchange Integration |
| Source commit | [a3e810fa749b10201083b531209011777eab21f0](https://github.com/Synpath-ai/synpath/commit/a3e810fa749b10201083b531209011777eab21f0) |
| Reviewed | 2026-10-14 |
| Declared license | [MIT](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/LICENSE#L1) for the repository code; hosted data has separate service terms |
| Review depth | 3/3: documentation, relevant implementation and test source inspected; tests not run |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Historical replay preserves absent intervals and dataset identity; reconciliation reports venue/journal differences. A failed terminal-order lookup still becomes a local cancellation, and the inspected client does not establish real archive coverage or executable passive fills. |

## What this project offers

Synpath normalizes prediction-market APIs and provides a client for hosted Kalshi book and trade history. Its advertised historical service is separate from the local venue adapters. Historical requests send a Synpath key to the configured history host, while matching uses another hosted endpoint. [History client, lines 33–71](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/synpath/history.py#L33-L71), [hosted services, lines 1–41](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/synpath/hosted.py#L1-L41).

## Mechanism inspected

The response types retain dataset_version, a recorder-receive time basis, explicit available/unavailable intervals and separate venue and observation times. Book ranges carry initial books plus snapshots or exact decimal-string deltas. A missing snapshot is represented by book=None and an absence reason. These are client contracts, not independent evidence about what the recorder captured. [Historical types, lines 367–442](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/synpath/types.py#L367-L442).

The example tracker requires full-depth starting snapshots and rejects negative resulting quantities. It verifies the response market and time range, refuses a continuation cursor, checks that segments cover the request and emits BookGap instead of carrying state through missing intervals. HTTP 413 causes recursive subdivision; a version change aborts the walk. [Replay, lines 50–164](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/examples/track_historical_book.py#L50-L164).

The relevant mock-based tests cover a gap across calls, subdivision after HTTP 413 and rejection of a dataset-version change. Other tests distinguish an absent book from an empty book and a host-level 404 from a market-not-found response. These tests were read, not executed. [Tracker tests, lines 71–130](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/tests/test_history_tracker.py#L71-L130), [hosted tests, lines 71–127](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/tests/test_hosted.py#L71-L127).

## Boundaries that matter

- The inspected code calls a hosted archive; it does not establish the archive's first recorded date, retained market population, continuous coverage, quotas or availability for a new account. Documentation says coverage varies by market. Example timestamps are not a coverage manifest. [API contract, lines 3–60](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/docs/api.md#L3-L60).
- Recorder receipt is the provider's clock, not the downstream strategy's historical receipt. Record acquisition/publication provenance separately before making an as-of feature claim.
- Snapshot models expose floating-point prices and sizes. Deltas use exact strings and Decimal arithmetic in the tracker, but the documentation explicitly says this is not a lossless decimal archival format. [Precision boundary, line 25](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/docs/api.md#L25), [replay representation, lines 50–88](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/examples/track_historical_book.py#L50-L88).
- Displayed depth and observed trades support liquidity research; they do not identify personal queue position, acknowledgement latency, cancellations or passive fills for a proposed order.
- The Hyperliquid adapter in this review targets HIP-4 outcome markets, with limited recent prints; its presence does not imply a historical perpetual-futures archive. [Adapter, lines 598–634](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/synpath/hyperliquid.py#L598-L634), [book/trades, lines 778–846](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/synpath/hyperliquid.py#L778-L846).
- Matching returns a proposition link and side_map, without certifying identical settlement rules. Its matching computation is in the hosted service. [Matching, lines 1–23](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/synpath/matching.py#L1-L23), [link contract, lines 610–627](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/synpath/types.py#L610-L627).
- The MIT code license does not license the hosted dataset. The [service terms](https://www.synpath.dev/terms), consulted 2026-10-14, restrict hosted-data redistribution/resale without written permission and allow changing quotas/access. No data is redistributed in this review.

## Practical check

Before a replay, freeze the intended market/window set and verify coverage, response boundaries, dataset identity, event order and precision. Preserve raw responses and provider receipt times, then account for downstream availability. Evaluate queue and execution separately. A successful typed parse or a provider example is insufficient to certify the dataset.

## Account-state observation retained from the earlier review

The reconciler names orphan, ghost, drift, fill, position and balance differences. Orphan policy defaults to reporting. At this new commit, the earlier terminal-state caveat remains: when a journal-open order is absent from venue open orders and fetch_order fails, the fallback writes CANCELED locally. Recovery of fills and the timestamp-based cursor need separate completeness evidence; absence from the open-order set is insufficient to certify cancellation. [Orders, lines 128–181](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/synpath/engine/reconcile.py#L128-L181), [fills, lines 185–206](https://github.com/Synpath-ai/synpath/blob/a3e810fa749b10201083b531209011777eab21f0/synpath/engine/reconcile.py#L185-L206).

## Why this score

3/5 direct: useful history and reconciliation controls, with history test source inspected; a terminal-state fallback and unverified hosted coverage remain material limits. The rating is unchanged; evidence depth increases from 2/3 to 3/3 because relevant historical-client tests were read.

**Scope:** README, license, API/capability docs, historical and hosted clients, matching contracts, replay example and relevant tests; the complete reconciliation module and limited outcome-adapter/type excerpts. No installation, upstream execution, authenticated archive query, backend audit, security audit or profitability claim.


## Update history

2026-10-14: expanded the existing review from reconciliation alone to historical replay and missing-evidence handling at a3e810fa749b10201083b531209011777eab21f0. The earlier cancellation caveat was rechecked and retained. This updates one catalog entry; it does not add a second review or count the repository twice.
