# CmdInterface - Do per-file hashes actually identify each input file independently?

**Decision question:** Do per-file hashes actually identify each input file independently?

| Field | Review |
| --- | --- |
| Upstream | [MIC-DKFZ/cmdint](https://github.com/MIC-DKFZ/cmdint) |
| Primary area | Research & Reproducibility |
| Source commit | [3cb762c65499336d39810e5a8dce9662ad4d62b7](https://github.com/MIC-DKFZ/cmdint/commit/3cb762c65499336d39810e5a8dce9662ad4d62b7) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The file-hashing method initializes one MD5 object before looping over all files and appends its digest after each file. Later digests include prior file bytes, so they are cumulative and cannot identify each file in isolation. |

## What this project does

A workflow wrapper that logs file and Git provenance.

## Mechanism inspected

The file-hashing method initializes one MD5 object before looping over all files and appends its digest after each file.

## Limitation that matters

Later digests include prior file bytes, so they are cumulative and cannot identify each file in isolation.

## Practical check for a trading system

Create a fresh digest per file and verify against independently recomputed hashes.

## Why this score

2/5. The provenance intent is valuable; the inspected hash loop is an instructive counterexample.

## Source trail

[README](https://github.com/MIC-DKFZ/cmdint/blob/3cb762c65499336d39810e5a8dce9662ad4d62b7/Readme.md#L1); [cmdint/CmdInterface.py](https://github.com/MIC-DKFZ/cmdint/blob/3cb762c65499336d39810e5a8dce9662ad4d62b7/cmdint/CmdInterface.py#L448); [cmdint/CmdInterface.py](https://github.com/MIC-DKFZ/cmdint/blob/3cb762c65499336d39810e5a8dce9662ad4d62b7/cmdint/CmdInterface.py#L470); [Root license](https://github.com/MIC-DKFZ/cmdint/blob/3cb762c65499336d39810e5a8dce9662ad4d62b7/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
