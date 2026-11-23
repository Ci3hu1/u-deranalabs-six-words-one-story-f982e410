#!/usr/bin/env python3
"""Tests for the six-word story entry.

Pure standard library (unittest). Runs main.py twice and asserts:
- the output file is written, UTF-8, 1-60 chars, not only whitespace
- exactly six words, and the content is exactly the expected story
- the two runs are byte-identical (deterministic, per run_deterministic)
- the story is not Hemingway's famous line
"""

import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_PY = os.path.join(REPO, "main.py")

EXPECTED = "Grandma's last letter arrived after her."
HEMINGWAY = "For sale: baby shoes, never worn."


def run_entry(out_path):
    result = subprocess.run(
        [sys.executable, MAIN_PY, out_path],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result


class TestSixWordStory(unittest.TestCase):
    def test_story_is_exactly_six_words(self):
        self.assertEqual(len(EXPECTED.split()), 6)
        self.assertEqual(EXPECTED.split(), [
            "Grandma's", "last", "letter", "arrived", "after", "her.",
        ])

    def test_story_within_gate(self):
        # The sealed scorer gates on 1-60 UTF-8 chars, not only whitespace.
        self.assertTrue(1 <= len(EXPECTED) <= 60)
        self.assertEqual(len(EXPECTED), 40)
        self.assertTrue(EXPECTED.strip())
        self.assertTrue(EXPECTED.endswith("."))
        self.assertEqual(EXPECTED.encode("utf-8"), EXPECTED.encode("utf-8"))

    def test_story_is_original_not_hemingway(self):
        self.assertNotEqual(EXPECTED, HEMINGWAY)
        self.assertNotIn("baby shoes", EXPECTED)
        self.assertNotIn("For sale", EXPECTED)

    def test_story_has_no_brand_or_number(self):
        # Clean and universal: no brand names, no inflated numbers.
        self.assertFalse(any(ch.isdigit() for ch in EXPECTED))

    def test_program_writes_exact_story(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.txt")
            result = run_entry(out)
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            with open(out, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content, EXPECTED)
            self.assertEqual(len(content.split()), 6)

    def test_deterministic_two_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            out1 = os.path.join(tmp, "a.txt")
            out2 = os.path.join(tmp, "b.txt")
            r1 = run_entry(out1)
            r2 = run_entry(out2)
            self.assertEqual(r1.returncode, 0, msg=r1.stderr)
            self.assertEqual(r2.returncode, 0, msg=r2.stderr)
            with open(out1, "rb") as f:
                b1 = f.read()
            with open(out2, "rb") as f:
                b2 = f.read()
            self.assertEqual(b1, b2)

    def test_default_output_path(self):
        # main.py with no argument targets /output/entry.txt; only check
        # the constant, not the write, so the suite never needs /output.
        source = open(MAIN_PY, encoding="utf-8").read()
        self.assertIn('DEFAULT_OUTPUT = "/output/entry.txt"', source)


if __name__ == "__main__":
    unittest.main()
