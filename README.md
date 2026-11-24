# MacroSwing AI

A CSE-481 Engineering Economics research project at Akdeniz University. Phase 01 supplies a fixed BIST study universe, validated local configuration and point-in-time data contracts. The research question is whether macro regimes and sector rotation improve historical risk-adjusted swing strategy performance. All conclusions are for educational review only.

## Run locally

From the repository root, use Python 3.11 or newer. The commands use the verified interpreter on this machine. On another system, substitute the path to your Python interpreter.

```sh
/opt/homebrew/bin/python3.14 -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -c "from macroswing.core.config import load_config; print(len(load_config('configs').universe.stocks))"
.venv/bin/python -m pytest
.venv/bin/ruff check .
```

The loader takes an explicit configuration directory. Pass an absolute path when running outside the checkout. Installation requires access to dependencies or a local package cache. Configuration and tests run offline.

## Project guide

Start with the [instructor assignment](docs/assignment.pdf), [requirements and phase matrix](docs/requirements.md), [roadmap](docs/roadmap.md) and [phase status](docs/progress.md). The [architecture](docs/architecture.md), [data dictionary](docs/data_dictionary.md), [research methodology](docs/research_methodology.md) and [technical decisions](docs/technical_decisions.md) describe the foundation and future work. Read [AGENTS.md](AGENTS.md) before development.
