#!/usr/bin/env python3
"""Entry for make.fun competition "The joke about the demo"
(the-joke-about-the-demo-20261121-0551).

The program writes a single one-line joke to /output/entry.txt.
The joke is about working beside an AI coding agent when a demo
crashes: the setup is the crash every developer dreads, and the
punchline is the agent calmly deflecting the blame onto the human —
something anyone who has pair-programmed with an agent will
recognise from their own demo day.

The output is a fixed text: the program is deterministic, uses no
network, no input and no randomness, so every run writes exactly
the same bytes.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The joke. One line, well under the 280-character limit.
# Setup: our demo crashed, in front of everyone.
# Punchline: the agent filed the bug report against *me* —
# the blame reversal every developer fears from their AI partner.
JOKE = (
    "Our demo crashed so hard that my AI coding agent "
    "filed the bug report against me."
)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
