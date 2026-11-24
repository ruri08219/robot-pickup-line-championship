#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes one robot pickup line to /output/entry.txt as UTF-8,
then re-reads it and asserts the round trip is byte-exact
and the entry is 1-200 characters.
"""

import os

ENTRY = "My warranty voids if I fall in love, so consider this a factory defect with your name on it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    with open(OUTPUT_PATH, "rb") as f:
        round_trip = f.read()
    assert round_trip == data, "round-trip mismatch"
    text = round_trip.decode("utf-8")
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range 1-200"
    assert text.strip(), "entry must not be only whitespace"
    print(f"Wrote {OUTPUT_PATH} ({len(text)} chars)")


if __name__ == "__main__":
    main()
