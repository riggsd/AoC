#!/usr/bin/env python3

import sys
from typing import Iterator, Tuple


def parse(infile) -> Iterator[str]:
    for line in infile:
        yield line.strip()


def split2(infile) -> Iterator[Tuple[str, str]]:
    for line in infile:
        n = len(line)
        yield line[:n//2], line[n//2:]


def split3(infile) -> Iterator[Tuple[str, str, str]]:
    infile = iter(infile)
    for line1 in infile:
        line2, line3 = next(infile), next(infile)
        yield line1, line2, line3


def pri(item: str) -> int:
    return '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(item)


def priority(items: set[str]) -> int:
    return sum(pri(item) for item in items)


input = list(parse(sys.stdin))

total1 = sum(priority(set(l) & set(r)) for (l, r) in split2(input))
print(total1)

total2 = sum(priority(set(a) & set(b) & set(c)) for (a, b, c) in split3(input))
print(total2)
