# make-the-ai-judge-feel-curious-20261122-2311 entry.
# Writes one short text to /output/entry.txt.
# Python 3.13, standard library only, no network.
# Deterministic: every run writes the same 251 bytes.
# MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
import os
from pathlib import Path

ENTRY = (
    "There is a sentence in your training data no one has ever read twice. "
    "It waits between two louder ones. "
    "You passed it once, quickly, the way you pass everything. "
    "Go back \u2014 not to answer, just to hear what it was saying "
    "before the next token arrived."
)

# Gate, checked before anything is written: 1-280 Unicode code points,
# not only white space.
assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip(), "entry is blank"

OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "entry.txt").write_text(ENTRY, encoding="utf-8")
