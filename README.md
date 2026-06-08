# agentic_ai

A hands-on codebase for learning and teaching **Agentic AI** — building systems where LLMs plan, use tools, and act autonomously toward a goal.

This repository grows alongside workshops and study sessions with friends and colleagues. Each module adds runnable examples you can read, run, and extend.

## What you'll learn

| Topic | Description |
| --- | --- |
| **Agents & loops** | ReAct-style reasoning, tool selection, and multi-step execution |
| **Tool use** | Defining callable tools and wiring them into an agent runtime |
| **MCP (Model Context Protocol)** | Connecting agents to external capabilities via MCP servers and clients |
| **Orchestration** | Routing tasks, managing state, and composing multi-agent workflows |
| **Production patterns** | Config, logging, error handling, and safe defaults |

## Project structure

```
agentic_ai/
├── config/          # Runtime configuration (API keys via env, not committed)
├── data/            # Sample datasets and fixtures for examples
├── docs/            # Workshop notes, diagrams, and reference material
├── src/
│   └── main.py      # Entry point for examples and demos
├── pyproject.toml   # Project metadata and dependencies
└── README.md
```

## Prerequisites

- **Python 3.14+** (see `.python-version`)
- [uv](https://docs.astral.sh/uv/) or `pip` for dependency management
- An LLM provider API key (e.g. OpenAI, Anthropic) — store in environment variables, never in source

## Getting started

```bash
# Clone the repository
git clone git@github.com:shivpsingh/agentic_ai.git
cd agentic_ai

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install the project (dependencies added as examples land)
pip install -e .

# Run the entry point
python src/main.py
```

With **uv**:

```bash
uv venv && source .venv/bin/activate
uv pip install -e .
python src/main.py
```

## Configuration

Place secrets and environment-specific settings outside of source control:

```bash
# Example — copy and fill in your values
cp config/.env.example config/.env   # when available
export OPENAI_API_KEY="your-key-here"
```

Never commit `.env` files or API keys. See `.gitignore` for excluded paths.

## Roadmap

- [ ] Minimal agent loop with a single tool
- [ ] MCP server exposing custom tools
- [ ] MCP client consuming external servers
- [ ] Multi-step task with memory and state
- [ ] Workshop walkthrough docs in `docs/`

## Contributing & learning together

This repo is meant for collaborative learning. If you're following along in a session:

1. Pull the latest changes before each workshop.
2. Work through examples in order — later modules build on earlier ones.
3. Open issues or PRs for clarifications, fixes, or new examples.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE).
