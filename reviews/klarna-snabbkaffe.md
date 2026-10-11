# Snabbkaffe — Trace checks distinguish coverage from causality

**Decision question:** Does every intended effect have the required event evidence?

| Field | Review |
| --- | --- |
| Upstream | [Snabbkaffe](https://github.com/klarna/snabbkaffe) |
| Primary area | Testing & Verification |
| Source commit | [2bdf6e842c825ca935b34884528f51158dd31e6e](https://github.com/klarna/snabbkaffe/commit/2bdf6e842c825ca935b34884528f51158dd31e6e) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/klarna/snabbkaffe/blob/2bdf6e842c825ca935b34884528f51158dd31e6e/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Trace assertions pair causes and effects, optionally require an effect for every cause, check uniqueness after removing timestamps, and compare projected events with an expected set. The assertions can only see emitted trace points and the supplied matching rule. |

## Project overview

Erlang trace-based testing library separating program execution from assertions over collected events. [Documentation](https://github.com/klarna/snabbkaffe/blob/2bdf6e842c825ca935b34884528f51158dd31e6e/README.org).

## Mechanism worth inspecting

Trace assertions pair causes and effects, optionally require an effect for every cause, check uniqueness after removing timestamps, and compare projected events with an expected set. [Source](https://github.com/klarna/snabbkaffe/blob/2bdf6e842c825ca935b34884528f51158dd31e6e/src/snabbkaffe.erl#L423-L465).

## Important limit

The assertions can only see emitted trace points and the supplied matching rule. A missing instrumentation event is different from a demonstrated missing exchange effect. [Evidence 1](https://github.com/klarna/snabbkaffe/blob/2bdf6e842c825ca935b34884528f51158dd31e6e/src/snabbkaffe.erl#L423-L465). [Evidence 2](https://github.com/klarna/snabbkaffe/blob/2bdf6e842c825ca935b34884528f51158dd31e6e/README.org#L7-L15).

## Questions to take into your own design

- Is the expected event set checked before interpreting a causal assertion?
- Does matching use stable operation identity rather than timestamps alone?

## Why this score for a trading system

Concrete event-evidence assertions for execution tests; adding Erlang instrumentation to the trading service is unnecessary.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
