# mozaiks - Track scorer errors separately from pass rate

**Decision question:** Can a review look better because scorers stopped working?

| Field | Review |
| --- | --- |
| Upstream | [BlocUnited-LLC/mozaiks](https://github.com/BlocUnited-LLC/mozaiks) |
| Primary area | Testing & Verification |
| Source commit | [dfc067d8c1e04502ed831215eb955abd973069d6](https://github.com/BlocUnited-LLC/mozaiks/commit/dfc067d8c1e04502ed831215eb955abd973069d6) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/BlocUnited-LLC/mozaiks/blob/dfc067d8c1e04502ed831215eb955abd973069d6/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | For each scorer it counts passed, failed and errored results, saves a JSON run, and compares runs by bundle ID. Its pass rate divides by passed plus failed and excludes errored. A comparison can look better if error cases disappear from that denominator. |

## What this project does

Mozaiks evaluates a fixed corpus of generated app bundles and stores versioned run results. [README](https://github.com/BlocUnited-LLC/mozaiks/blob/dfc067d8c1e04502ed831215eb955abd973069d6/README.md).

## Mechanism inspected

For each scorer it counts passed, failed and errored results, saves a JSON run, and compares runs by bundle ID. [Implementation](https://github.com/BlocUnited-LLC/mozaiks/blob/dfc067d8c1e04502ed831215eb955abd973069d6/factory_app/eval/bundle_eval.py#L23-L54). [Related path](https://github.com/BlocUnited-LLC/mozaiks/blob/dfc067d8c1e04502ed831215eb955abd973069d6/factory_app/eval/bundle_eval.py#L107-L145).

## Limitation that matters

Its pass rate divides by passed plus failed and excludes errored. A comparison can look better if error cases disappear from that denominator. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Report planned, graded and errored counts together and block a trading research verdict when a required scorer errors.

## Why this score

The corpus and run diff are useful references; the denominator rule must be tightened before use in financial research.

## Source trail

[README](https://github.com/BlocUnited-LLC/mozaiks/blob/dfc067d8c1e04502ed831215eb955abd973069d6/README.md) - [Implementation](https://github.com/BlocUnited-LLC/mozaiks/blob/dfc067d8c1e04502ed831215eb955abd973069d6/factory_app/eval/bundle_eval.py#L23-L54) - [Related path](https://github.com/BlocUnited-LLC/mozaiks/blob/dfc067d8c1e04502ed831215eb955abd973069d6/factory_app/eval/bundle_eval.py#L107-L145) - [License](https://github.com/BlocUnited-LLC/mozaiks/blob/dfc067d8c1e04502ed831215eb955abd973069d6/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
