#!/usr/bin/env python3
"""Everyday Wonder — one-sentence wonder writer.

Writes a single original sentence (<=200 chars) about a small everyday
moment to /output/entry.txt.
"""
import os

SENTENCE = "The escalator handrail outruns the steps, so my hand keeps arriving a half-second before the rest of me."

def main():
    # Exactly one sentence: no trailing newline, no extra whitespace.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
