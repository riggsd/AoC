#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 14
https://adventofcode.com/2021/day/14

Reads an input file consisting of a polymer and insertion rules, and calculates the polymer chain after n steps

We model the polymer in two pieces:
- One dict keeping track of every element-pair and its count, so that we can calculate the next step
- One dict keeping track of individual element counts, which grow with each insertion

We can't derive one from the other, because we throw away *position* by modeling it this way. And we *must*
model it this way, because the polymer string would be 20.9-trillion characters long (~21TB) after 40 steps!
"""

import sys
from collections import defaultdict


def main(polymer:dict, element_counts:dict, insertions:dict, n:int):
    for i in range(n):
        replacements = defaultdict(int)
        for pair, count in polymer.copy().items():
            if pair in insertions:
                pair1 = pair[0] + insertions[pair]
                pair2 = insertions[pair] + pair[1]
                print(f'\t{count}\t{pair} -> {pair1} {pair2}')
                del polymer[pair]
                replacements[pair1] += count
                replacements[pair2] += count
                element_counts[insertions[pair]] += count
            else:
                print('\t', pair)
        polymer.update(replacements)
        print(f'Step {i+1}  Size: {sum(element_counts.values())}')
    
    stats = sorted(element_counts.items(), key=lambda kv: kv[1])
    most, least = stats[-1], stats[0]
    print('Final Element Counts:', stats)
    print(f'Most: {most}  Least: {least}')
    print(f'Score after {n} steps: {most[1] - least[1]}')


def parse(lines):
    """
    Parse input file and produce three values:
    - initial polymer as a dict of element-pair strings
    - initial individual element counts as dict
    - dict of insertion rules, element-pair to insertion element
    """
    polymerstr = lines[0]

    insertions = {}
    for line in lines[2:]:
        a, b = line.strip().split(' -> ')
        insertions[a] = b

    polymer = defaultdict(int)
    for j in range(len(polymerstr)-1):
        pair = polymerstr[j:j+2]
        polymer[pair] += 1

    element_counts = defaultdict(int)
    for element in polymerstr:
        element_counts[element] = polymerstr.count(element)

    return polymer, element_counts, insertions


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    lines = list([line.strip() for line in infile.readlines()])

    polymer, element_counts, insertions = parse(lines)
    main(polymer, element_counts, insertions, 10)

    polymer, element_counts, insertions = parse(lines)
    main(polymer, element_counts, insertions, 40)
