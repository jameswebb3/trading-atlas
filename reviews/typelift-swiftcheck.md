# SwiftCheck — Failures need source-location evidence

**Decision question:** What makes a randomly generated failure reproducible for its owner?

| Field | Review |
| --- | --- |
| Upstream | [typelift/SwiftCheck](https://github.com/typelift/SwiftCheck) |
| Primary area | Testing & Verification |
| Source commit | [7494bedfa42972431004a5d478dbf1fc2655e1e6](https://github.com/typelift/SwiftCheck/commit/7494bedfa42972431004a5d478dbf1fc2655e1e6) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/typelift/SwiftCheck/blob/7494bedfa42972431004a5d478dbf1fc2655e1e6/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The property wrapper records a name, file, line, and checker arguments when it runs through XCTest. File and line make a failure locatable, but replay also needs seed, generated value, and environment. |

## What this project does

A Swift property-testing library integrated with XCTest. [Project README](https://github.com/typelift/SwiftCheck/blob/7494bedfa42972431004a5d478dbf1fc2655e1e6/README.md#L18).

## Mechanism inspected

The property wrapper records a name, file, line, and checker arguments when it runs through XCTest. [Implementation](https://github.com/typelift/SwiftCheck/blob/7494bedfa42972431004a5d478dbf1fc2655e1e6/Sources/SwiftCheck/Check.swift#L45).

## Limitation that matters

File and line make a failure locatable, but replay also needs seed, generated value, and environment. Swift is outside the usual trading stack. This is a source review, not a runtime or security test.

## Practical check for a trading system

For any generated execution test, retain seed, minimal failing event sequence, source revision, and failure location.

## Why this score

The reporting convention transfers, but the implementation language and generic testing scope are distant.

## Source trail

[README](https://github.com/typelift/SwiftCheck/blob/7494bedfa42972431004a5d478dbf1fc2655e1e6/README.md#L18); [Implementation](https://github.com/typelift/SwiftCheck/blob/7494bedfa42972431004a5d478dbf1fc2655e1e6/Sources/SwiftCheck/Check.swift#L45) - [License](https://github.com/typelift/SwiftCheck/blob/7494bedfa42972431004a5d478dbf1fc2655e1e6/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
