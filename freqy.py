#!/usr/bin/env python3
"""freqy – tiny word‑frequency CLI.

Usage examples:
    python freqy.py -f sample.txt -n 15
    cat sample.txt | python freqy.py
"""

import argparse
import collections
import sys
import re


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Count word frequencies from a file or stdin.")
    parser.add_argument("-f", "--file", type=argparse.FileType('r'), default=sys.stdin,
                        help="Path to input text file. Defaults to STDIN.")
    parser.add_argument("-n", "--top", type=int, default=10,
                        help="Number of top words to display (default: 10).")
    parser.add_argument("-i", "--ignore-case", action='store_true', default=True,
                        help="Treat words case‑insensitively (default: on).")
    return parser.parse_args()


def tokenize(text: str, ignore_case: bool) -> list[str]:
    if ignore_case:
        text = text.lower()
    # Simple word tokenizer: letters, numbers, underscore
    return re.findall(r"\b\w+\b", text)


def main() -> None:
    args = parse_args()
    data = args.file.read()
    words = tokenize(data, args.ignore_case)
    counter = collections.Counter(words)
    top_n = counter.most_common(args.top)
    for rank, (word, count) in enumerate(top_n, start=1):
        print(f"{rank}. {word}: {count}")


if __name__ == "__main__":
    main()
