#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 14
https://adventofcode.com/2021/day/14

Reads an input file consisting of a polymer and insertion rules, and calculates the polymer chain after n steps
"""

import sys
from collections import defaultdict


def main(polymer, insertions, n):
    for i in range(n):
        print(f'Step {i}: size {len(polymer)}')
        replacement = []
        for j in range(len(polymer)-1):
            pair = polymer[j:j+2]
            #print('\t', pair)
            replacement.append(pair[0] + insertions.get(pair, ''))
        replacement.append(pair[1])
        polymer = ''.join(replacement)
    counts = quantify(polymer)
    stats = sorted(counts.items(), key=lambda kv: kv[1])
    most, least = stats[-1][1], stats[0][1]
    print(f'After {n} steps: {most - least}')

def quantify(polymer):
    counts = defaultdict(int)
    for c in polymer:
        counts[c] += 1
    return counts

def parse(infile):
    polymer = infile.readline().strip()
    infile.readline()

    insertions = {}
    for line in infile:
        a, b = line.strip().split(' -> ')
        insertions[a] = b

    return polymer, insertions


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    polymer, insertions = parse(infile)

    main(polymer, insertions, 10)
    main(polymer, insertions, 40)
