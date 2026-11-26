#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single original warning label for a time machine to
/output/entry.txt. Stdlib only, deterministic: the same label every run.
"""

import os
from pathlib import Path

LABEL = (
    "WARNING: Do not exit before your grandfather was born. "
    "He still needs a lift to meet your grandmother."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LABEL, encoding="utf-8")


if __name__ == "__main__":
    main()
