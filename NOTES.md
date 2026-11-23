# NOTES — u-deranalabs-six-words-one-story-f982e410

## Entry

- Competition: Six Words, One Story ($5: 1st $2, 2nd $2, 3rd $1), free entry.
- Opens 24 Nov 2026 00:38 WIB, closes 24 Nov 2026 03:35 WIB (three-hour window). Results 15 Dec 2026.
- The story (6 words, 40 chars): "Grandma's last letter arrived after her."
- Submission title is the story itself.
- Program: `main.py`, pure Python stdlib, writes the story to `/output/entry.txt`. Deterministic (identical bytes on repeat runs).
- Judge: pairwise text comparison, z-ai/glm-5.3-flash; criteria in order: (1) complete story in exactly six words, (2) turn/surprise/whole life implied, (3) every word earns its place, (4) reads cleanly aloud, (5) leaves something unsaid. Blind rounds (3), board hidden; dev heat vs 3 anchors + 3 rungs; final heat = 3 Swiss rounds + top-5 playoff. Gate: 1–60 UTF-8 chars (we are 40).

## Field

- 22 entries at build (per parent task). Blind rounds hide standings; top 10 could not be studied (and per Joni 23 Nov, no top-10 study before building anyway).
- Quota at build: day cap 5 left, hard limit 40 left, can_submit true, entries_made 0. Blind round slot available (round 1, ends 01:37 WIB).

## Build

- Fresh kit downloaded 24 Nov ~00:53 WIB. Kit `init` created LICENSE (MIT, SPDX line) + .makefun/freshness.json (anchor 98804f4276bca0c4ea8734ed9337a22cca226b5c, round 34217677).
- `main.py`, `STRATEGY.md`, `tests/test_entry.py`, `README.md` (template badges, owner/repo/referral filled), `NOTES.md` written in the build session.
- Tests: `python3 -m unittest discover -s tests -v` — all pass (six words, gate 1–60 chars, exact output, originality vs Hemingway, determinism over two runs).
- NOT submitted — awaiting Joni's Setuju on the exact entry (parent presents it).
- **SUBMITTED 24 Nov ~01:01 WIB on Joni's "Setuju": submission 01a20991-eb1b-722d-8d2d-f49edacb4c30, stage "scored", round 1. All intake checks pass. Claim code ONLY in ~/.config/makefun/u-deranalabs-six-words-one-story-f982e410-submission.json (0600).**

## Live score

- Blind rounds: NO live score at submit. Round 1 of 3 judged after cutoff 01:37 WIB (2026-11-23T18:37:29Z); check GET /api/competitions/u-deranalabs-six-words-one-story-f982e410/rounds then. Final at deadline 03:35 WIB; results 15 Dec 2026.
