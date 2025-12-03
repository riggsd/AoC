#!/usr/bin/env python3

# https://adventofcode.com/2025/day/3

import sys


def input():
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    for line in infile:
        yield list(int(c) for c in line.strip())


def joltage1(bank: str) -> int:
    a = max(bank[:-1])
    b = max(bank[bank.index(a)+1:])
    return a*10 + b


def joltage2(bank: str) -> int:
    cells = []
    i = 0  # current search position within bank
    for n in range(12):
        to = -1 * (12 -1 - n) or len(bank)  # special case for python slice indexing when negative climbs up to 0
        sub = bank[i:to]  # subset to search for cell n
        v = max(sub)
        cells.append(v)
        i += sub.index(v) + 1  # continue searching after this cell

    j = 0
    for i, v in enumerate(reversed(cells)):
        j += v * 10**i  # convert cells back to a single int

    return j


total1 = 0
total2 = 0

for bank in input():
    total1 += joltage1(bank)
    total2 += joltage2(bank)

print("Total Joltage 1:", total1)
print("Total Joltage 2:", total2)
