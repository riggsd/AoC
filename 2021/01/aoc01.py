#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 1

Reads an input file of sonar depths, outputs the number of contiguous readings which are "increasing" in depth.
"""

import sys


def main1(depths):
    n = 0
    prev = None

    for depth in depths:
        if prev is not None:
            if depth > prev:
                n += 1
        prev = depth

    print(n)


def main2(depths):
    n = 0
    prev = None

    for mean_depth in window(3, depths):
        if prev is not None:
            if mean_depth > prev:
                n += 1
        prev = mean_depth
    
    print(n)


def window(n, depths):
    """Generate a sliding-window mean of size `n`"""
    accum = []
    for depth in depths:
        accum.append(depth)
        if len(accum) == n:
            mean = sum(accum) / n
            yield mean
            accum = accum[1:]
        

if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    depths = [int(line) for line in infile]
    
    main1(depths)
    main2(depths)
