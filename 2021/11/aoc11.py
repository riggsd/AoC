#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 11
https://adventofcode.com/2021/day/11

Reads an input file of bioluminescent octopus values, simulates their flashing.
"""

import sys
from array import array
from collections import namedtuple

Point = namedtuple('P', 'x y')


def main1(grid, steps=100):
    """Count the total flashes after 100 steps"""
    flashes = 0
    for i in range(steps):
        print(f'\nStep: {i+1}\tFlashes:{flashes}')
        print_grid(grid)
        flashes += step(grid)
    print(flashes)

def step(grid):
    """Simulate a single time step"""
    # 1. Increment all values by 1
    # 2. Find all coords with value 10, which will flash this step
    flashers = []
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            row[y] += 1
            if row[y] == 10:
                flashers.append( Point(x,y) )
    # 3. Flash, which prapogates to adjacent coordinates, and may recursively trigger their flash
    for p in flashers:
        flash(grid, p)
    # 4. Restore all the flashed 10's to energy 0, return total number that flashed
    flashed = 0
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val == 10:
                row[y] = 0
                flashed += 1
    return flashed

def flash(grid, p):
    """Flash an octopus at point p, energizing all of its neighbors"""
    h, w = len(grid), len(grid[0])
    x, y = p
    grid[x][y] = 10
    def energize(x, y):
        if grid[x][y] == 10:
            return  # already flashed this step
        grid[x][y] += 1
        if grid[x][y] == 10:
            flash(grid, Point(x,y))  # recursive flash
    if x > 0:               energize(x-1, y)    # N
    if x > 0 and y < w-1:   energize(x-1, y+1)  # NE
    if y < w-1:             energize(x, y+1)    # E
    if y < w-1 and x < h-1: energize(x+1, y+1)  # SE
    if x < h-1:             energize(x+1, y)    # S
    if x < h-1 and y > 0:   energize(x+1, y-1)  # SW
    if y > 0:               energize(x, y-1)    # W
    if y > 0 and x > 0:     energize(x-1, y-1)  # NW


def print_grid(grid, cmap='\u2588123456789'):
    """Print the grid, highlighting octopi who flashed this step"""
    h, w = len(grid), len(grid[0])
    print('  ' + ''.join(str(i % 10) for i in range(0, w)))
    print('  ' + '-' * w)
    for x, row in enumerate(grid):
        print(f'{x % 10}|' + ''.join(cmap[v] for v in row))


def main2(grid):
    """Find the step where they all flash simultaneously"""
    i = 0
    while any([any(row) for row in grid]):
        print(f'\nStep: {i+1}')
        print_grid(grid)
        step(grid)
        i += 1
    print(f'\nStep: {i}')
    print_grid(grid)


def parse(infile):
    """Parse a grid as list of arrays of ints"""
    return list([array('B', map(int, line.strip())) for line in infile])


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    grid = parse(infile)
    main1(grid)

    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    grid = parse(infile)
    main2(grid)
