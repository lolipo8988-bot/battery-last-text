#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — a one-line make.fun entry.

The line is built in three beats, the way a last text is actually typed:
the sacrifices made to survive the day, the twist (the charger was in the
same pocket all along, unplugged), and a punchline that pays off on the
double meaning of "contact" — electrical and emotional.
"""
import os
from pathlib import Path

# Beat 1 — what the battery gave up to last until the charger arrived.
SACRIFICES = (
    "I dimmed, I killed every app I loved, "
    "I held on at 1% all day for you"
)
# Beat 2 — the twist: the charger never had to travel. It just had to plug in.
TWIST = "and you were in my pocket the whole time. Unplugged."
# Beat 3 — the payoff, saved for the final words.
PUNCHLINE = "We could've been electric. You just never made contact."


def build_entry() -> str:
    """Assemble the three beats into the battery's single last line."""
    return f"{SACRIFICES} \u2014 {TWIST} {PUNCHLINE}"


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
