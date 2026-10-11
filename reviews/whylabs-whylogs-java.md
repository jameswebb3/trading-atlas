# whylogs-java — Mergeable column profiles are a compact comparison, not provenance

**Decision question:** Can a compact data profile reveal feed drift without hiding identity mismatches?

| Field | Review |
| --- | --- |
| Upstream | [whylabs/whylogs-java](https://github.com/whylabs/whylogs-java) |
| Primary area | Data Quality & Lineage |
| Source commit | [24933f19aa31fae192e5eaa2fa39b641577c5e87](https://github.com/whylabs/whylogs-java/commit/24933f19aa31fae192e5eaa2fa39b641577c5e87) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/whylabs/whylogs-java/blob/24933f19aa31fae192e5eaa2fa39b641577c5e87/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | ColumnProfile.merge checks matching column names by default, then merges counters, number and schema trackers, cardinality sketches and frequent-item sketches. A caller can disable the name check; sketches are approximate and the profile has no event-time or publication-time contract. |

## What this project does

Java implementation of mergeable statistical profiles for datasets and columns. [README](https://github.com/whylabs/whylogs-java/blob/24933f19aa31fae192e5eaa2fa39b641577c5e87/README.md).

## Mechanism inspected

ColumnProfile.merge checks matching column names by default, then merges counters, number and schema trackers, cardinality sketches and frequent-item sketches. [Implementation](https://github.com/whylabs/whylogs-java/blob/24933f19aa31fae192e5eaa2fa39b641577c5e87/core/src/main/java/com/whylogs/core/ColumnProfile.java#L140-L195).

## Limitation that matters

A caller can disable the name check; sketches are approximate and the profile has no event-time or publication-time contract. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Compare profiles only after enforcing feed identity, window, count and available_at; retain raw samples for incident reconstruction.

## Why this score

ColumnProfile.merge checks matching column names by default, then merges counters, number and schema trackers, cardinality sketches and frequent-item sketches. A caller can disable the name check; sketches are approximate and the profile has no event-time or publication-time contract.

## Source trail

[README](https://github.com/whylabs/whylogs-java/blob/24933f19aa31fae192e5eaa2fa39b641577c5e87/README.md) · [Implementation](https://github.com/whylabs/whylogs-java/blob/24933f19aa31fae192e5eaa2fa39b641577c5e87/core/src/main/java/com/whylogs/core/ColumnProfile.java#L140-L195) · [License](https://github.com/whylabs/whylogs-java/blob/24933f19aa31fae192e5eaa2fa39b641577c5e87/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
