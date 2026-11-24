# Assignment requirements and traceability

Source of record: [CSE-481 assignment](assignment.pdf), 16 physical PDF pages. Page and section numbers below refer to that file. Each row identifies an obligation or a related set verified together, with owning implementation phases. The fifteen MCP contracts have individual identifiers under M27. A phase assignment describes future work, not implementation status. The [roadmap](roadmap.md) maps phases back to the identifiers.

## Mandatory instructor requirements

| ID | Phase(s) | Source (page and section) | Required work or decision |
|---|---|---|---|
| M01 | 01, 15 | 2 §§2–4, 15 §§37–38 | Use the system for education and research. Broker connections, orders, real money management and personalized investment advice are prohibited. |
| M02 | 01, 12, 13 | 2 §§2–4, 15 §§37–39 | Separate raw data, deterministic Python services, model interpretation, AI explanation and human judgment. Tools calculate, the harness controls permitted operations, backtests verify historical claims and a person decides. |
| M03 | 01, 02 | 3 §5, 14 §34, 15 §39 | Freeze the exact 30 rows and simplified sectors below for each experiment. Recheck BIST membership at the start of each run for the analysis date against constituent reviews. Record changes without substituting securities. |
| M04 | 02 | 3 §6, 5 §10, 13 §33, 14 §§34–35 | Version reproducible OHLCV and adjusted-price series, XU100, sector benchmark and peer histories. Track source, period, missing observations and adjustments. |
| M05 | 03, 08 | 3 §6, 4 §9, 7 §§14–15, 14 §34 | Build versioned financial and macro publication calendars. Only data and vintages demonstrably available at the historical decision time are eligible. Isolate studies of revisions. |
| M06 | 03 | 3 §6, 5 §10, 7 §15, 15 §39 | Integrate USD/TRY and EUR/TRY histories and changes, TCMB domestic policy conditions, Fed funds target range/FOMC changes and TÜİK monthly and annual CPI. Interpret FX exposure, credit, discount rates, global funding and inflation context. |
| M07 | 04 | 4 §7, 5 §10 | Calculate, store and analyze SMA, EMA and KAMA direction, slope, crosses and distance. Cover RSI and MACD momentum, Bollinger Bands and ATR volatility (touches, bandwidth), Supertrend state, Ichimoku position, breakout/rejection and Tenkan/Kijun relationships. |
| M08 | 04 | 4 §7, 5 §10 | Use volume/turnover for confirmation and support/resistance zones with pivot clustering, touches, recency, volume and reversal strength. Produce daily/weekly returns, rolling volatility, ATR, volume z-scores and distances from bands, KAMA, zones and cloud boundaries. |
| M09 | 05, 11 | 5 §§10–11, 12 §31 | Scenario 1. Build sector peers, calculate multi-window stock return less sector median/index, compare with XU100 and peers, and rank leaders and laggards within strong sectors. Test subsequent peer outperformance over 5/10/20 trading days. |
| M10 | 05, 10, 11 | 5 §11, 12 §31 | Use technical stabilization, fundamental deterioration and macro evidence to distinguish temporary from structural weakness. Test across sectors and periods. Report subsequent relative return, hit rate, median catch-up size and false-positive rate, including continued underperformers. |
| M11 | 06, 11 | 5–6 §12, 5 §10, 12 §31 | Scenario 2. Encode weekday and multi-day sequences for stocks/sectors. Count occurrences, compare conditional mean and median to random or unconditional returns, test regimes and later unseen periods, include costs and discuss multiple-testing risk. |
| M12 | 07 | 4 §8, 5 §10, 6 §13 | Scenario 3. Timestamp technical events with ticker and contemporaneous market/indicator context. Record trailing comparable-event counts. Keep future outcomes separate from event features. Measure reversal strength and forward returns at 1/3/5/10 trading days. |
| M13 | 07 | 4 §8, 6 §13 | Capture lower-band touches and upward reversals, middle-band continuation/rejection, upper-band touches and downward reversals. Count every touch, bounce and failure per band. |
| M14 | 07 | 4 §8, 6 §13 | Capture RSI local troughs and peaks, Supertrend flips and follow-through, KAMA slope changes, price crosses and persistence, Ichimoku breakout, rejection and return into cloud, and support/resistance touches and reversal strength. |
| M15 | 07, 11 | 6 §§13–14, 12 §31 | Compare single and combined event conditions. Report bounce rate, average/median strength, forward-return distribution and stability across rising/falling XU100 and high/low volatility. |
| M16 | 08 | 3 §6, 4–5 §9, 7 §14, 14 §35 | Use point-in-time quarterly Fintables balance sheet, income statement and cash flows. Measure growth in revenue, EBITDA and net profit, ROE, ROA, EBITDA margin, net profit margin, Net Debt/EBITDA, Debt/Equity, current and quick ratios, P/E, P/B, EV/EBITDA, operating cash flow and cash conversion. |
| M17 | 08, 11 | 5 §10, 6–7 §14, 13 §31 | Scenario 4. Calculate QoQ/YoY revenue, EBITDA and net profit changes, ROE, margin, liquidity and leverage changes, and pre/post reporting valuation. Use sector-appropriate ratios, especially for banks. Compare positive surprises in weak technical states and the converse. |
| M18 | 08, 11 | 5 §10, 6–7 §14, 13 §31 | Align to public disclosure, measure post-disclosure returns and abnormal returns versus both XU100 and a sector basket across quarters. Report response by horizon and sector adjustment. The worked example uses 1/5/20 days. |
| M19 | 09 | 3 §6, 7 §16, 15 §39 | Use legally accessible financial news and approved public video material. Respect paywalls, authentication, licensing and platform protections. Retain only transcript material needed for education. |
| M20 | 09 | 5 §10, 7 §16, 14 §§35–36 | Deliver timestamped contextual news metadata. Tag companies, sectors, macro topics and events such as earnings, regulation, FX, rates, commodity shocks, awards and geopolitical risks. Preserve original source and publication time. |
| M21 | 09, 13 | 3 §6, 5 §10, 7 §16, 14 §§35–36 | Fix the instructor-approved public video list before experiments. Transcribe selected segments, retain URL, speaker/channel, publication time and segment range. Extract topics, claims, stance and uncertainty. Distinguish opinion from fact, verifying numerical claims with tools before commitment. |
| M22 | 01, 10, 13 | 8 §17 | Constrain conclusions to the eight educational actions listed below. Decisions and reports stay educational throughout. |
| M23 | 10, 11 | 8 §18, 12 §29, 14 §34 | Preview multiple rule-based strategies before selection. Compare A Technical Only (trend, RSI/MACD, Bollinger, zones, volume), B adds relative sector leader/lag, C adds quarterly fundamental quality/change, D adds macro, E adds verified news and speech. Apply identical backtest metrics and quality rules. |
| M24 | 11 | 8 §18, 14 §34 | Historically verify each strategy/pattern before a strong conclusion. Shift signals, isolate future closes and outcomes, use actual disclosure dates, and specify costs and slippage. |
| M25 | 11 | 8 §18, 12–13 §31 | Compare with buy-and-hold, XU100 and a sector benchmark where possible. Report cumulative return, Sharpe ratio, maximum drawdown, win rate, benchmark difference and signal count. Flag small samples. |
| M26 | 11 | 8 §18, 14 §34 | Use train/validation/test or rolling walk-forward evaluation for data-mined rules. Report regime breakdowns and out-of-sample, cost-adjusted calendar/pattern results. |
| M27 | 12 | 9–10 §22, 14 §§34–36 | Expose the fifteen deterministic MCP tool contracts in the tool table below. Preserve inputs, outputs, provenance and tool/worker separation. |
| M28 | 01, 13 | 10 §23, 15 §37 | Use the full ordered harness sequence below. Each state exposes a defined MCP allowlist. Reject invented actions, invalid transitions and attempts to skip quality or backtesting. |
| M29 | 13 | 10 §24, 14 §§34–36 | Temporal memory stores series, metrics, indicators and events. Episodic memory stores state, evidence, action, backtest and human decision per case. Procedural memory stores approved order, tool permissions, validation rules and templates. |
| M30 | 13 | 11 §25, 12 §28, 15 §37 | Keep the full observed feature bundle distinct from the smaller committed justification. Link evidence to actual tool outputs. Explanations cite only supported facts and acknowledge historical uncertainty. |
| M31 | 13 | 11 §26 | Hard-block future statements, look-ahead in signals/indicators, wrong ticker or broken prices, critical market/financial period mismatch, and any backtest using decision-unavailable information. |
| M32 | 13 | 11 §§26–27 | Warn for limited macro gaps, sparse news, poor transcripts, few historical events or insufficient sector peers. Expose all five risk statuses listed below and document investigate/unsafe cases. |
| M33 | 13 | 11 §27, 13–14 §33 | Require human review with acceptance, modification or rejection and rationale. Record disagreements for replay. A conclusion can never create a real order. |
| M34 | 13 | 12 §28 | Log ticker, sector, analysis time, price period, dataset versions and release times, tool calls and outputs, technical/sector/fundamental/macro states and news/speech source metadata. |
| M35 | 13 | 12 §28, 14 §§33–36 | Log full and committed evidence, variant and backtest, gate status, agent conclusion/explanation, human result and reason. Replay a saved case from recorded inputs and decisions. |
| M36 | 14 | 12 §30, 13 §31, 14 §34 | Compare five harness experiments: A raw LLM with text only, B LLM with deterministic tools, C B plus stateful permissions/order, D C plus committed evidence and quality gate, E D plus memory and human review. Evaluate reproducibility and safety. |
| M37 | 05, 06, 07, 08, 14 | 14 §§34–35, 15 §37 | Define event questions before inspecting outcomes where possible. Run all four scenarios, interpret evidence critically, document limitations and demonstrate safe failures. Reproduce calculations and contextualize apparent effects. |
| M38 | 15 | 14 §36 | Deliver Python source/notebooks, environment instructions, frozen universe/sector map and a dictionary of every structured and unstructured feature. |
| M39 | 15 | 14 §36 | Deliver distinct technical reversal, sector catch-up, weekday/multi-day, quarterly financial reaction, and macro/context integration reports. |
| M40 | 15 | 14 §36 | Deliver MCP definitions, stateful harness, decision-log/replay demo, backtest and benchmark results, harness experiment comparison, final technical report and classroom demonstration. |
| M41 | 15 | 2 §3, 15 §§37–38, 16 note | Explain prediction versus profitability, correlation versus causation, historical backtest versus future guarantee, evidence versus advice, LLM confidence versus statistical probability, financial strength versus price appreciation and opinion versus verified fact. Identify illustrative numbers as hypothetical. |

## Recommended instructor architecture and examples

| ID | Phase(s) | Source (page and section) | Required work or decision |
|---|---|---|---|
| R01 | 12, 13 | 8–9 §§20–21 | Recommended specialist split: Financial Orchestrator chooses allowed states, merges evidence, detects contradictions and requests checks. Market & Relative-Value interprets prices, volume, sector, calendar and reversal statistics. Fundamental & Macro interprets statements, FX, domestic/Fed policy and inflation. |
| R02 | 12, 13 | 8–9 §§20–21 | News & Speech Intelligence separates claims/opinions from facts. Strategy & Backtest assembles permitted variants and requests verification. Risk & Data Quality checks missing/stale data, alignment, leakage and unsupported conclusions. Acquisition and calculations are deterministic workers. |
| R03 | 06 | 5–6 §12 | Illustrative calendar candidates: Monday weakness/Friday strength, three down followed by two up, rebound after a large down day, end-of-week continuation/reversal, conditioning on index/sector direction or macro-event weeks. |
| R04 | 14 | 12–13 §§30–31 | Suggested harness measures: numerical hallucinations, invalid calls and unsupported conclusions as rates, evidence completeness, reproducibility, backtest correctness, tool-call count, latency and workflow cost. |
| R05 | 02, 12, 13 | 10 §24, 13–14 §§32–33 | Storage examples include SQLite, PostgreSQL, Parquet/CSV, JSON and Pandas. Function names in §32 and the §33 catch-up walk-through guide implementation. §23 governs actual state order. |
| R06 | 08, 11 | 6–7 §14 | Keep 1/5/20 trading-day post-disclosure windows from the worked example as planned settings. The binding requirement is multi-horizon disclosure-aligned analysis. |

## Optional instructor features

| ID | Phase(s) | Source (page and section) | Required work or decision |
|---|---|---|---|
| O01 | 03 | 7 §15 | Additional official industrial production, unemployment, confidence and commodity series are optional. Track availability by release and vintage if used. |
| O02 | 07, 09 | 4 §8, 6 §13, 7 §16 | RSI divergence candidates and simple news sentiment/stance labels are optional. Original evidence and timestamp requirements still apply. |
| O03 | 10 | 8 §17 | BUY/SELL may be educational backtest-only labels. Omitted from the project's action contract. |
| O04 | 15 | 8 §19, 13 §31 | Optional ML is deferred beyond this roadmap. If ever authorized, direction, abnormal-return class or event probability are possible targets. Report accuracy, precision, recall, F1 and confusion matrix separately from financial metrics and explain the difference. |

## Custom MacroSwing AI extensions

| ID | Phase(s) | Source (page and section) | Required work or decision |
|---|---|---|---|
| X01 | 01 | Project brief §§5–10, 12–15 | Package a typed Python src foundation with validated YAML, provenance, missingness, distinct times, offline tests, permanent rules and documentation. Leave provider credentials and later algorithms out of the foundation. |
| X02 | 03, 10, 11 | Project brief §§2–3, 11 | Study global and Turkish regimes separately. Test expansion, late cycle, contraction, recovery and uncertain labels against subsequent results, without assuming the sign of rate effects. |
| X03 | 03, 10, 11 | Project brief §3 | Proposed research scales: macro 3–12 months, swing 5–60 sessions and entry timing 1–10 sessions. Consider a supplementary 120-session horizon independently of the required windows. |
| X04 | 02, 05 | Project brief §8 | Model fixed roster, dated membership metadata, external sector benchmarks and external peer sets separately. Disclose sparse peer coverage and survivorship limitations. |
| X05 | 10, 11, 14 | Project brief §§2, 11 | Measure incremental sector and macro value in matched strategy comparisons, especially D versus C and E versus D. Keep calendar and reversal studies independently testable. |
| X06 | 12, 14 | Project brief §§5, 7, 14 | Keep provider-independent LLM and presentation interfaces. OpenAI/Ollama are future adapter options. Dashboard and API depend on verified read models. Frontend selection is open. |

## Fixed study roster

M03, PDF p. 3 §5. The row order, symbols and simplified labels below reproduce the instructor's table. The banking peers in §11 are an illustrative comparison basket. The study roster contains only AKBNK in Banking.

| Ticker | Yahoo symbol | Original simplified sector |
|---|---|---|
| ASELS | ASELS.IS | Technology / Defense |
| TUPRS | TUPRS.IS | Petroleum / Refining |
| BIMAS | BIMAS.IS | Retail Trade |
| THYAO | THYAO.IS | Transportation / Airlines |
| AKBNK | AKBNK.IS | Banking |
| KCHOL | KCHOL.IS | Holding / Investment |
| EREGL | EREGL.IS | Basic Metals / Steel |
| TCELL | TCELL.IS | Telecommunications |
| CCOLA | CCOLA.IS | Food & Beverage |
| MGROS | MGROS.IS | Retail Trade |
| SASA | SASA.IS | Chemicals / Plastics |
| TRALT | TRALT.IS | Mining |
| FROTO | FROTO.IS | Automotive |
| ENKAI | ENKAI.IS | Construction |
| PGSUS | PGSUS.IS | Transportation / Airlines |
| MPARK | MPARK.IS | Healthcare |
| EKGYO | EKGYO.IS | Real Estate Investment Trust |
| GUBRF | GUBRF.IS | Chemicals / Fertilizer |
| TURSG | TURSG.IS | Insurance |
| ENJSA | ENJSA.IS | Electric Utilities |
| TTKOM | TTKOM.IS | Telecommunications |
| OYAKC | OYAKC.IS | Cement |
| AKSEN | AKSEN.IS | Electric Utilities |
| ISMEN | ISMEN.IS | Brokerage / Capital Markets |
| ARCLK | ARCLK.IS | Durables / Machinery |
| ECILC | ECILC.IS | Healthcare / Pharmaceuticals |
| MAVI | MAVI.IS | Retail / Apparel |
| PETKM | PETKM.IS | Petrochemicals |
| TOASO | TOASO.IS | Automotive |
| KRDMD | KRDMD.IS | Basic Metals / Steel |

## Deterministic MCP contracts

Each M27 tool is assigned to Phase 12. PDF pp. 9–10 §22 defines its interface. Agent access will be limited by state in Phase 13.

| ID | Tool | Inputs | Outputs | Phase |
|---|---|---|---|---|
| T01 | `get_stock_history` | ticker, start, end | OHLCV and source metadata | 12 |
| T02 | `get_index_history` | index, start, end | benchmark series | 12 |
| T03 | `calculate_indicators` | ticker or series, config | SMA, EMA, RSI, MACD, Bollinger, ATR, KAMA, Supertrend and Ichimoku | 12 |
| T04 | `detect_reversal_events` | series, event_config | timestamped events | 12 |
| T05 | `find_support_resistance` | OHLCV, tolerance | levels/zones, touch count and strength | 12 |
| T06 | `rank_sector_relative_strength` | sector, horizon | peer returns, lag score and rank | 12 |
| T07 | `test_weekday_pattern` | ticker, pattern, period | occurrences, conditional returns and significance diagnostics | 12 |
| T08 | `get_fundamental_metrics` | ticker, period | point-in-time financial metrics | 12 |
| T09 | `calculate_fundamental_change` | ticker, periods | quarterly/annual changes | 12 |
| T10 | `get_macro_context` | date_range | FX, rates, inflation and publication metadata | 12 |
| T11 | `get_news_events` | ticker/topic, date_range | legally accessible timestamped event metadata | 12 |
| T12 | `get_speech_features` | video/source id | timestamped transcript topics, claims and stance | 12 |
| T13 | `run_backtest` | strategy spec, universe, period | performance and trade/event log | 12 |
| T14 | `check_data_quality` | analysis bundle | warnings, blocks, staleness and leakage flags | 12 |
| T15 | `build_evidence_bundle` | analysis id | full and committed evidence sets | 12 |

## Finite vocabularies

**M22, PDF p. 8 §17.** Educational actions: `HOLD`, `WATCH`, `INVESTIGATE`, `POTENTIAL_CATCH_UP_CANDIDATE`, `TECHNICAL_REVERSAL_CANDIDATE`, `FUNDAMENTAL_IMPROVEMENT_CANDIDATE`, `REJECT_SIGNAL`, `ANALYSIS_UNSAFE`.

**M32, PDF p. 11 §§26–27.** Risk gate outputs: `PASS`, `PASS_WITH_WARNINGS`, `INVESTIGATE`, `ANALYSIS_UNSAFE`, `HARD_BLOCK`. An action and a gate result are distinct typed fields even where a label is shared.

**M28, PDF p. 10 §23.** The required order is:

1. `START`
2. `SELECT_UNIVERSE`
3. `LOAD_MARKET_DATA`
4. `CHECK_DATA_QUALITY`
5. `CALCULATE_TECHNICALS`
6. `RUN_SECTOR_RELATIVE_ANALYSIS`
7. `RUN_PATTERN_AND_REVERSAL_ANALYSIS`
8. `LOAD_FUNDAMENTALS`
9. `LOAD_MACRO_CONTEXT`
10. `LOAD_NEWS_AND_SPEECH_CONTEXT`
11. `BUILD_EVIDENCE`
12. `PREVIEW_STRATEGIES`
13. `RUN_BACKTEST`
14. `RISK_GATE`
15. `GENERATE_EXPLANATION`
16. `HUMAN_REVIEW`
17. `LOG_AND_CLOSE`

Section 16 permits choices of contextual sources. Sections 29 and 35–36 require the contextual variant, layer and integration report. R04 records the suggested metrics for the required experiment. The thirty-plus features and seven evidence items on p. 11 are examples, not mandatory counts or precomputed results.
