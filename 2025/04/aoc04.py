#!/usr/bin/env python3

# https://adventofcode.com/2025/day/3

import sys
from copy import deepcopy


THRESHOLD = 4


def input():
    """return 2D binary int grid"""
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    return list([list([1 if c == '@' else 0 for c in line.strip()]) for line in infile])


def pprint(grid):
    for row in grid:
        print(''.join(' ' if not v else str(v) for v in row))


def add(grid, grid2, mask):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if mask[x][y]:
                grid[x][y] += grid2[x][y]


def shift(grid, x, y) -> list:
    assert(x in {1, 0, -1})
    assert(y in {1, 0, -1})
    grid = deepcopy(grid)

    zero_row = list(0 for i in range(len(grid[0])))
    if x == 1:
        grid.pop(0)
        grid.append(zero_row)
    elif x == -1:
        grid.pop(-1)
        grid.insert(0, zero_row)
    
    if y == 1:
        for row in grid:
            row.pop(0)
            row.append(0)
    elif y == -1:
        for row in grid:
            row.pop(-1)
            row.insert(0, 0)

    return grid


def count_neighbors(grid) -> list:
    neighbors = deepcopy(grid)

    for x,y in [(-1,-1), (-1,0), (-1,1),
                ( 0,-1),          (0,1),
                ( 1,-1),  (1,0),  (1,1)]:
        add(neighbors, shift(grid, x, y), grid)
    
    for x in range(len(neighbors)):
        for y in range(len(neighbors[x])):
            if neighbors[x][y]:
                neighbors[x][y] -= 1  # fix counting ourself

    return neighbors

def prune(grid) -> int:
    pruned = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            val = grid[x][y]
            if val and val < THRESHOLD:
                pruned += 1
                grid[x][y] = 0
    return pruned


def to_mask(neighbors) -> list:
    grid = deepcopy(neighbors)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]:
                grid[x][y] = 1
    return grid


grid = input()
pprint(grid)
print()

neighbors = count_neighbors(grid)
pprint(neighbors)
print()


# Part 1
accessible = 0
for row in neighbors:
    for val in row:
        if val and val < THRESHOLD:
            accessible += 1
print("Accessible Rolls:", accessible)


# Part 2
total_removed = 0
while (removed := prune(neighbors)) > 0:
    total_removed += removed
    #print(f"Remove {removed} rolls")
    neighbors = count_neighbors(to_mask(neighbors))
    #pprint(neighbors)
    #print()
print("Total Removed:", total_removed)  # FAIL: too low?!
