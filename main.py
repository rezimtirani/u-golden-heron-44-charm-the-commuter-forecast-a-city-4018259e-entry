"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (at most 140 characters) for a city that
does not exist to /output/entry.txt.
"""

import os

FORECAST = (
    "Good morning, Grumplewick: 14°C with light drizzle, clearing by nine "
    "— and yes, the 8:15 bus is actually on time."
)


def validate(line):
    """The forecast must be one non-blank line of at most 140 chars."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("forecast must not be blank")
    if "\n" in stripped or len(stripped) > 140:
        raise ValueError("forecast must be one line of at most 140 chars")
    return stripped


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(validate(FORECAST))


if __name__ == "__main__":
    main()
