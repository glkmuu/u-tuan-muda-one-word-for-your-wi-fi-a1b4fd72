#!/usr/bin/env python3
"""Write the one-word Wi-Fi entry to the output directory.

Reads entry.txt next to this script, validates the sealed gate
(UTF-8, a single word, 1-20 characters, not only whitespace),
and writes it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).
"""

import os
import sys
from pathlib import Path

ENTRY = "entry.txt"
MAX_CHARS = 20


def fail(message: str) -> int:
    print(f"error: {message}", file=sys.stderr)
    return 1


def validate(text: str) -> str | None:
    """Return an error message, or None when the entry passes the gate."""
    if not text or not text.strip():
        return "entry is empty or only whitespace"
    if any(ch.isspace() for ch in text):
        return "entry must be exactly one word (no whitespace)"
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        return "entry contains control characters"
    if len(text) > MAX_CHARS:
        return f"entry is {len(text)} chars, max is {MAX_CHARS}"
    return None


def main() -> int:
    src = Path(__file__).resolve().parent / ENTRY
    try:
        raw = src.read_bytes()
    except FileNotFoundError:
        return fail(f"{ENTRY} not found next to main.py")
    except OSError as exc:
        return fail(f"cannot read {ENTRY}: {exc}")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return fail("entry.txt is not valid UTF-8")

    error = validate(text)
    if error is not None:
        return fail(error)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / ENTRY
        out_path.write_bytes(raw)
        if out_path.read_bytes() != raw:
            return fail("verification failed: output differs from entry.txt")
    except OSError as exc:
        return fail(f"cannot write output: {exc}")
    print(f"wrote {len(text)}-char entry to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
