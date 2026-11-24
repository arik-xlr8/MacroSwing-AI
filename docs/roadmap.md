# Controlled development roadmap

Only Phase 01 is authorized. Dependencies below are inputs to later work. Each future phase requires its own authorization; a successful foundation test does not verify any financial result.

## 01 — Project Foundation

- **Objective and expected implementation.** Package the offline contracts and seven configuration files, document all requirements and phase ownership, initialize Git and preserve the source PDF.
- **Dependencies.** Assignment PDF and Phase 01 authorization.
- **Acceptance.** Install editable in a clean environment, import from outside the checkout, reproduce all 30 PDF rows, reject invalid identities, timestamps and workflow configuration.
- **Required tests.** Package/import independence, config success/failure, roster, enums, core types, missing values and historical cutoff.
- **Traceability.** M01, M02, M03, M22, M28, X01.

## 02 — Market Data Pipeline

- **Objective and expected implementation.** Build market/index/peer adapters, version raw and adjusted prices, validate calendar, membership by date and provenance. Record unknown history explicitly.
- **Dependencies.** 01, source terms and availability, research-period choice for a production dataset.
- **Acceptance.** Rebuild an identified dataset version from documented inputs, report missing coverage and current versus historical membership, preserve the frozen 30.
- **Required tests.** Fixtures for split adjustments, non-trading days, duplicates, missing symbols, stale data and membership changes. Verify repeatable snapshots.
- **Traceability.** M03, M04, R05, X04.

## 03 — Macro Regime Engine

- **Objective and expected implementation.** Align domestic FX, rates and CPI and global Fed series by vintage. Develop separate Turkish/global regime specifications after rules are approved. Evaluate optional additional official series.
- **Dependencies.** 01–02, dated macro sources and release calendars.
- **Acceptance.** Every feature carries release and availability times, revisions are identifiable, ambiguity can yield UNCERTAIN and both contexts can be evaluated separately.
- **Required tests.** Late releases, revision leakage, gaps, regime ambiguity and independent domestic/global state.
- **Traceability.** M05, M06, O01, X02, X03.

## 04 — Technical Analysis Engine

- **Objective and expected implementation.** Implement mandatory indicators, raw-to-feature transforms, support/resistance and activity confirmation as deterministic functions.
- **Dependencies.** 01–02 and aligned price histories.
- **Acceptance.** Reproducible indicators carry periods, parameters and warm-up status, with historical features invariant under future data changes.
- **Required tests.** Known numerical examples, flat prices, gaps, zero volume, warm-up and prefix invariance.
- **Traceability.** M07, M08.

## 05 — Sector Rotation Engine

- **Objective and expected implementation.** Build dated peer groups and benchmark definitions, compute relative windows/ranks, and identify candidate laggards. Defer fundamental filtering and full strategy verification to 08–11.
- **Dependencies.** 01–02, with technical and macro context from 03–04 when available.
- **Acceptance.** Rank peers and emit subsequent 5/10/20-session relative outcomes separately from decision-time features. Flag or withhold underpowered groups.
- **Required tests.** Small/singleton sectors, changing membership, ties, external peers, no self-benchmark artifact and outcome isolation.
- **Traceability.** M09, M10, M37, X04.

## 06 — Calendar Pattern Engine

- **Objective and expected implementation.** Generate weekday and session-sequence labels, count occurrences, construct unconditional/random comparisons and plan held-out tests before inspecting outcomes.
- **Dependencies.** 02, with regime and technical inputs from 03–04.
- **Acceptance.** Report conditional means/medians, sample counts and multiple-testing exposure by period, stock/sector and regime. Supply events for cost-adjusted verification in 11.
- **Required tests.** Holiday-shortened weeks, missing sessions, boundary-crossing labels, independent baseline and held-out partition.
- **Traceability.** M11, M37, R03.

## 07 — Technical Reversal Engine

- **Objective and expected implementation.** Build timestamped events for all eight required reversal families and attach separately matured outcomes. Compare single and combined conditions.
- **Dependencies.** 02 and 04, with regime inputs from 03.
- **Acceptance.** Report touches, successes/failures, average/median strength and forward distributions at 1/3/5/10 sessions across index direction and volatility regimes.
- **Required tests.** Family-specific fixtures, delayed extrema confirmation, cloud displacement, overlapping events and incomplete forward windows.
- **Traceability.** M12, M13, M14, M15, M37, O02.

## 08 — Fundamental Analysis

- **Objective and expected implementation.** Version statements, compute sector-appropriate metrics and QoQ/YoY changes, align release dates and measure post-disclosure response.
- **Dependencies.** 01–02, legal Fintables access and dated disclosures, plus 04–05 for cross-layer comparisons.
- **Acceptance.** Each comparison uses the vintage available on the decision date. Report abnormal returns versus XU100 and sector at 1/5/20 sessions and identify conflicting technical evidence.
- **Required tests.** After-close disclosures, revisions, period mismatch, negative/zero denominators, missing quarters and banking ratios.
- **Traceability.** M05, M16, M17, M18, M37, R06.

## 09 — News and Speech Intelligence

- **Objective and expected implementation.** Store news metadata, segment-level speech provenance and timestamped topics, opinions, claims, stance and uncertainty. Link numerical claims to deterministic verification.
- **Dependencies.** 01–02, permitted news access, instructor-approved video list and usage terms.
- **Acceptance.** Return legally available context and segment references as of cutoff. Unverified numerical claims cannot be committed.
- **Required tests.** Late publications, duplicate articles, ambiguous speakers, transcript gaps, denied access and unsupported claims.
- **Traceability.** M19, M20, M21, O02.

## 10 — Swing Strategy Engine

- **Objective and expected implementation.** Define A–E as cumulative evidence variants and produce reproducible educational previews. Extend macro-aware swing hypotheses chiefly in D/E.
- **Dependencies.** 03–09 and specified entry/exit, sizing and risk rules.
- **Acceptance.** Preview each variant from the same as-of dataset. Constrain output to allowed actions and isolate calendar and reversal contributions.
- **Required tests.** Variant information boundaries, deterministic decisions, missing evidence, invalid actions and shared assumptions.
- **Traceability.** M10, M22, M23, O03, X02, X03, X05.

## 11 — Backtesting and Verification

- **Objective and expected implementation.** Evaluate the four scenarios and all strategies under common benchmarks, samples and rolling or held-out periods. Record trades/events and risk metrics.
- **Dependencies.** 02–10, explicit fill timing, cost, slippage and risk assumptions.
- **Acceptance.** Report mandatory metrics, distributions, false positives, cost-adjusted results, counts and regimes. Quantify incremental sector/macro/context effects and discuss uncertainty.
- **Required tests.** Signal shifting, costs/slippage, timing around releases, benchmark alignment, drawdowns, few/zero trades and holdout isolation.
- **Traceability.** M09, M10, M11, M15, M17, M18, M23, M24, M25, M26, R06, X02, X03, X05.

## 12 — MCP and AI Agents

- **Objective and expected implementation.** Expose the fifteen deterministic tools. Separate specialists and orchestration from services. Route LLM use through a provider-independent interface.
- **Dependencies.** 02–11, verified research outputs and provider access decision.
- **Acceptance.** Validate each tool schema and source lineage. Agent claims resolve to tool outputs. Use local test doubles to verify providers can be exchanged.
- **Required tests.** MCP request/response schemas, invalid arguments, unavailable tools, invented numerical claims and adapter substitution.
- **Traceability.** M02, M27, R01, R02, R05, X06, T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15.

## 13 — Stateful Harness, Evidence, Risk and Memory

- **Objective and expected implementation.** Implement the exact state machine, state-specific permissions, quality and risk gates, committed evidence, three memories, review, logging and replay.
- **Dependencies.** 11–12, typed vocabularies from 01.
- **Acceptance.** Block skipped states, future data and unsupported conclusions. A reviewer can modify/reject and replay traces using original versions and rationale.
- **Required tests.** Every legal transition, disallowed calls, all hard blocks and warnings, review outcomes, missing inputs, idempotent log closure and replay.
- **Traceability.** M02, M21, M22, M28, M29, M30, M31, M32, M33, M34, M35, R01, R02, R05.

## 14 — Dashboard and Academic Experiments

- **Objective and expected implementation.** Build a read-only educational presentation and compare five harness conditions on common cases, including failures. Report research and harness metrics separately.
- **Dependencies.** 11–13, matched experiment questions and a presentation choice.
- **Acceptance.** A reviewer can inspect evidence, gates and replay. Report all A–E harness results, quality, reproducibility, latency/cost and uncertainty alongside separate financial strategy comparisons.
- **Required tests.** UI/API boundary, matched cases, unsupported claims, metric denominators, replay consistency and restricted access to unverified baseline outputs.
- **Traceability.** M36, M37, R04, X05, X06.

## 15 — Final Delivery

- **Objective and expected implementation.** Assemble code/notebooks, installation guide, dictionary, all research reports, MCP/stateful harness, benchmarks, experiments, replay and class demonstration. Record optional ML disposition.
- **Dependencies.** 01–14 artifacts and reviewed results.
- **Acceptance.** Reproduce a documented analysis from pinned inputs, deliver every §36 artifact, address limitations, learning distinctions and educational framing.
- **Required tests.** Clean environment installation, full regression suite, trace every mandatory ID and demonstrate one reviewed replay and one safe failure.
- **Traceability.** M01, M38, M39, M40, M41, O04.

## Coverage

Every mandatory M and T identifier in the [requirements matrix](requirements.md) has an owning phase. Recommendations, optional items and extensions are also mapped. O04 is a Phase 15 scope review only. ML implementation is outside the plan. Cost-adjusted and held-out verification of early research modules is completed in Phase 11. Findings and delivery artifacts remain pending until their phases pass acceptance.
