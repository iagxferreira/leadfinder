import time

import requests

SEARCH_URL = "https://places.googleapis.com/v1/places:searchText"

FIELD_MASK = (
    "places.id,places.displayName,places.formattedAddress,"
    "places.internationalPhoneNumber,places.websiteUri,places.rating,"
    "places.businessStatus,nextPageToken"
)

PAGE_TOKEN_DELAY_SECONDS = 2


def search_text(query: str, api_key: str) -> list[dict]:
    """Run a Places API (New) Text Search, following pagination until exhausted."""
    results = []
    page_token = None

    while True:
        body = {"textQuery": query, "languageCode": "pt-BR"}
        if page_token:
            body["pageToken"] = page_token

        response = requests.post(
            SEARCH_URL,
            json=body,
            headers={
                "Content-Type": "application/json",
                "X-Goog-Api-Key": api_key,
                "X-Goog-FieldMask": FIELD_MASK,
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        results.extend(data.get("places", []))

        page_token = data.get("nextPageToken")
        if not page_token:
            break

        # Google requires a short delay before a pageToken becomes valid.
        time.sleep(PAGE_TOKEN_DELAY_SECONDS)

    return results
