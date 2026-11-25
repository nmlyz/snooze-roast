#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a roast of an alarm clock that
rings at 6 AM on a Saturday morning.

The line was picked from 36 candidates by pairwise judging against the
brief, with three reader personas scoring each pair on the brief's five
criteria in order. The winner mocks the alarm as a microwave beeping
for food nobody put in: a pointless noise for a meal that does not
exist, on a morning when nothing is scheduled. The punchline lands in
the last five words, the line is 85 characters, and every word earns
its place. The program holds the line as one constant and checks it
against the entry gate (length, single line, no leading or trailing
space) before writing it, then reads the file back to confirm the
bytes match.
"""

import os
import sys

LINE = (
    "At 6 AM on a Saturday my alarm rang like a microwave "
    "beeping for food I never put in."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
