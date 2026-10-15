# Agentic AI Course: Python Foundations

My hands-on practice repository on the path to becoming an **AI Automation Engineer**.
It covers the Python foundations needed before building LLM-powered agents.

> This is a **learning repo**: small, focused practice scripts.
> Portfolio projects will live in their own separate repositories.

## Structure

| Folder | What's inside |
|---|---|
| `basics/` | Functions, loops, conditionals, comprehensions, type hints, custom exceptions |
| `pydantic/` | Pydantic v2 models, field and model validators, nested models, data filtering |
| `files_logging/` | JSON and text file handling, logging (handlers, rotation), `.env` config |
| `http/` | REST API calls with `requests` (GET/POST, timeouts, error handling) |
| `capstones/` | Mini-projects combining several topics (agent fleet, ticket resolver, tool router, news scraper) |

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install pydantic requests python-dotenv
```

Run scripts **from the repo root**, for example `python pydantic/nested_models.py`.
Generated `.log` / `.json` / `.txt` outputs are git-ignored and recreated on each run.

## Tech

Python 3.14 · Pydantic v2 · requests · python-dotenv · logging