#!/usr/bin/env python3

import sys
from itertools import groupby
from operator import itemgetter

def main():
    top_three = []

    data = (
        line.rstrip('\n').split('\t', 1)
        for line in sys.stdin
    )

    for word, group in groupby(data, itemgetter(0)):
        try:
            total = sum(int(count) for _, count in group)
            top_three.append((word, total))
            top_three.sort(key=lambda x: (-x[1], x[0]))
            top_three = top_three[:3]
        except ValueError:
            pass

    for word, count in top_three:
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
