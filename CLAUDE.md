# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Dependency management and execution go through `uv` (installed via `mise use -g uv`, not a standalone installer — this repo follows the user's existing `mise`-based tool workflow).

```bash
uv sync                    # install project + dev dependencies into .venv
uv run leadfinder --city "..."  # run the CLI (entry point defined in pyproject.toml [project.scripts])
uv run ruff check .        # lint
uv run ruff format .       # format
uv run pytest              # run tests
uv run pytest path/to/test_file.py::test_name  # run a single test
```

Python version is pinned to 3.12 (`.python-version`), managed by `uv`, independent of the system Python.

Secrets (`GOOGLE_PLACES_API_KEY`) go in a gitignored `.env`, loaded via `python-dotenv`. Copy `.env.example` to `.env` and fill in the real key — never commit `.env`.

## Architecture

`leadfinder` is a lead-generation CLI, not a service: it queries the **Google Places API (New)** for local business categories (salons, clinics, restaurants, shops, offices, etc.) in a given city, flags businesses with no `website` field or a clearly outdated one (no HTTPS, not mobile-friendly), and outputs a prioritized CSV for outreach. See `README.md` for the full rationale (built for freelance lead-gen around Barbacena, MG, Brazil; WhatsApp-first outreach; official Places API used deliberately instead of scraping Google Maps, for ToS/legal reasons).

The city is meant to be a CLI parameter (`--city`), not hardcoded — this is a deliberate design decision so the tool isn't tied to one location.

Package uses a `src/` layout (`src/leadfinder/`), with the CLI entry point mapped via `[project.scripts]` in `pyproject.toml` to `leadfinder:main`.

**Scope note:** this tool is intentionally a local CLI script, not a hosted API. Wrapping it as a service (e.g. FastAPI) was considered and deliberately deferred until there's a real second consumer beyond the primary user, since exposing it as an API would require adding auth and rate-limiting to protect the paid Google Places quota.

## Commit conventions

Commit in small, atomic, logically-scoped commits using Conventional Commits prefixes (`feat:`, `fix:`, `chore:`, `docs:`, `test:`, etc.) — this is an explicit preference for this repo, not just a default.
