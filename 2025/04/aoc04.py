#!/usr/bin/env python3

# https://adventofcode.com/2025/day/4

import sys
from copy import deepcopy


THRESHOLD = 4


def input():
    """Return input as 2D binary int grid"""
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    return [[1 if c == '@' else 0 for c in line.strip()] for line in infile]


def pprint(grid):
    """Print a grid"""
    for row in grid:
        print(''.join(' ' if not v else str(v) for v in row))


def add(grid, grid2, mask):
    """Add shifted grid2 onto grid, per the binary mask locations"""
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if mask[x][y]:
                grid[x][y] += grid2[x][y]


def shift(grid, x, y) -> list:
    """Calculate a shifted grid in the specified direction"""
    assert(x in {1, 0, -1})
    assert(y in {1, 0, -1})
    shifted = deepcopy(grid)

    if x == 1:
        shifted.pop(0)
        shifted.append(list(0 for i in range(len(shifted[0]))))
    elif x == -1:
        shifted.pop(-1)
        shifted.insert(0, list(0 for i in range(len(shifted[0]))))
    
    if y == 1:
        for row in shifted:
            row.pop(0)
            row.append(0)
    elif y == -1:
        for row in shifted:
            row.pop(-1)
            row.insert(0, 0)

    return shifted


def count_neighbors(grid) -> list:
    """From a binary grid, calculate a grid of neighbor counts"""
    neighbors = [[0 for _ in range(len(grid[x]))] for x in range(len(grid))]  # zero grid

    for x,y in [(-1,-1), (-1,0), (-1,1),
                ( 0,-1),          (0,1),
                ( 1,-1),  (1,0),  (1,1)]:
        add(neighbors, shift(grid, x, y), grid)
    
    return neighbors


def prune(neighbors, mask) -> int:
    """Remove all accessible rolls from grid and mask, and return the count"""
    pruned = 0
    for x in range(len(neighbors)):
        for y in range(len(neighbors[x])):
            if mask[x][y] and neighbors[x][y] < THRESHOLD:
                neighbors[x][y] = 0
                mask[x][y] = 0
                pruned += 1
    return pruned


grid = input()
neighbors = count_neighbors(grid)

# Part 1
accessible = 0
for x in range(len(neighbors)):
    for y in range(len(neighbors[x])):
        if grid[x][y] and neighbors[x][y] < THRESHOLD:
            accessible += 1
print("Accessible Rolls:", accessible)

# Part 2
total_removed = 0
while (removed := prune(neighbors, grid)) > 0:
    total_removed += removed
    #print(f"Remove {removed:4d} rolls")
    neighbors = count_neighbors(grid)
    #pprint(neighbors)
    #print()
print("Total Removed:", total_removed)
