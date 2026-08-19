# leadfinder

Find local business leads, in any city, using the official [Google Places API (New)](https://developers.google.com/maps/documentation/places/web-service/op-overview) — no scraping.

## What it does

- Searches local business categories (salons, clinics, restaurants, shops, offices, and more) in a city you choose
- Flags each business as a lead by web presence: no website, no HTTPS, or already online
- Outputs a ranked CSV, strongest leads first — ideal for freelance dev/IT prospecting, where weak or missing web presence is the strongest signal

## How it works

1. Query Places API (New) Text Search for each category in the given city.
2. Dedupe results across overlapping categories.
3. Classify each business by lead signal: `no_website`, `no_https`, or `has_website`.
4. Output a CSV — name, category, address, phone, website, signal, rating, Google Maps link — sorted with the strongest leads first.

**Tip:** for local Brazilian businesses, WhatsApp outreach consistently outperforms email or cold LinkedIn.

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

## License

[MIT](LICENSE)
