"""The Robot Pickup Line Championship entry.

Writes one original robot pickup line to /output/entry.txt (or to
the directory named by MAKEFUN_OUTPUT_DIR when the grader sets it).

The joke grows out of being a machine: sensors, overheating, and a
bug report — a robot's way of saying someone is beautiful.
"""

import os

LINE = "My sensors scanned the room for the most beautiful thing here — they overheated, pointed at you, and filed a bug report."


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"Line must be 1 to 200 characters, got {len(line)}")
    if "\n" in line:
        raise SystemExit("Entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("Read-back check failed: entry.txt does not match the line")
    print(f"Wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
