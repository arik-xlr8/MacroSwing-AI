# MacroSwing AI development rules

## Phase control

- Read the complete assignment, docs/requirements.md, docs/roadmap.md and docs/progress.md before implementing each phase.
- Implement only the explicitly authorized phase. Stop after its acceptance report and wait for explicit authorization before starting another.
- Preserve scope. Document assumptions, limitations, unresolved requirements and incomplete work. Obtain authorization for scope changes.
- Preserve existing user files and the original assignment PDF. Never delete or overwrite user files without authorization.
- Update docs/progress.md after every phase with actual verification results and remaining work.

## Research integrity

- Never fabricate financial data. Clearly label synthetic test fixtures and keep them separate from research data and published results.
- Never introduce look-ahead bias or use unpublished, revised-later or future information in historical decisions. Separate observation, publication, availability, retrieval and decision times.
- Preserve source provenance, immutable dataset versions and data availability timestamps.
- Keep calculations deterministic and modules independently testable. Reject numerical LLM claims lacking verified tool evidence.
- Enforce all mandatory quality, risk and backtesting states. A human reviews educational conclusions.
- Never execute real financial transactions, connect to brokers, manage real funds or provide personalized advice.

## Access and verification

- Respect authentication, paywalls, licensing restrictions and platform protections. Never bypass them.
- Never expose credentials or API keys. Paid API requests require explicit user approval.
- Write and execute tests for implemented functionality. Report actual commands and results. Identify any untested behavior.
