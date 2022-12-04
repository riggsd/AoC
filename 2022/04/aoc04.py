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


def fully_contains(a: set, b: set) -> bool:
    return not a - b or not b - a


def overlaps(a: set, b: set) -> bool:
    return bool(a & b)


input = list(parse(sys.stdin))

n1 = len([pair for pair in input if fully_contains(*pair)])
print(n1)

n2 = len([pair for pair in input if overlaps(*pair)])
print(n2)
