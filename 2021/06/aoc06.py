#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 5
https://adventofcode.com/2021/day/5

Reads an input file of "fish" modeled as numbers, calculates exponential growth.
"""

import sys
from collections import defaultdict


def main(fishes, days):
    school = defaultdict(int)  # age -> count

    for fish in fishes:
        school[fish] += 1  # initial state

    for day in range(1, days+1):
        # iterate up from 1 to 8 since each tick propogates downward
        # handle 0 last so they don't get counted twice
        zeros = school[0]
        for i in range(1, 8+1):
            school[i-1] = school[i]
        school[8] = zeros
        school[6] += zeros
    
    print(f'Day {day}:\t{sum(school.values())} lanternfish')


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    fishes = list(map(int, infile.readline().split(',')))
    
    main(fishes, 80)
    main(fishes, 256)
