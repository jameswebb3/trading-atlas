# Finta — Indicator names do not fix initialization

**Decision question:** Does an EMA period fully specify the indicator?

| Field | Review |
| --- | --- |
| Upstream | [Finta](https://github.com/peerchemist/finta) |
| Primary area | Signals & Models |
| Source commit | [af01fa594995de78f5ada5c336e61cd87c46b151](https://github.com/peerchemist/finta/commit/af01fa594995de78f5ada5c336e61cd87c46b151) |
| Reviewed | 2026-09-27 |
| Declared license | [LGPL-3.0](https://github.com/peerchemist/finta/blob/af01fa594995de78f5ada5c336e61cd87c46b151/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The EMA path calls Pandas ewm with adjust=True by default. Adjusted weighted history is not the same initialization contract as every recursive online EMA. |

## Project overview

Pandas implementations of financial technical indicators. [Documentation](https://github.com/peerchemist/finta/blob/af01fa594995de78f5ada5c336e61cd87c46b151/README.md).

## Mechanism worth inspecting

The EMA path calls Pandas ewm with adjust=True by default. Input validation checks required column names; the moving-average methods choose different warm-up policies. [Source](https://github.com/peerchemist/finta/blob/af01fa594995de78f5ada5c336e61cd87c46b151/finta/finta.py#L7-L124).

## Important limit

Adjusted weighted history is not the same initialization contract as every recursive online EMA. Column presence alone also does not prove finite or complete observations. [Evidence 1](https://github.com/peerchemist/finta/blob/af01fa594995de78f5ada5c336e61cd87c46b151/finta/finta.py#L7-L124). [Evidence 2](https://github.com/peerchemist/finta/blob/af01fa594995de78f5ada5c336e61cd87c46b151/README.md#L13-L18).

## Questions to take into your own design

- Do replay and streaming use the same seed, adjust flag and warm-up?
- What happens after an initial gap or nonfinite input?

## Why this score for a trading system

Direct feature-equivalence questions at inspectable formulas; indicator count and names are not evidence of new alpha.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
