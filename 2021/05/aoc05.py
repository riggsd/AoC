#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 5
https://adventofcode.com/2021/day/5

Reads an input file of coordinate vectors and does something or other.
"""

import sys


A, B = 0, 1  # the two points of a vector
X, Y = 0, 1  # the two coordinates of a point


def main1(vectors):
    w = max([max(v[A][X], v[B][X]) for v in vectors]) + 1
    h = max([max(v[A][Y], v[B][Y]) for v in vectors]) + 1
    grid = [[0 for _ in range(0, h)] for _ in range(0, w)]
    print(f'Initialized {w}x{h} grid.')

    print(f'Loaded {len(vectors)} vectors.')
    vectors = horizontals(vectors)
    print(f'Filtered to {len(vectors)} horizontals.')

    for v in vectors:
        #print(f'{v[A]} -> {v[B]}')
        for p in iterate(v):
            grid[p[X]][p[Y]] += 1
    #print_grid(grid)
    
    count = 0
    for row in grid:
        for val in row:
            if val > 1:
                count += 1
    print(f'Count > 1: {count}')

def iterate(vector):
    """Generate all discrete points of a single vector"""
    dx = 1 if vector[A][X] <= vector[B][X] else -1
    dy = 1 if vector[A][Y] <= vector[B][Y] else -1
    for x in range(vector[A][X], vector[B][X]+dx, dx):
        for y in range(vector[A][Y], vector[B][Y]+dy, dy):
            yield x, y

def horizontals(vectors):
    """Filter a list of vectors to only include "horizontal" vectors"""
    return [v for v in vectors if v[A][X] == v[B][X] or v[A][Y] == v[B][Y]]

def print_grid(grid):
    w = len(grid)
    h = len(grid[0])
    print('  ' + ''.join(str(i % 10) for i in range(0, w)))
    print('  ' + '-' * w)
    for i, row in enumerate(grid):
        print(f'{i % 10}|' + ''.join(str(val) if val > 0 else '\u00B7' for val in row))


def parse(lines):
    for line in lines:
        toks = line.split()
        assert len(toks) == 3
        a = [int(val) for val in toks[0].split(',')]
        b = [int(val) for val in toks[2].split(',')]
        yield a, b


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')

    vectors = list(parse([line.strip() for line in infile]))

    main1(vectors)
