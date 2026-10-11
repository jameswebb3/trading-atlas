# LangWatch - Secret redaction and leak detection have different size limits

**Decision question:** Can an oversized agent trace bypass either secret scrubbing or leak reporting?

| Field | Review |
| --- | --- |
| Upstream | [langwatch/langwatch](https://github.com/langwatch/langwatch) |
| Primary area | Operations & Observability |
| Source commit | [e683dd9ea52c148e7678b1c22202dbfea9f1eb9f](https://github.com/langwatch/langwatch/commit/e683dd9ea52c148e7678b1c22202dbfea9f1eb9f) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Redacts agent-trace secrets with layered rules and slices long text so the scrubber still processes oversized payloads. The companion detector returns no matches above its size limit, so empty detection results and successful redaction are not equivalent evidence. |

## What this project does

An LLM observability platform with in-process secret redaction and a separate secret detector. The reviewed code handles free-text agent traces.

## Mechanism inspected

Redaction uses vendor-shaped, contextual and entropy-based rules, slices oversized text at whitespace or safe lookahead boundaries, and scans every slice. Source tests include secrets in over-budget inputs and at slice boundaries. The detector shares the rule set for ordinary strings and reports matched spans.

## Limitation that matters

The detector returns an empty match list when text exceeds 250,000 characters, while redaction slices and scans such text. A large trace can therefore be scrubbed but reported as having no detected secrets by a caller relying on the detector. Regex and entropy rules can also miss novel credential shapes or over-redact identifiers. This is a source review, not a runtime or security test.

## Practical check for a trading system

For agent and trade logs, measure both redaction and detection coverage on long traces. Record whether each path scanned, skipped or truncated input; never treat an empty match list after a size guard as proof that no secret was present.

## Why this score

3/5 because source and tests demonstrate a transferable long-trace redaction pattern with a precise detector-size caveat relevant to agent audit logs.

## Source trail

[README](https://github.com/langwatch/langwatch/blob/e683dd9ea52c148e7678b1c22202dbfea9f1eb9f/README.md#L1); [Rule and size contract](https://github.com/langwatch/langwatch/blob/e683dd9ea52c148e7678b1c22202dbfea9f1eb9f/packages/redaction/src/secrets.ts#L35); [Oversized slicing](https://github.com/langwatch/langwatch/blob/e683dd9ea52c148e7678b1c22202dbfea9f1eb9f/packages/redaction/src/secrets.ts#L991); [Detector size guard](https://github.com/langwatch/langwatch/blob/e683dd9ea52c148e7678b1c22202dbfea9f1eb9f/packages/redaction/src/secrets.ts#L1171); [Oversized tests](https://github.com/langwatch/langwatch/blob/e683dd9ea52c148e7678b1c22202dbfea9f1eb9f/packages/redaction/src/__tests__/secrets.unit.test.ts#L161); [License](https://github.com/langwatch/langwatch/blob/e683dd9ea52c148e7678b1c22202dbfea9f1eb9f/LICENSE.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
