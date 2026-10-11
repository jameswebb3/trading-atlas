# ChemInformant: What if a source name resolves to several records or a batch lookup partly fails?

**Decision question:** What if a source name resolves to several records or a batch lookup partly fails?

| Field | Review |
| --- | --- |
| Upstream | [HzaCode/ChemInformant](https://github.com/HzaCode/ChemInformant) |
| Primary area | Data Quality & Lineage |
| Source commit | [1389de5f86a9937748f241667d63385a637b8dc9](https://github.com/HzaCode/ChemInformant/commit/1389de5f86a9937748f241667d63385a637b8dc9) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/HzaCode/ChemInformant/blob/1389de5f86a9937748f241667d63385a637b8dc9/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The resolver raises AmbiguousIdentifierError when a name maps to multiple IDs. The batch API writes input_identifier, resolved ID and status for every requested item; the object API raises typed errors instead of flattening them into a DataFrame status. The HTTP layer caches 200, 404 and 503, but explicitly evicts cached 503 before retry. A cached 404 can remain a negative answer until expiry. The repository targets chemical data, so identity rules and cache freshness need adaptation to market symbols and exchange metadata. |

## What this project does

Resolves a name to one stable identifier or raises a typed ambiguity error; batch results retain a status per input. Useful for instrument and entity resolution in data ingestion, with a cache policy that must be evaluated for changing sources.

## Mechanism inspected

The resolver raises AmbiguousIdentifierError when a name maps to multiple IDs. The batch API writes input_identifier, resolved ID and status for every requested item; the object API raises typed errors instead of flattening them into a DataFrame status. The HTTP layer caches 200, 404 and 503, but explicitly evicts cached 503 before retry.

## Limitation that matters

A cached 404 can remain a negative answer until expiry. The repository targets chemical data, so identity rules and cache freshness need adaptation to market symbols and exchange metadata.

## Practical check for a trading system

For market or event aliases, require an unambiguous canonical ID and retain the original input and status. Test partial batches, new listings after cached 404, and source error versus true absence.

## Why this score

3/5 transferable: explicit ambiguity and per-row status prevent silent joins to the wrong entity, but the PubChem implementation and its cache choices are not a market-data collector.

## Source trail

[README.md](https://github.com/HzaCode/ChemInformant/blob/1389de5f86a9937748f241667d63385a637b8dc9/README.md#L78); [src/ChemInformant/cheminfo_api.py](https://github.com/HzaCode/ChemInformant/blob/1389de5f86a9937748f241667d63385a637b8dc9/src/ChemInformant/cheminfo_api.py#L33); [src/ChemInformant/cheminfo_api.py](https://github.com/HzaCode/ChemInformant/blob/1389de5f86a9937748f241667d63385a637b8dc9/src/ChemInformant/cheminfo_api.py#L190); [src/ChemInformant/api_helpers.py](https://github.com/HzaCode/ChemInformant/blob/1389de5f86a9937748f241667d63385a637b8dc9/src/ChemInformant/api_helpers.py#L60); [src/ChemInformant/api_helpers.py](https://github.com/HzaCode/ChemInformant/blob/1389de5f86a9937748f241667d63385a637b8dc9/src/ChemInformant/api_helpers.py#L135)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
