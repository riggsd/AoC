#!/usr/bin/env python3

# https://adventofcode.com/2025/day/7

import sys


def input():
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    return [list(line.strip()) for line in infile]


splits = 0

data = input()

row = data.pop(0)
i   = row.index('S')  # initial beam
row[i] = '|'
print(''.join(row))
beams = [i]

for row in data:
    beams = list(set(beams))  # remove dupes
    to_split = []
    for i in beams:
        if row[i] == '.':
            row[i] = '|'
        elif row[i] == '^':
            splits += 1
            row[i-1] = row[i+1] = '|'
            to_split += [i]
    for j in to_split:
        beams.remove(j)
        beams += [j-1, j+1]
    print(''.join(row))

print('Beam Splits:', splits)
