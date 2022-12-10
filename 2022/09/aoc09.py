#!/usr/bin/env python3

import sys
from itertools import pairwise
from typing import Iterator


X, Y = 0, 1


def parse(infile) -> Iterator[tuple[str, int]]:
    for line in infile:
        direction, steps = line.strip().split()
        yield direction, int(steps)


def compare(head, tail) -> tuple[int, int]:
    return abs(head[X] - tail[X]), abs(head[Y] - tail[Y])


def distance(head, tail) -> int:
    return max(compare(head, tail))


def move(head, direction):
    match direction:
        case 'U': head[X] += 1
        case 'D': head[X] -= 1
        case 'R': head[Y] += 1
        case 'L': head[Y] -= 1


def yank(head, tail):
    if head == tail or distance(head, tail) == 1:
        return
    dx, dy = compare(head, tail)
    if dx:
        tail[X] += 1 if head[X] > tail[X] else -1
    if dy:
        tail[Y] += 1 if head[Y] > tail[Y] else -1


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
