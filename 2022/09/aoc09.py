#!/usr/bin/env python3

import sys
from itertools import pairwise
from typing import Iterator


def parse(infile) -> Iterator[tuple[str, int]]:
    for line in infile:
        direction, steps = line.strip().split()
        yield direction, int(steps)


def compare(head, tail) -> tuple[int, int]:
    return abs(head[0] - tail[0]), abs(head[1] - tail[1])


def distance(head, tail) -> int:
    return max(compare(head, tail))


def move(head, direction):
    match direction:
        case 'U':
            head[0] += 1
        case 'D':
            head[0] -= 1
        case 'R':
            head[1] += 1
        case 'L':
            head[1] -= 1


def yank(head, tail):
    if head == tail or distance(head, tail) == 1:
        return
    dx, dy = compare(head, tail)
    if dx:
        tail[0] += 1 if head[0] > tail[0] else -1
    if dy:
        tail[1] += 1 if head[1] > tail[1] else -1


def play(rope, input) -> int:
    visited = set()

    for direction, steps in input:
        for i in range(steps):
            move(rope[0], direction)
            for head, tail in pairwise(rope):
                yank(head, tail)
            visited.add(tuple(rope[-1]))

    return len(visited)


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
input = list(parse(infile))


# Part 1
rope1 = [[0,0] for _ in range(2)]
print(play(rope1, input))


# Part 2
rope2 = [[0,0] for _ in range(10)]
print(play(rope2, input))
