#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 7
https://adventofcode.com/2021/day/7

Reads an input file of horizontal positions, optimizes fuel cost for aligning them.
"""

import sys
from array import array
from functools import cache
from statistics import median


def main1(positions):
    mid = median(positions)
    fuel = sum([abs(pos - mid) for pos in positions])
    print(f'1. Burn {fuel} fuel aligning to position {mid}.')


def main2(positions):
    # I am embarassed by this O(n**2) bruteforce solution, but the ends justify the means!
    a = array('L', [calculate_fuel(positions, end) for end in range(min(positions), max(positions)+1)])
    fuel = min(a)
    end = [i for i, val in enumerate(a) if val == fuel][0]
    print(f'2. Burn {fuel} fuel aligning to position {end}.')

def calculate_fuel(positions, end):
    """Calculate total fuel cost to move all crabs to end point"""
    return sum([calculate_crab(pos, end) for pos in positions])

@cache
def calculate_crab(start, end):
    """Calculate fuel cost for a single crab moving from start -> end"""
    dist = abs(end - start)
    fuel = 0
    for i in range(1, dist+1):
        fuel += i
    return fuel


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    positions = list(map(int, infile.readline().split(',')))
    
    main1(positions)
    main2(positions)
