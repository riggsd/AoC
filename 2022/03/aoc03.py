#!/usr/bin/env python3

import sys
from typing import Iterator, Tuple


def split2(infile) -> Iterator[Tuple[set, set]]:
    for line in infile:
        n = len(line)
        yield set(line[:n//2]), set(line[n//2:])


def split3(infile) -> Iterator[Tuple[set, set, set]]:
    infile = iter(infile)
    for line1 in infile:
        line2, line3 = next(infile), next(infile)
        yield set(line1), set(line2), set(line3)


def priority(items: set[str]) -> int:
    return sum('_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(item) for item in items)


input = list(line.strip() for line in sys.stdin)

total1 = sum( priority(l & r) for (l, r) in split2(input) )
print(total1)

total2 = sum( priority(a & b & c) for (a, b, c) in split3(input) )
print(total2)
