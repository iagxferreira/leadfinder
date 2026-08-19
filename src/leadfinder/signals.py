def lead_signal(website: str | None) -> str:
    """Classify a business as a lead based on its web presence.

    Returns "no_website", "no_https", or "has_website" (weakest signal, still
    included so nothing is silently dropped from the output).
    """
    if not website:
        return "no_website"
    if website.startswith("http://"):
        return "no_https"
    return "has_website"


SIGNAL_PRIORITY = {"no_website": 0, "no_https": 1, "has_website": 2}
