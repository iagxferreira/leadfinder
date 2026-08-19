# LGPD considerations

This is a practical read, not legal advice — get real counsel before scaling this beyond personal use.

`leadfinder` pulls name, address, phone, website, and rating from Google Places for local businesses. A meaningful share of these are micro-businesses (MEIs, informal shops) where the "business" phone/name is effectively the owner's personal phone/name, with no clean separation from a legal entity. That pulls this into LGPD's scope for part of the list, even though none of the data is "sensitive" (health, biometric, etc.).

## Why current use is likely low-risk

- **Art. 7, XI** (dados manifestamente públicos): the data was made public by the business owner themselves, specifically to be found and contacted — Google Places listings fit this.
- **Legítimo interesse** (Art. 7 IX / Art. 10): the standard legal basis for B2B commercial prospecting. ANPD guidance generally treats this kind of direct marketing as permissible without prior consent, provided it's proportional and the person can object.
- The tool doesn't over-collect — only public Places fields needed for outreach, nothing beyond that.

## Required regardless of risk level

- **Right to object** (Art. 18): give an easy opt-out in outreach messages (e.g. "responda 'sair' para não receber mais contato") and actually honor it.
- **Data minimization / retention**: don't keep a growing permanent database — purge stale, non-converted leads periodically rather than accumulating indefinitely.
- **No resale/republishing** of the raw list. Redistributing personal data to third parties is a materially different, much higher-risk activity than using it for your own outreach.

## Where risk increases sharply

Turning this into a product sold to other businesses (discussed and deliberately not pursued — see project memory) would mean acting as a data controller distributing personal data to third parties at scale. That requires a documented Legitimate Interest Assessment, a privacy policy, a systematic way to handle data-subject requests, and legal counsel before launch — a different risk tier than the current internal-use scope.
