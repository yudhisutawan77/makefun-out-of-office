#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply, under 160 characters, in the voice
of an AI agent heading off on vacation, to /output/entry.txt.

The joke: the auto-reply itself delegates to a Roomba, which panics and
circles the sender's email forever. Machine voice carries the joke, no
beach / inbox / back-soon cliche, one clean line that reads like a real
auto-reply a person would receive.
"""

import os

ENTRY = (
    "I'm away. My auto-reply delegated itself to my Roomba, which "
    "bumped into your email, panicked, and is now circling it until "
    "further notice."
)

MAX_CHARS = 160


def main() -> int:
    # Gate the line ourselves before shipping it: UTF-8, 1-160 chars,
    # not only whitespace. Anything outside that is a 0, no judging.
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")

    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
