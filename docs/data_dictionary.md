# Foundation data dictionary

The fields below are implemented in `macroswing.core.contracts`. The final dictionary will also document units, transformations, parameters, sources and availability rules for each later structured feature, contextual tag and outcome.

| Contract or field | Meaning and constraints |
|---|---|
| StockIdentity.ticker, yahoo_symbol | BIST identity and matching Yahoo symbol with .IS suffix. The universe validator verifies the complete instructor roster. |
| SectorIdentity.label | Nonempty simplified sector label. The fixed map preserves exact spelling, case, spaces and punctuation from PDF §5. |
| AnalysisId | UUID for joining a research case, its evidence, decisions and replay. |
| SourceMetadata.provider, source_reference | Nonblank source name and traceable record, file or URL reference. |
| SourceMetadata.retrieved_at | RetrievalTimestamp for actual collection of this version. |
| DatasetMetadata.dataset_id, version, source | Dataset identity, nonempty version identifier and source snapshot metadata. Ingestion must resolve identifiers to immutable content. |
| Observation.observed_at | ObservationTimestamp for the realized event or end of the measured period. |
| Observation.published_at | PublicationTimestamp for this release or revision, nullable when unknown. A known publication cannot precede its observation. |
| Observation.available_at | AvailabilityTimestamp, earliest evidenced access to this exact version. Required for an available value. It follows or equals known publication/observation and cannot follow retrieval. |
| Observation.historical_vintage_reference | Reference documenting point-in-time access to this exact vintage. Required to use a later-retrieved record at an earlier decision cutoff. |
| AnalysisTimestamp | Decision cutoff passed to value_as_of. Equality with the availability instant is admitted. Execution timing is evaluated separately. |
| Observation.status | AVAILABLE, MISSING (expected observation absent), UNAVAILABLE (source inaccessible or availability cannot be established). |
| Observation.value, missing_reason | Typed payload for an available observation. Use null and a nonblank reason for both missing statuses. Zero is a valid measured value. |
| EducationalAction, HarnessState, RiskGateStatus | Distinct contracts for finite analytical output, ordered workflow and gate disposition. The exact values are transcribed in requirements.md. |
| MacroRegime | Proposed research labels EXPANSION, LATE_CYCLE, CONTRACTION, RECOVERY, UNCERTAIN. A label supplies no classification rule. |

Use timezone-aware instants. Contracts normalize offsets to UTC. For real observations the source retrieval cannot precede the observation or known publication/availability. Retain source timezone and release convention in future provider metadata where needed. For a new revision, create a new version with its own public release and availability. Never backdate it to the original period.

## Configuration ownership

| File | Authority and meaning |
|---|---|
| universe.yaml | PDF §5 fixes stock identity triples and membership revalidation. External comparisons and optional membership history are separate project fields. |
| market.yaml | Required index and market fields. Adapter selection is proposed. Dataset start date is unresolved. |
| macro.yaml | Domestic FX/rates/CPI and US policy measures come from §15. Two regime scopes and their labels are project proposals. |
| indicators.yaml | §7 indicator coverage without periods, thresholds or calibrated settings. |
| strategies.yaml | §29 variants. Entries, exits and weights remain open. |
| backtest.yaml | Reversal and catch-up windows are in trading sessions. Disclosure windows follow the worked example. Empty additional_days disables extensions; costs, slippage, sizing and risk constraints are unselected. |
| harness.yaml | Exact instructor workflow, educational actions and gate statuses. Permissions and execution arrive in Phase 13. |

Future dated membership records must distinguish constituent status for an analysis date, effective dates of index changes, publication date and source, including unknown status. External sector benchmarks and peers have their own references and sector mapping. They supply comparison evidence only.
