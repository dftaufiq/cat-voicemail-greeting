#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, as if recorded by a cat, to
/output/entry.txt. The greeting must be UTF-8 text of 1 to 120
characters (RULES.txt gate); this one is 117 characters.
"""

import os

GREETING = "You've reached Beans. Press 1 for treats, press 2 to be ignored, meow after the beep — I'll pretend I didn't hear it."

def main() -> None:
    text = GREETING
    assert 1 <= len(text) <= 120, f"greeting is {len(text)} chars, must be 1-120"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)

if __name__ == "__main__":
    main()
