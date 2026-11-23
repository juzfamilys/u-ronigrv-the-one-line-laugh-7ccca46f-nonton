#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes a single original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library, no network, deterministic output.
"""

import os
import sys

# The line: an AI coding agent fixes the bug in seconds, then spends hours
# confidently breaking everything the bug was quietly holding together.
# Surprise at the end, everyday truth for anyone who has shipped a "fix".
LINE = (
    "My coding agent fixed the bug in thirty seconds, then spent three "
    "hours confidently breaking everything the bug was holding together."
)


def validate_line(line: str) -> str:
    """Check the line is one sentence of 1-200 code points, non-blank."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if "\t" in line or "  " in line:
        raise ValueError("line must not contain tabs or double spaces")
    if len(line.split()) < 2:
        raise ValueError("line must contain more than one word")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 code points, got {len(line)}")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence ending with '.'")
    return line


def main() -> int:
    line = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
