# pytest — expected failures need a retirement rule

**Decision question:** Should an unexpectedly passing known-failure test leave the suite green?

| Field | Review |
| --- | --- |
| Upstream | [pytest](https://github.com/pytest-dev/pytest) |
| Primary area | Testing & Verification |
| Source commit | [c333125d977b323fafbeb0e09cd86e203ab4af39](https://github.com/pytest-dev/pytest/commit/c333125d977b323fafbeb0e09cd86e203ab4af39) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/pytest-dev/pytest/blob/c333125d977b323fafbeb0e09cd86e203ab4af39/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Makes expected failure distinct from an ordinary pass. Strict XPASS can force review when a documented defect stops reproducing, while reasons, exception scope and skipped-test coverage remain application responsibilities. |

## Project overview

pytest is a test framework with assertion introspection and explicit skipped, expected-failure and unexpected-pass reporting. [Project documentation](https://github.com/pytest-dev/pytest/blob/c333125d977b323fafbeb0e09cd86e203ab4af39/README.rst#L46-L47).

## Mechanism worth inspecting

The xfail report path turns an unexpectedly passing call into a failed report when strict mode is enabled; without strict mode it reports a pass with xfail metadata. An expected failure can also be restricted to particular exceptions. [Report logic](https://github.com/pytest-dev/pytest/blob/c333125d977b323fafbeb0e09cd86e203ab4af39/src/_pytest/skipping.py#L288-L311); [strict behavior](https://github.com/pytest-dev/pytest/blob/c333125d977b323fafbeb0e09cd86e203ab4af39/doc/en/how-to/skipping.rst#L323-L331).

## Important limit

Strict XPASS catches stale expected-failure markers; it does not prove that the test exercises the intended failure. `run=False`, broad exception expectations and accidental skips need separate review. The inspected version resolves explicit marker strictness through configuration fallbacks. [Marker resolution](https://github.com/pytest-dev/pytest/blob/c333125d977b323fafbeb0e09cd86e203ab4af39/src/_pytest/skipping.py#L214-L238).

## Questions to take into your own design

- Does every known-failure marker have a reason, owner and specific expected failure?
- Do release-critical checks fail on unexpected pass and unexpected skip?

## Why this score for a trading system

3/5: a precise test-outcome contract that improves known-failure management, with application coverage and marker governance still required.

**Scope of this review:** xfail evaluation and report outcomes; not the complete pytest runner.
