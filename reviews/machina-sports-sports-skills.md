# Sports Skills: Can an offline replay prove what a provider actually returned?

**Decision question:** Can an offline replay prove what a provider actually returned?

| Field | Review |
| --- | --- |
| Upstream | [machina-sports/sports-skills](https://github.com/machina-sports/sports-skills) |
| Primary area | Market Data & Ingestion |
| Source commit | [0420a7ca09ef5116167309821816a68853fc516e](https://github.com/machina-sports/sports-skills/commit/0420a7ca09ef5116167309821816a68853fc516e) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/machina-sports/sports-skills/blob/0420a7ca09ef5116167309821816a68853fc516e/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Record, replay and fill modes use a required replay directory. Pure replay never invokes the live loader; a missing or corrupt entry returns an error. DataFrame recording compares restored columns and index to the original and saves a sidecar with provider version and inexact columns. The metadata connector rejects loosely matched team names. Recordings only prove the captured provider response at a particular request; they do not prove the provider was complete, timely or legally redistributable. The repository's sports identity rules are domain-specific and should not be transplanted to symbols without a venue-specific contract. |

## What this project does

Records upstream responses under normalized request keys, refuses network access on replay misses, verifies stored-entry integrity and marks DataFrame columns that fail exact round-trip. A useful ingestion test pattern; provider terms still govern recorded data.

## Mechanism inspected

Record, replay and fill modes use a required replay directory. Pure replay never invokes the live loader; a missing or corrupt entry returns an error. DataFrame recording compares restored columns and index to the original and saves a sidecar with provider version and inexact columns. The metadata connector rejects loosely matched team names.

## Limitation that matters

Recordings only prove the captured provider response at a particular request; they do not prove the provider was complete, timely or legally redistributable. The repository's sports identity rules are domain-specific and should not be transplanted to symbols without a venue-specific contract.

## Practical check for a trading system

For market-feed regression tests, bind each fixture to normalized request, provider/version, receipt time, checksum and exactness flags. In offline mode, reject any unrecorded request instead of silently fetching live.

## Why this score

3/5 transferable: strict offline replay and exactness flags are strong data-lineage patterns, while the sport connectors and provider rights require adaptation.

## Source trail

[README.md](https://github.com/machina-sports/sports-skills/blob/0420a7ca09ef5116167309821816a68853fc516e/README.md#L1); [src/sports_skills/_replay.py](https://github.com/machina-sports/sports-skills/blob/0420a7ca09ef5116167309821816a68853fc516e/src/sports_skills/_replay.py#L1); [src/sports_skills/_replay.py](https://github.com/machina-sports/sports-skills/blob/0420a7ca09ef5116167309821816a68853fc516e/src/sports_skills/_replay.py#L191); [src/sports_skills/_replay.py](https://github.com/machina-sports/sports-skills/blob/0420a7ca09ef5116167309821816a68853fc516e/src/sports_skills/_replay.py#L319); [src/sports_skills/metadata/_connector.py](https://github.com/machina-sports/sports-skills/blob/0420a7ca09ef5116167309821816a68853fc516e/src/sports_skills/metadata/_connector.py#L280); [docs/provider-attested-operations.md](https://github.com/machina-sports/sports-skills/blob/0420a7ca09ef5116167309821816a68853fc516e/docs/provider-attested-operations.md#L1)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
