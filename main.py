#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes one funny one-line review of my Monday to /output/entry.txt
(or $OUTPUT_DIR/entry.txt) and validates the competition gate:
UTF-8 text, 1-200 characters, not only whitespace, a single line.
"""

import os
import sys

ENTRY = (
    "Monday review: woke up tired, inbox already angry, "
    "and my 9 a.m. meeting could have been an email. "
    "One star, would not Monday again."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
