#!/usr/bin/env python3

import sys
from functools import reduce


def parse(infile):
    for line in infile.readlines():
        yield [int(col) for col in list(line.strip())]


def walk(input):
    for r, row in enumerate(input):
        for c, val in enumerate(row):
            yield r, c


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
grid = list(parse(infile))
W, H = len(grid[0]), len(grid)


def visible(r, c) -> bool:
    val = grid[r][c]
    if all(n < val for n in [grid[i][c] for i in range(0, r)]):
        return True
    if all(s < val for s in [grid[i][c] for i in range(r + 1, H)]):
        return True
    if all(w < val for w in [grid[r][i] for i in range(0, c)]):
        return True
    if all(e < val for e in [grid[r][i] for i in range(c + 1, W)]):
        return True
    return False


def score(r, c) -> int:
    val = grid[r][c]
    scores = {'N': 0, 'S': 0, 'W': 0, 'E': 0}

    for n in reversed([grid[i][c] for i in range(0, r)]):
        scores['N'] += 1
        if n >= val:
            break

    for s in [grid[i][c] for i in range(r + 1, H)]:
        scores['S'] += 1
        if s >= val:
            break

    for w in reversed([grid[r][i] for i in range(0, c)]):
        scores['W'] += 1
        if w >= val:
            break

    for e in [grid[r][i] for i in range(c + 1, W)]:
        scores['E'] += 1
        if e >= val:
            break

    return reduce(lambda a, b: a * b, scores.values())


# Part 1
n = 0
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if visible(r, c):
            n += 1
            print(val, end='')
        else:
            print('.', end='')
    print()

print()
print(f'1. Visible Trees: {n}')


# Part 2
most_scenic = max(score(r, c) for (r, c) in walk(grid))
print(f'2. Most Scenic: {most_scenic}')
