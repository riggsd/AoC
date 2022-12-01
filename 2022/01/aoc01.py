#!/usr/bin/env python3

import sys
from typing import Iterator, TextIO


def parse(infile: TextIO) -> Iterator[int]:
    """Yield the total calorie count for each elf"""
    total = 0
    for line in infile:
        line = line.strip()
        if not line:
            yield total
            total = 0
        else:
            total += int(line)


counts = list(parse(sys.stdin))

top1 = max(counts)
print(top1)

top3 = sorted(counts)[-3:]
print(sum(top3))

