#!/usr/bin/env python3

import sys
from typing import Iterator


def elf_range(s: str) -> tuple[int, int]:
    return tuple(int(n) for n in s.split('-'))


def parse(infile) -> Iterator[tuple[set, set]]:
    for line in infile:
        pair = [elf_range(r) for r in line.strip().split(',')]
        a, b = pair[0], pair[1]
        yield set(range(a[0], a[1]+1)), set(range(b[0], b[1]+1))


def fully_contains(pair: tuple) -> bool:
    return not pair[0] - pair[1] or not pair[1] - pair[0]


def overlaps(pair: tuple) -> bool:
    return pair[0] & pair[1]


input = list(parse(sys.stdin))

n1 = len([pair for pair in input if fully_contains(pair)])
print(n1)

n2 = len([pair for pair in input if overlaps(pair)])
print(n2)
