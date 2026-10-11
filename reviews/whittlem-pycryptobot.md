# PyCryptoBot — Can a buy/sell report represent arbitrary position histories

**Decision question:** Can a buy/sell report represent arbitrary position histories?

| Field | Review |
| --- | --- |
| Upstream | [PyCryptoBot](https://github.com/whittlem/pycryptobot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [1fa9aaef141725623899230daa585e17fa7ba007](https://github.com/whittlem/pycryptobot/commit/1fa9aaef141725623899230daa585e17fa7ba007) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/whittlem/pycryptobot/blob/1fa9aaef141725623899230daa585e17fa7ba007/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Retrieves exchange orders and exports simple buy/sell trackers. Inspect how repeated entries and partial exits are allocated before using those reports as an accounting ledger. |

## Project overview

Python cryptocurrency bot with exchange account access, order exports and configurable market scanning. [Project documentation](https://github.com/whittlem/pycryptobot/blob/1fa9aaef141725623899230daa585e17fa7ba007/README.md#L1-L3).

## Mechanism worth inspecting

Account retrieval distinguishes live broker orders from local simulation records. The CSV tracker groups by market and builds buy/sell pairs from action transitions, while validating an exact column schema. [Retrieval](https://github.com/whittlem/pycryptobot/blob/1fa9aaef141725623899230daa585e17fa7ba007/models/TradingAccount.py#L84-L127), [tracker](https://github.com/whittlem/pycryptobot/blob/1fa9aaef141725623899230daa585e17fa7ba007/models/TradingAccount.py#L917-L1008), [scanner docs](https://github.com/whittlem/pycryptobot/blob/1fa9aaef141725623899230daa585e17fa7ba007/docs/TelegramBotScanner.md#L13-L35).

## Important limit

Action-pair reporting does not establish lot-level allocation for multiple entries, partial exits or derivatives funding. The inspected account model holds base and quote balances; it is not a perpetual-margin accounting reference. [Balances](https://github.com/whittlem/pycryptobot/blob/1fa9aaef141725623899230daa585e17fa7ba007/models/TradingAccount.py#L32-L49).

## Questions to take into your own design

- Can a buy/sell report represent arbitrary position histories?
- Can the ledger allocate fills across multiple entries and partial exits without action-pair shortcuts?

## Why this score for a trading system

2/5: useful exchange-reporting caution, with spot-style balances and simplified pairing that limit its value for derivatives systems.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
