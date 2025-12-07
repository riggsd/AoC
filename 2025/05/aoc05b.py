#!/usr/bin/env python3

# https://adventofcode.com/2025/day/5

import sys


def input():
    """list of ranges and list of ingredient IDs"""
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    ranges, ingredients = [], []
    for line in infile:
        if '-' in line:
            ranges.append([int(v) for v in line.split('-')])
        elif line.strip():
            ingredients.append(int(line))
    return ranges, ingredients


def overlap(r1, r2):
    """Given two range tuples, determine whether their start/ends overlap"""
    return r1[0] <= r2[1] and r2[0] <= r1[1]

def normalize(ranges):
    """Rewrite the list of ranges so that there's no overlap between ranges"""
    # our strategy is to sort the ranges by their starting point, compare each to all subsequent
    # ranges, and if we find any overlap we "grow" the range to encompass both, thowing out the
    # redundant range
    new_ranges = []
    ranges = sorted(ranges, key = lambda r: r[0])
    while ranges:
        r1 = ranges.pop(0)
        to_delete = []
        for r2 in ranges:
            if overlap(r1, r2):
                # we know r1 starts <= r2 because sorted, so use the largest of the two ends
                r1[1] = max(r1[1], r2[1])
                # now that our new range covers both these ranges, get rid of the redundant one
                to_delete.append(r2)
        
        for r2 in to_delete:
            ranges.remove(r2)

        new_ranges.append(r1)
    
    return new_ranges


ranges, ids = input()
ranges = normalize(ranges)

total = 0
for start, end in ranges:
    total += 1 + end - start
print("Total Fresh:", total)
