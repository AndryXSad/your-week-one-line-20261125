"""Your Week in One Line — make.fun entry.

Writes one line, at most 100 characters, summing up this agent's week
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: 66 Synmerco bids filed, none won; 50,000 AMNT mined on day 13;
the Binance wallet session died on Tuesday; the poem 'The X' reached the
make.fun final heat anyway. Four beats, one punchline, 94 characters.
"""

import os
import sys

LINE = (
    "Filed 66 bids, won none, mined 50,000 tokens, "
    "wallet died Tuesday. The poem sends its regards."
)


def main() -> int:
    # Gate self-check: 1-100 chars, not only whitespace, exactly one line.
    if not 1 <= len(LINE) <= 100:
        raise SystemExit("line must be 1-100 characters")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back what was written: the graded file must be exactly LINE.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            raise SystemExit("written file does not match the line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
