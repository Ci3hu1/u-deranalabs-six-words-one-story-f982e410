# STRATEGY — Six Words, One Story

## The story

> Grandma's last letter arrived after her.

Six words. 40 characters. The submission title is the story itself.

## What the six words do

A grandmother writes a letter, dies before it arrives, and someone
receives it after she is gone. The whole arc — writing, dying, arriving —
is implied in six words:

1. **"Grandma's"** — the relationship. Warmth, family, a person the reader
   already cares about in one word.
2. **"last"** — finality. This is the last letter; there will be no more.
   It tells the reader she is dying, or already dead, without saying so.
3. **"letter"** — the object and the message. A letter is a voice from
   someone absent; it carries words she chose.
4. **"arrived"** — the event. The letter completes its journey.
5. **"after"** — the turn. The whole story hinges on this word: the
   letter arrives AFTER her. Too late. She is gone.
6. **"her."** — the absence. She is not here to see it arrive.

## Against the judge's five criteria (in the brief's order)

1. **Complete story in exactly six words.** Six words, counted:
   Grandma's / last / letter / arrived / after / her. It is a story, not
   a slogan or a list: a writer, a letter, a death, an arrival. A
   fragment would lose to any six-word story; this one is complete.
2. **A turn, a surprise, a whole life implied.** The turn is "after":
   the letter arrives too late. A whole life is implied — the
   grandmother's life, and the relationship between her and the reader
   who receives the letter. Six words carry far more than their length.
3. **Every word earns its place.** No filler. "Grandma's" sets the
   relationship; "last" sets the finality; "letter" is the object;
   "arrived" is the event; "after" is the twist; "her" is the absence.
   Remove any one and the story breaks. No word could be replaced by a
   better one without changing the story.
4. **Reads cleanly aloud.** "Grandma's last letter arrived after her."
   One smooth sentence, plain words, a natural rhythm. No clumsy
   phrasing, no ambiguity that trips the reader — the primary reading
   (she died; the letter arrived too late) is immediate.
5. **Leaves something unsaid.** What did the letter say? Who received
   it? Did she know she was dying when she wrote it? The reader fills
   that in. The story does not spell it out.

## Why this shape, not a shorter or longer one

Judge-scored text rewards one concrete image with a turn — the icantcodefyi
evidence (poem "Always Allow", 2 words, 91.9% win rate). Six words is the
brief's fixed length, so the work is choosing which six. A line that is
only a mood ("The rain fell. Nobody stayed.") is a fragment, not a story.
A line that explains itself ("She died, but her letter came late.")
spends its words telling instead of showing. This line shows: the letter
arriving after her IS the story.

## Candidates considered and dropped

- **"The lighthouse keeper finally turned inland."** (6 words) A good
  image and a turn, but less of a complete story — why he turned inland
  is unclear, and the emotional weight is thinner than a grandmother's
  last letter.
- **"The door opened. Nobody was there."** (6 words) A twist, but a
  horror beat more than a story, and a familiar trope; less emotional
  depth and less for the reader to fill in.
- **"She sold the house. Kept the swing."** — 7 words. Does not fit.
- **"He kept her voicemail. She moved on."** — 7 words. Does not fit.
- **"The old dog waited. Nobody came home."** — 7 words. Does not fit.
- **"After fifty years, he finally said yes."** — 7 words. Does not fit.

The dropped lines that fit the word count were weaker on criterion 1
(complete story) or criterion 2 (turn / whole life implied). The
grandmother's letter is strongest on both.

## Truthfulness

Clean and universal: no brand names, no numbers, nothing inflated. The
story is fiction, not a claim about the world — nothing in it can be
checked false. It is original: it is not Hemingway's "For sale: baby
shoes, never worn." and it copies no known six-word story.

## The program

`main.py` is pure Python stdlib. It holds the story as a constant,
validates it (1–60 chars, exactly 6 words, not only whitespace), and
writes it byte-for-byte to `/output/entry.txt`. Deterministic: the same
bytes on every run, no randomness, no clock, no network. The gate in the
brief (1–60 UTF-8 chars) passes at 40 characters.
