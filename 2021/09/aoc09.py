#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 9
https://adventofcode.com/2021/day/9

Reads an input file of Digital Elevation Model, finds topographic lows / basins.
"""

import sys
from array import array
from collections import namedtuple
from math import prod


Point = namedtuple('P', 'x y')


def main1(dem):
    print(sum(map(risk, lows(dem))))

def lows(dem):
    for x, row in enumerate(dem):
        for y, elevation in enumerate(row):
            if is_low(dem, (x, y)):
                yield elevation

def is_low(dem, coordinate) -> bool:
    h, w = len(dem), len(dem[0])
    x, y = coordinate
    val = dem[x][y]
    def neighbors():
        if y < w-1: yield dem[x][y+1]
        if x < h-1: yield dem[x+1][y]
        if y > 0:   yield dem[x][y-1]
        if x > 0:   yield dem[x-1][y]
    return all(val < neighbor for neighbor in neighbors())

def risk(elevation: int) -> int:
    return elevation + 1


def main2(dem):
    """
    Since we only care about the size of basins, model them like this:
    - a point is an (x,y) tuple
    - a basin is a set of points
    - a slice is a set of points, horizontally contiguous, between ridges

    We'll scan row by row, building basins slice by slice.
    """
    print_dem(dem)
    print()

    basins = []
    for x, row in enumerate(dem):
        for slice in list(slices(x, row)):
            matched_basin = None
            for basin in basins.copy():
                if is_adjacent(slice, basin):
                    if not matched_basin:
                        basin.update(slice)          # old basin grows
                        matched_basin = basin
                    else:
                        basins.remove(basin)
                        matched_basin.update(basin)  # coalesce two basins
            if not matched_basin:
                basins.append(slice)                 # new basin
    
    print()
    print(f'Found {len(basins)} basins!')
    print()

    top = sorted(basins, key=lambda basin: len(basin), reverse=True)[:3]
    assert len(top) == 3
    print(f'Top {len(top)} basins:')
    for basin in top:
        print(f'{len(basin)}\t{sorted(basin)}')
    
    print()
    print('Answer:', prod(map(len, top)))  # Fail! 878430 is too low

def print_dem(dem, cmap='012345678\u2588'):
    h, w = len(dem), len(dem[0])
    print('  ' + ''.join(str(i % 10) for i in range(0, w)))
    print('  ' + '-' * w)
    for x, row in enumerate(dem):
        print(f'{x % 10}|' + ''.join(cmap[v] for v in row))

def slices(x, row):
    """Produce all the basin slices in a row"""
    slice = set()
    for y, v in enumerate(row):
        if v != 9:
            slice.update({Point(x,y)})
            continue
        if slice:
            yield slice
            slice = set()
    if slice:
        yield slice  # rightmost edge

def is_adjacent(slice, basin) -> bool:
    """Is this slice adjacent to (ie. part of) the basin?"""
    x = list(slice)[0].x
    sub_basin = {p for p in basin if abs(p.x - x) == 1}
    for p1 in slice:
        if any(filter(lambda p2: p2.y == p1.y, sub_basin)):
            return True
    return False


def parse(infile):
    """Parse a DEM as list of arrays of ints"""
    return list([array('B', map(int, line.strip())) for line in infile])

if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    dem = parse(infile)
    
    main1(dem)
    main2(dem)
