#!/usr/bin/env python3

# https://adventofcode.com/2025/day/5

import sys


def input():
    """list of ranges and list of ingredient IDs"""
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    ranges, ingredients = [], []
    for line in infile:
        if '-' in line:
            ranges.append([int(v) for v in line.split('-')])
        elif line.strip():
            ingredients.append(int(line))
    return ranges, ingredients


ranges, ids = input()

fresh = 0
for id in ids:
    for start, end in ranges:
        if start <= id <= end:
            fresh += 1
            break

print("Fresh Ingredients:", fresh)
