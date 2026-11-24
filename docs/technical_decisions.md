# Technical decisions

## Confirmed for Phase 01

- Python 3.11+ src-layout package with setuptools and editable installation. Python 3.14 is available locally. Core types use Pydantic v2. Safe YAML parsing rejects duplicate keys, schema extras and incompatible universe or workflow changes.
- Keep configuration in the checkout and pass its directory explicitly. The roster digest validates the normalized instructor triples independently of order. The original table order is preserved in the template. Dates are timezone-aware and normalized to UTC.
- Use typed missingness, dataset versions and a conservative historical access check. Historical archives require evidence for the exact vintage. A later phase must verify references and custody.
- Pytest and Ruff are development extras. SQLite is available in Python. Parquet and SQLite are proposed for versioned series and case logs respectively. Adopt Pandas, NumPy, SciPy, statsmodels, Parquet tooling, yfinance and FastMCP only when their owning phases need them.
- Deterministic research services sit inside provider, LLM, API and presentation adapters. Future OpenAI and Ollama adapters must satisfy the same interface. Phase 01 requires no external credentials, market access or model calls.
- Execution is educational and offline in this phase. Exact price prediction and ML are outside the initial plan.

## Open decisions

| Decision | Evidence or approval needed | Revisit |
|---|---|---|
| Historical dataset start date | Available coverage, corporate actions, membership history and release calendars | 02 |
| Fundamental data access method | Permitted Fintables access, historical statements and publication/vintage fidelity | 08 |
| Macroeconomic data provider access | Official channels, credentials if needed, revision histories, release granularity and terms | 03 |
| Instructor-approved video sources | Fixed approved channels/segments and permitted transcript retention | 09 |
| Exact macro regime classification rules | Reproducible hypotheses, separate domestic/global specifications and uncertainty treatment | 03 |
| Strategy entry and exit rules | Predeclared signals, confirmation windows, execution timing and validation design | 10 |
| Position sizing and risk constraints | Comparable exposure, cost/slippage and risk protocol for all variants | 10–11 |
| Factor scoring weights, if used | Economic rationale, sensitivity study and out-of-sample protocol | 10–11 |
| Frontend framework | Review/replay usability and read-model/API boundaries | 14 |
| Final LLM provider | Reproducibility, permitted access, measured cost/latency and privacy | 12–14 |

Also open are sector benchmark availability, historic peer membership, disclosure-time precision and licensed news coverage. Source gaps are reported explicitly. No numeric financial threshold or rate-to-regime rule has been selected.
