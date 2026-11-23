#!/usr/bin/env python3
"""Six Words, One Story.

Writes one complete story, in exactly six words, to /output/entry.txt
(or to the path given as the first argument, for local testing).

The story was written by hand, not generated:

    Grandma's last letter arrived after her.

Six words, 40 characters. A grandmother writes a letter, dies before it
arrives, and someone receives it after she is gone. The turn is the word
"after": the letter arrives too late. What the letter said, and who
received it, is left for the reader to fill in.

Pure standard library. Deterministic: the same bytes on every run, no
randomness, no clock, no network.
"""

import os
import sys

STORY = "Grandma's last letter arrived after her."

DEFAULT_OUTPUT = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 60
EXPECTED_WORDS = 6


def word_count(text: str) -> int:
    """Words are whitespace-separated tokens; a possessive like
    "Grandma's" is one word."""
    return len(text.split())


def main(argv) -> int:
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT

    if not STORY.strip():
        print("story is only whitespace", file=sys.stderr)
        return 1
    if not (MIN_CHARS <= len(STORY) <= MAX_CHARS):
        print(
            f"story is {len(STORY)} chars, must be {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if word_count(STORY) != EXPECTED_WORDS:
        print(
            f"story is {word_count(STORY)} words, must be {EXPECTED_WORDS}",
            file=sys.stderr,
        )
        return 1

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)

    print(f"wrote {len(STORY)} chars, {word_count(STORY)} words to {output_path}")
    print(STORY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
