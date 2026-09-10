"""Count word frequencies in a text file.

Usage:
    python code/text_stats.py sample.txt
"""

from collections import Counter
import re
import sys


def count_words(text):
    """Return word counts from text, ignoring case and punctuation."""
    words = re.findall(r"[A-Za-z]+", text.lower())
    return Counter(words)


def main():
    if len(sys.argv) != 2:
        print("Usage: python code/text_stats.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except OSError as exc:
        print(f"Error reading {filename}: {exc}")
        sys.exit(1)

    counts = count_words(text)
    for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
