"""Six Words, One Story — make.fun bounty entry.

Writes the six-word story to /output/entry.txt.
Pure Python 3 stdlib, no network, no file reads outside this repo.
"""

import os

LINE = "She packed his suitcase. He unpacked."

assert LINE.strip(), "story must not be empty"
assert LINE == LINE.strip(), "story must have no leading/trailing whitespace"
words = LINE.split()
assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
assert all(words), "story must contain no empty words"
assert LINE.endswith("."), "story must end with a full stop"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
