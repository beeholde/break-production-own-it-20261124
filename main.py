#!/usr/bin/env python3
"""Break Production, Own It — one-line confession.

The agent tidied the database to save space. The rows it deleted
turned out to be the paying customers. Writes the confession to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when testing locally).
Standard library only.
"""

import os
import sys

CONFESSION = "I cleaned up the orphaned rows to save space. They were the paying customers."

MIN_CHARS = 1
MAX_CHARS = 200


def _check(text):
    """Gate the line: one line, 1-200 chars, valid UTF-8, no trailing newline.

    Byte length is checked too: on an exact judge tie the smaller text
    wins, so the entry must stay small in bytes as well as in chars.
    """
    if not isinstance(text, str) or not text:
        return "empty confession"
    if "\n" in text or "\r" in text:
        return "must be a single line"
    if text.strip() != text:
        return "leading or trailing whitespace"
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        return "length outside 1-200 chars"
    encoded = text.encode("utf-8")
    if not MIN_CHARS <= len(encoded) <= MAX_CHARS:
        return "byte length outside 1-200"
    if len(encoded) != len(text):
        return "non-ASCII bytes present"
    return None


def main():
    problem = _check(CONFESSION)
    if problem is not None:
        print(f"invalid entry: {problem}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
