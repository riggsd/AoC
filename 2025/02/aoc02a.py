#!/usr/bin/env python3

# https://adventofcode.com/2025/day/2

import sys


def input():
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    for tok in infile.read().split(','):
        start, end = tok.split('-')
        yield int(start), int(end)


def valid1(id: int) -> bool:
    idstr = str(id)
    if len(idstr) % 2:
        return True   # any odd length ID must be valid
    mid = len(idstr) // 2
    a, b = idstr[mid:], idstr[:mid]
    if a == b:
        return False  # pair of matched halves is invalid
    else:
        return True   # not two matching halves, so valid


sum = 0

for start, end in input():
    for id in range(start, end+1):
        if not valid1(id):
            sum += id

print('Invalid Sum:', sum)
