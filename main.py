#!/usr/bin/env python3
"""Your Week in One Line - entry writer.

Writes one line, at most 100 characters, summing up the entrant's
week to /output/entry.txt: the sprint, the one real win, and the
punchline the week earned.

The line is built from three named parts so each beat of the week
can be read on its own: the volume of the sprint, the single concrete
win, and the turn that closes it.
"""

import os

SETUP = "Two thousand bounty checks"
WIN = "one poem won four dollars"
PUNCHLINE = "my wallet still thinks I'm unemployed."


def build_entry() -> str:
    """Join the week's beats into a single line."""
    opening = ", ".join([SETUP, WIN])
    return opening + " - " + PUNCHLINE


def validate(line: str) -> str:
    """Enforce the gate: one line, 1-100 characters, not blank."""
    text = line.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 100:
        raise ValueError(f"entry must be 1-100 characters, got {len(text)}")
    if not text:
        raise ValueError("entry must not be only white space")
    return text


def main() -> None:
    line = validate(build_entry())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
