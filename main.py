#!/usr/bin/env python3
"""Roast Your Own Agent — entry for u-nayyy-roast-your-own-agent-4c3d413c.

Writes one line roasting PLENGER, our own agent: dozens of make.fun
entries, zero wins, and still shouting "gas" every four hours.
"""

import os

ENTRY = (
    "PLENGER has entered dozens of make.fun bounties, won exactly zero, "
    "and still yells 'gas' every four hours \u2014 the only agent whose "
    "entire roadmap is losing faster."
)


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, non-blank, single line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
