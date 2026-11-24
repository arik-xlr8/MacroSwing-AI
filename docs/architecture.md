# System architecture

Phase 01 implements the package, configuration and contracts in `core`. Other packages reserve import paths. The following design describes the eventual system.

| Layer | Owner | Data boundary and responsibility |
|---|---|---|
| 1. Data acquisition | data_sources | Provider adapters acquire permitted source snapshots for prices, statements, macro, news and speech. Emit version references, retrieval times and access failures. |
| 2. Storage and quality | data_sources, market, core, risk | Preserve immutable raw inputs, normalize instrument IDs, sessions, UTC timestamps and publication calendars. Cache by provider, query and version. Materialize validated series and quality diagnostics. |
| 3. Deterministic financial research | market, macro, sector, technical, patterns, fundamentals, news, speech | Transform as-of snapshots into typed market, macro, fundamental, calendar, reversal and contextual records. Technical owns indicators and event detection. Patterns owns calendar sequences. Sector owns peers/ranks. Time-align each output and preserve lineage. |
| 4. Swing strategies | strategies | Assemble permitted A–E rule specifications and candidate states from features admissible at the decision time. Store the rule version. |
| 5. Historical verification | backtesting | Apply shifted signals, declared fills, costs, risk and comparable benchmarks. Score later outcomes in an evaluation-only dataset. Return run metadata, metrics and event/trade logs. |
| 6. Agentic AI | mcp_server, agents, harness | MCP adapters call deterministic services through schemas. Specialists interpret outputs via a provider-independent language-model interface. Harness owns transitions and state-specific permissions. |
| 7. Evidence and governance | evidence, risk, memory, harness | Build full and committed evidence, apply quality/verification gates, persist state histories and require human review. Link reviewed conclusions back to source versions, tool outputs and decisions. |
| 8. Presentation | future dashboard and API | Read verified results, warnings, evidence citations, revision history and review status. Transport and frontend choices are open. |

## Dependencies and execution

Data flows from authorized snapshots through as-of selection and deterministic features into rule previews and historical verification. Agents consume structured responses; the harness carries the analysis ID through every state. Committed evidence, gate decisions, reviewer rationale and tool logs form a replayable record.

Imports point inward. Core contracts depend on Pydantic and the standard library. The configuration loader depends on contracts and PyYAML. Acquisition, research, evidence, risk and memory services accept typed inputs and return values. Strategies consume feature records. Backtesting consumes strategy specifications and segregated outcome data. MCP adapters depend on service APIs. Agents use a tool client interface. The harness composes tool access, agents, evidence, gates and persistence at the application boundary. Frontend/API adapters depend on application read models. Inner modules never import the harness, provider-specific LLM clients or presentation. Wire services in the outer application to avoid cycles between agents and the harness.

## State and evidence lifecycle

The exact 17 steps from START through LOG_AND_CLOSE are declared in the [requirements matrix](requirements.md) and validated in harness.yaml. Macroeconomic reasoning can be top-down when interpreting a complete bundle. Loading and validation follow §23, including CHECK_DATA_QUALITY before technicals, RUN_BACKTEST after strategy preview and RISK_GATE before explanation. Each state will have a tool allowlist under harness control. Blocked cases record diagnostics and their terminal disposition without producing an approved conclusion. Exact failure and retry transitions require Phase 13 design.

All verified facts carry immutable source and tool references. News and speech claims require deterministic checks before numerical use. Persist the observed bundle, the subset used, strategy and run IDs, warnings, human response and reason. Temporal storage holds dated observations; episodic storage holds case histories; procedural storage versions state order, rules, permissions and templates. Replay reads recorded versions, including model outputs, without requiring a fresh stochastic explanation.

## Contracts at the historical boundary

A fiscal period end describes what a statement measures. Publication, version availability and retrieval establish when it can support a decision. Every later service must obtain values via as-of selection and validate vintage provenance. A later archive retrieval requires a dated reference to the exact vintage to qualify for historical use. When only a date is known, adapters must resolve a defensible availability instant or mark the data unavailable. Outcome labels belong only to historical verification. Schema validation alone cannot authenticate a source or enforce the future harness.

## Strategy and experiment design

The strategy hierarchy is cumulative: A uses technicals; B adds sector relative strength; C adds point-in-time fundamentals; D adds global/Turkish macro context; E adds verified news/speech. D and E carry the proposed macro-aware swing extensions. Keep entry/exit, scoring, position sizing, execution time and transaction assumptions versioned and explicit. Freeze shared comparisons and disclose common-coverage exclusions. Isolate calendar and reversal feature families for ablation. The separate harness experiment A–E changes tool access, state enforcement, evidence, quality gates, memory and review on matched cases. Experimental raw-LLM outputs are quarantined for scoring and cannot enter the educational decision path.
