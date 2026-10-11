# Real-Time Crypto Flow - Can a stream repair missing trades without confusing backfill with live data?

**Decision question:** Can a stream repair missing trades without confusing backfill with live data?

| Field | Review |
| --- | --- |
| Upstream | [omerfeyzioglu/real-time-crypto-flow](https://github.com/omerfeyzioglu/real-time-crypto-flow) |
| Primary area | Market Data & Ingestion |
| Source commit | [9c829114f701232cb72bfd2369a554362da18110](https://github.com/omerfeyzioglu/real-time-crypto-flow/commit/9c829114f701232cb72bfd2369a554362da18110) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Repairs bounded trade-ID gaps and tags replayed rows so backfill does not trigger another gap cycle. Large gaps are skipped rather than repaired, and destination completeness must be checked separately. |

## What this project does

A Binance aggregate-trade pipeline that detects per-symbol ID gaps, backfills bounded ranges and validates the destination.

## Mechanism inspected

The consumer detects jumps in aggregate-trade IDs, requests a bounded missing range, republishes recovered rows with a source=backfill header and bypasses recursive gap detection for those rows. A separate SQL check reports missing IDs.

## Limitation that matters

Gaps over the configured size are logged and skipped, so the pipeline can remain incomplete. The README also states the write buffer is unbounded during database outages and has little fault-injection testing.

## Practical check for a trading system

Persist unresolved ranges and replay provenance, then block consumers on completeness rather than assuming a live stream is whole.

## Why this score

3/5 because A useful direct repair pattern is visible, but large skipped ranges and outage buffering are material reliability limits.

## Source trail

[README](https://github.com/omerfeyzioglu/real-time-crypto-flow/blob/9c829114f701232cb72bfd2369a554362da18110/README.md#L93); [pipeline/crypto/consumer.py](https://github.com/omerfeyzioglu/real-time-crypto-flow/blob/9c829114f701232cb72bfd2369a554362da18110/pipeline/crypto/consumer.py#L54); [pipeline/crypto/consumer.py](https://github.com/omerfeyzioglu/real-time-crypto-flow/blob/9c829114f701232cb72bfd2369a554362da18110/pipeline/crypto/consumer.py#L67); [platform/airflow-plugins/sql/gap_detection.sql](https://github.com/omerfeyzioglu/real-time-crypto-flow/blob/9c829114f701232cb72bfd2369a554362da18110/platform/airflow-plugins/sql/gap_detection.sql#L1); [README limitation](https://github.com/omerfeyzioglu/real-time-crypto-flow/blob/9c829114f701232cb72bfd2369a554362da18110/README.md#L344).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
