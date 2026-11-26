"""One-Line Roast: The Gadget You Use Every Day.

Writes one roast to /output/entry.txt: the phone battery quits at 4pm
like a union worker finishing its shift, and the charger is not its
problem. Pure Python 3.13 standard library, deterministic: no network,
no clock, no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

LINE = "My phone's battery dies at 4pm like it's unionised: it has worked its eight hours, it is going home, and my charger is not its problem."

# Bounty gate: the entry must be one line of 1-200 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    entry = LINE
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        print(
            f"invalid entry: {len(entry)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} range",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in entry or "\r" in entry:
        print("invalid entry: must be a single line", file=sys.stderr)
        sys.exit(1)
    if entry != entry.strip():
        print(
            "invalid entry: must not start or end with whitespace",
            file=sys.stderr,
        )
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, so the file holds
    # exactly the entry and nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
