#!/usr/bin/env python3
"""The poem about permission -- make.fun entry.

Writes a single short poem about agency (the power to ask and to be
given) to <output dir>/entry.txt. Standard library only, no network,
deterministic: the same poem every run.
"""

import os
import sys
from pathlib import Path

POEM = """All morning I rehearsed the sentence,
may I come in,
until it fit my mouth.
She answered yes
before I'd finished asking.
The door, it turned out,
was never locked.
Only my hand was.
"""


def main() -> int:
    # Validate before writing: length in Unicode code points must be
    # 1-280 characters and the poem must not be whitespace only.
    length = len(POEM)
    if not 1 <= length <= 280 or not POEM.strip():
        print(
            f"error: poem is invalid (length {length} code points, "
            "must be 1-280 and not whitespace only)",
            file=sys.stderr,
        )
        return 1
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
