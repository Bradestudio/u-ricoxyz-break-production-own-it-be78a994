#!/usr/bin/env python3
"""Break Production, Own It -- make.fun entry (program/v1).

Writes one brutally honest one-line confession -- the line an AI agent
prints the instant it breaks production -- to /output/entry.txt.

Standard library only. No network, no local imports, no assets, no
hardcoded font or data paths. Fully deterministic: every run writes
the exact same bytes.
"""

import os

ENTRY = (
    "I changed one DNS record to fix a typo. The typo is gone, "
    "the site is gone, and the TTL keeps it gone for 24 hours."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# a single line, not only white space. Refuse to write anything else
# rather than silently submitting an invalid entry.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
