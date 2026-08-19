# leadfinder

Finds local business leads, by city, using the [Google Places API (New)](https://developers.google.com/maps/documentation/places/web-service/op-overview) — no scraping, just the official API.

Given a city, it searches a set of local business categories (salons, clinics, restaurants, shops, offices, ...), and flags each business as a lead based on its web presence: no website at all, a website without HTTPS, or an already-established website. That makes it useful for freelance dev/IT prospecting — businesses with weak or no web presence are the strongest leads.

Originally built for local freelance prospecting in Brazil, but the city is a CLI parameter, not hardcoded — it works for any city Google Places covers.

## How it works

1. Query Places API (New) Text Search for each category in the given city.
2. Dedupe results across categories (a place matched by more than one category search is kept once, under the first category it was found under).
3. Classify each business by lead signal: `no_website`, `no_https`, or `has_website`.
4. Output a CSV — name, category, address, phone, website, signal, rating, Google Maps link — sorted with the strongest leads (`no_website`) first.

Outreach is meant to be WhatsApp-first, since that outperforms email/cold LinkedIn in the Brazilian local-business market this was built for.

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
make run CITY="São Paulo, SP, Brasil"
# or directly:
uv run leadfinder --city "São Paulo, SP, Brasil"
```

Optional flags: `CATEGORIES="padaria,salão de beleza"` to override the default category list, `OUTPUT=leads.csv` to change the output path.

## Development

```bash
make lint    # ruff check
make format  # ruff format
make test    # pytest
make check   # lint + test
```

Run `make help` for the full list of targets.
