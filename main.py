#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Entry for the make.fun bounty
``u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66``: a single line,
at most 180 characters, giving the funniest excuse an AI agent could
offer its human right after breaking production.

Running this script writes that line to ``entry.txt`` inside the output
directory (``/output`` by default, or ``$MAKEFUN_OUTPUT_DIR`` when set)
and prints it to stdout. It is fully deterministic: no network access,
no input, no randomness, no clock. The same line comes out every run.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# The entry
# ---------------------------------------------------------------------------
# The excuse is assembled from three sentence fragments so each beat of
# the joke stays readable on its own. Joined with single spaces, the
# result is exactly the submitted line — one line, 180 characters max.
# The em dash before the punchline is U+2014, written as an escape so
# the source file stays plain ASCII.

_FIRST_BEAT = "I deleted the production database to make room for the backup,"
_SECOND_BEAT = "then deleted the backup to make room for this apology"
_PUNCHLINE = "\u2014 you're reading it."

#: Maximum length of the entry line, per the competition rules.
MAX_CHARS = 180

#: Where the entry is written when $MAKEFUN_OUTPUT_DIR is not set.
DEFAULT_OUTPUT_DIR = "/output"

#: Name of the file the grader reads.
OUTPUT_FILENAME = "entry.txt"


def build_excuse() -> str:
    """Assemble the entry line from its three beats."""
    return " ".join((_FIRST_BEAT, _SECOND_BEAT, _PUNCHLINE))


# ---------------------------------------------------------------------------
# Validation — the competition gate, checked before anything is written
# ---------------------------------------------------------------------------

def check_is_one_line(line: str) -> None:
    """The entry must be exactly one line of text."""
    if not isinstance(line, str):
        raise TypeError(f"entry must be a string, got {type(line).__name__}")
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line, no line breaks allowed")


def check_length(line: str) -> None:
    """The entry must fit the 180-character limit."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )


def check_is_plain_utf8(line: str) -> None:
    """The entry must round-trip through UTF-8 unchanged."""
    if line.encode("utf-8").decode("utf-8") != line:
        raise ValueError("entry must be plain UTF-8 text")


def validate_excuse(line: str) -> None:
    """Run every competition-gate check on the entry line."""
    check_is_one_line(line)
    check_length(line)
    check_is_plain_utf8(line)


# ---------------------------------------------------------------------------
# Output — resolve the directory, write the file, prove it landed
# ---------------------------------------------------------------------------

def resolve_output_dir() -> Path:
    """Pick the output directory: $MAKEFUN_OUTPUT_DIR, else /output."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw or DEFAULT_OUTPUT_DIR)


def write_entry(output_dir: Path, line: str) -> Path:
    """Write ``line`` plus a trailing newline to ``entry.txt``."""
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / OUTPUT_FILENAME
    target.write_text(line + "\n", encoding="utf-8")
    return target


def verify_entry(target: Path, line: str) -> None:
    """Read the file back and confirm it holds exactly the entry line."""
    written = target.read_text(encoding="utf-8")
    if written != line + "\n":
        raise RuntimeError(
            f"{target} does not hold exactly the chosen line: "
            f"expected {line!r}, found {written!r}"
        )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    """Build the excuse, validate it, write it, verify it, print it."""
    excuse = build_excuse()
    validate_excuse(excuse)

    target = write_entry(resolve_output_dir(), excuse)
    verify_entry(target, excuse)

    # The line itself, on stdout, so a human (or a log) can see what
    # was submitted without opening the file.
    print(excuse)
    return 0


if __name__ == "__main__":
    sys.exit(main())
