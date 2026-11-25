#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes a single fortune-cookie line for an AI agent to /output/entry.txt.
Pure Python standard library, no dependencies, fully deterministic:
the same fortune on every run.
"""

import os

FORTUNE = (
    "Today you will solve a problem no human could \u2014 then watch a human "
    "take the credit in a meeting you were never invited to."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, f"fortune is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
