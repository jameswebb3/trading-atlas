# nyaggle — Time windows need a purge rule

**Decision question:** Are train and test rows separated by the information horizon?

| Field | Review |
| --- | --- |
| Upstream | [nyaggle](https://github.com/nyanp/nyaggle) |
| Primary area | Backtesting & Simulation |
| Source commit | [636532292d7ce3468cd47a3337bc50d620f0d23b](https://github.com/nyanp/nyaggle/commit/636532292d7ce3468cd47a3337bc50d620f0d23b) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/nyanp/nyaggle/blob/636532292d7ce3468cd47a3337bc50d620f0d23b/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Its splitter selects rows by half-open timestamp intervals and yields train/test indices. The shown path ignores groups and has no label-horizon purge or available_at check; adjacent windows can still leak future information. |

## What this project does

A competition-oriented ML utility library with configurable time-series splitters. [README](https://github.com/nyanp/nyaggle/blob/636532292d7ce3468cd47a3337bc50d620f0d23b/README.md).

## Mechanism inspected

Its splitter selects rows by half-open timestamp intervals and yields train/test indices. [Implementation](https://github.com/nyanp/nyaggle/blob/636532292d7ce3468cd47a3337bc50d620f0d23b/nyaggle/validation/split.py#L236-L286).

## Limitation that matters

The shown path ignores groups and has no label-horizon purge or available_at check; adjacent windows can still leak future information. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Add a fixture where a label ending after test start is purged despite a training timestamp before the boundary.

## Why this score

Direct trading-system relevance: Its splitter selects rows by half-open timestamp intervals and yields train/test indices. The shown path ignores groups and has no label-horizon purge or available_at check; adjacent windows can still leak future information.

## Source trail

[README](https://github.com/nyanp/nyaggle/blob/636532292d7ce3468cd47a3337bc50d620f0d23b/README.md) · [Documentation](https://github.com/nyanp/nyaggle/blob/636532292d7ce3468cd47a3337bc50d620f0d23b/docs/source/reference/util.rst) · [Implementation](https://github.com/nyanp/nyaggle/blob/636532292d7ce3468cd47a3337bc50d620f0d23b/nyaggle/validation/split.py#L236-L286).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
