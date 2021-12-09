#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 9
https://adventofcode.com/2021/day/

Reads an input file of Digital Elevation Model, finds topographic lows.
"""

import sys
from array import array


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


def parse(infile):
    return list([array('B', map(int, line.strip())) for line in infile])

if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    dem = parse(infile)
    
    main1(dem)
