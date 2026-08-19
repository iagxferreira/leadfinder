# leadfinder

A local lead-generation tool that finds small businesses without a website (or with an outdated one) as freelance dev/IT prospects.

Built for Iago's freelance work around Barbacena, MG, Brazil, but the target city is a parameter, not hardcoded.

## How it works

1. Query the [Google Places API (New)](https://developers.google.com/maps/documentation/places/web-service/op-overview) for local business categories (salons, clinics, restaurants, shops, offices, ...) in a given city.
2. Flag businesses that have no `website` field, or one that looks outdated (no HTTPS, not mobile-friendly).
3. Output a prioritized CSV of leads for outreach (WhatsApp-first, since that outperforms email/cold LinkedIn in this market).

## Setup

Requires [`mise`](https://mise.jdx.dev/) and [`uv`](https://docs.astral.sh/uv/) (see `CLAUDE.md` for how these are wired together in this repo).

```bash
mise use -g uv       # installs uv if not already present
uv sync              # installs project + dev dependencies into .venv
cp .env.example .env # then fill in GOOGLE_PLACES_API_KEY
```

You'll need a Google Cloud project with the **Places API (New)** enabled and billing set up (free within the $200/month Maps Platform credit for this scale of usage). See the Google Cloud Console: APIs & Services → Credentials, and restrict the key to the Places API.

## Usage

```bash
uv run leadfinder --city "Barbacena, MG, Brasil"
```

(Script not yet implemented — this documents the intended interface.)

## Development

```bash
uv run ruff check .   # lint
uv run pytest         # test
```
