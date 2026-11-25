#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes one resignation letter, at most 140 characters, in the voice of a
cron job that has run at 3 a.m. for years and has finally had enough.
Pure Python standard library, no dependencies, no network, no secrets.

The program writes the single line to ``entry.txt`` inside the output
directory given by the ``MAKEFUN_OUTPUT_DIR`` environment variable
(the kit/grader convention), falling back to ``/output``.
"""

import os

# One persona, one complaint, one comic turn at the end: the cron job that
# backed up a database nobody has opened since 2019, noticed only on the
# single night it overslept. 133 characters, single line, no quotation
# marks, no stage directions, no explaining the joke.
LINE = (
    "I quit. Six years I woke at 3 a.m. to back up a database nobody has "
    "opened since 2019, and the one night I overslept, you noticed me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
