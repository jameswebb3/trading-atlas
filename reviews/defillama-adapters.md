# DefiLlama TVL Adapters: a metric is an accounting rule

**Decision question:** Which accounting choices turn raw protocol balances into a TVL metric?

| Field | Review |
| --- | --- |
| Upstream | [DefiLlama TVL Adapters](https://github.com/DefiLlama/DefiLlama-Adapters) |
| Primary area | Data Quality & Lineage |
| Source commit | [d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4](https://github.com/DefiLlama/DefiLlama-Adapters/commit/d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4) |
| Reviewed | 2026-09-26 |
| Declared license | [ISC declared in package.json; no root license text](https://github.com/DefiLlama/DefiLlama-Adapters/blob/d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4/package.json) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Makes TVL accounting inspectable: the Aave helper separates locked balances from borrowed debt and applies configured exclusions. Useful for understanding a metric's denominator and scope. |

## Project overview

Repository of protocol-specific TVL calculations. Its adapters expose the contract addresses, balance queries, exclusions, and lending-accounting choices behind an aggregate DeFi metric. [Project documentation](https://github.com/DefiLlama/DefiLlama-Adapters/blob/d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4/README.md#L7-L12).

## Mechanism worth inspecting

[The lending methodology](https://github.com/DefiLlama/DefiLlama-Adapters/blob/d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4/projects/helper/methodologies.js#L1-L3) defines TVL using locked collateral and excludes borrowed coins to avoid inflation through recycled lending. [The Aave V3 helper](https://github.com/DefiLlama/DefiLlama-Adapters/blob/d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4/projects/helper/aave.js#L345-L410) queries reserves, separates borrowed debt from tokens held by aTokens, and subtracts configured lender balances. [The adapter configuration](https://github.com/DefiLlama/DefiLlama-Adapters/blob/d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4/projects/aave-v3/index.js#L4-L23) supplies concrete token and lender exclusions.

The transferable lesson for a trading feature is to publish an accounting recipe beside the value: raw balances, inclusion/exclusion policy, chain/contract coverage, price source, and transformation version. Two metrics with the same name can have different economic meaning when these change.

## Important limit

[The README](https://github.com/DefiLlama/DefiLlama-Adapters/blob/d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4/README.md#L31-L48) allows historical timestamps and discusses archive-node access. That evaluates balances at a historical time with the selected code; it does not reproduce the adapter or classifications available to a past consumer. [The harness](https://github.com/DefiLlama/DefiLlama-Adapters/blob/d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4/test.js#L501-L538) skips missing/low-confidence or stale prices and converts balances to numbers for USD totals. These are validation-path observations, not proof that every production TVL pipeline uses the same path. [package.json](https://github.com/DefiLlama/DefiLlama-Adapters/blob/d47d1514ddfbcac4e4ad2a85479f86cb1642e8f4/package.json#L24-L28) declares ISC; no root LICENSE text was found in the inspected tree. The broad helper and SDK dependency surface also makes this more useful as a selective reference than a small standalone dependency.

## Questions to take into your own design

- Does each metric carry its adapter commit, exclusions, price coverage, and unpriced balances?
- Can a research vintage reproduce the classifications and methodology known at decision time?

## Why this score for a trading system

Inspecting protocol accounting and price omissions directly improves interpretation of on-chain trading inputs, but vintage reconstruction and licensing evidence are incomplete.

**Scope of this review:** README, lending-methodology text, Aave V3 configuration/helper, token-summing helper, package declaration, and price validation harness; only this lending path was inspected, not all protocol adapters or production TVL calculation.
