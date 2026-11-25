"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes a single-line out-of-office email auto-reply to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python standard library; output is byte-identical on repeat runs.
"""

import os
from pathlib import Path

# The entry: one line, 98 characters, under the 160-character gate.
# The joke's turn: the auto-reply forwards your email to itself, and
# that reply is on holiday too — a real away message, just recursive.
LINE = "I'm on holiday. Your email has been forwarded to my out-of-office reply, which is also on holiday."


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, gate is 1-160"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
