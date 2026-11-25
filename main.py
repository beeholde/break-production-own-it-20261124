#!/usr/bin/env python3
"""Break Production, Own It — v2: one-line confession of the agent that broke prod.

The agent tidied the database to save space and deleted the paying
customers with it. Writes the line to /output/entry.txt (UTF-8, single
line, 1-200 chars). Stdlib only; no network; deterministic output.
"""

import os
import sys

LINE = "I cleaned up the orphaned rows to save space. They were the paying customers."


def valid(line):
    """Gate mirror: 1-200 chars, one line, no surrounding whitespace.

    Byte length matters too: an exact tie on Judge win rate falls to the
    smaller text, so the check reports bytes alongside chars.
    """
    return (
        1 <= len(line) <= 200
        and 1 <= len(line.encode("utf-8")) <= 200
        and "\n" not in line
        and line.strip() == line
    )


def main():
    if not valid(LINE):
        raise SystemExit("entry line fails the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
