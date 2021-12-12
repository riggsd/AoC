#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 12
https://adventofcode.com/2021/day/12

Reads an input file representing a graph of cave passages, exhaustively solves for routes.
"""

import sys
from collections import defaultdict
from functools import cache
from queue import LifoQueue as Queue


def main(cave, is_valid):
    solutions = []
    q = Queue()

    for seg in cave['start']:
        q.put( ['start', seg] )

    while not q.empty():
        route = q.get()
        routes = filter(is_valid, [route + [seg] for seg in cave[route[-1]]])
        for route in routes:
            if route[-1] == 'end':
                solutions.append(route)
            else:
                q.put(route)
    
    print('Solutions:')
    for route in sorted(solutions, key=len):
        print(','.join(route))
    print('Total:', len(solutions))

@cache
def is_little(seg: str) -> bool:
    return seg.islower() 


def is_valid1(route: list) -> bool:
    """Part 1: no little cave may be visited more than once"""
    return all([route.count(seg) == 1 for seg in route if is_little(seg)])


def is_valid2(route: list) -> bool:
    """Part 2: at most, one little cave may be visited twice"""
    visited_twice = None
    for seg in route:
        if not is_little(seg):
            continue                 # no limit on big segments
        n = route.count(seg)
        if n == 1:
            continue
        if n > 2:
            return False             # never allowed to visit littles more than twice
        if seg in {'start', 'end'}:  # can't visit terminal nodes more than once
            return False
        elif n == 2 and visited_twice and seg != visited_twice:
            return False             # exceeded our "one little twice" allowance
        elif n == 2:
            visited_twice = seg
    return True


def parse(infile) -> dict:
    """Parse a cave (undirected cyclic graph) as dict of list of segment names"""
    cave = defaultdict(list)
    for line in infile:
        a, b = line.strip().split('-')
        cave[a].append(b)
        cave[b].append(a)
    return cave

if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    cave = parse(infile)

    main(cave, is_valid1)
    main(cave, is_valid2)
