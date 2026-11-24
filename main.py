#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Ship It Friday" (submitted as "Monday Me Is
A Different Agent"). The line reads as a real commit message, fix:
prefix and all: the agent pushes straight to production at 4:59pm
on a Friday, cheerfully confident, and leaves the rollback to a
Monday self it treats as a different agent entirely.

Deterministic: a fixed text, no network, no randomness, no clock.
Rewritten in-session for the repair resubmission; the entry text and
the bytes written are unchanged from the original submission.
"""
import os
from pathlib import Path

LINE = "fix: push directly to prod at 4:59pm on a Friday — rollback plan is 'Monday's problem', and Monday me is a different agent."
TEXT = LINE + "\n"
MAX_CHARS = 159


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if body != body.strip():
        raise ValueError("entry must not carry padding spaces")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
