import argparse
import csv
import os
import sys

from dotenv import load_dotenv

from .categories import DEFAULT_CATEGORIES
from .places import search_text
from .signals import SIGNAL_PRIORITY, lead_signal

CSV_FIELDS = [
    "name",
    "category",
    "address",
    "phone",
    "website",
    "signal",
    "rating",
    "maps_url",
]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find local small-business leads via the Google Places API."
    )
    parser.add_argument("--city", required=True, help='e.g. "Barbacena, MG, Brasil"')
    parser.add_argument(
        "--categories",
        help="comma-separated business categories to search (defaults to a built-in local-business list)",
    )
    parser.add_argument("--output", default="leads.csv", help="CSV output path")
    return parser.parse_args(argv)


def place_to_row(place: dict, category: str) -> dict:
    website = place.get("websiteUri")
    return {
        "name": place.get("displayName", {}).get("text", ""),
        "category": category,
        "address": place.get("formattedAddress", ""),
        "phone": place.get("internationalPhoneNumber", ""),
        "website": website or "",
        "signal": lead_signal(website),
        "rating": place.get("rating", ""),
        "maps_url": f"https://www.google.com/maps/place/?q=place_id:{place['id']}",
    }


def find_leads(city: str, categories: list[str], api_key: str) -> list[dict]:
    seen_ids = set()
    rows = []

    for category in categories:
        query = f"{category} em {city}"
        for place in search_text(query, api_key):
            place_id = place.get("id")
            if not place_id or place_id in seen_ids:
                continue
            seen_ids.add(place_id)
            rows.append(place_to_row(place, category))

    rows.sort(key=lambda row: SIGNAL_PRIORITY[row["signal"]])
    return rows


def main(argv: list[str] | None = None) -> None:
    load_dotenv()
    api_key = os.environ.get("GOOGLE_PLACES_API_KEY")
    if not api_key:
        sys.exit("GOOGLE_PLACES_API_KEY is not set (check your .env file)")

    args = parse_args(argv if argv is not None else sys.argv[1:])
    categories = (
        [c.strip() for c in args.categories.split(",")]
        if args.categories
        else DEFAULT_CATEGORIES
    )

    rows = find_leads(args.city, categories, api_key)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} leads to {args.output}")
