#!/usr/bin/env python3

import sys
from itertools import pairwise
from typing import Iterator


def parse(infile) -> Iterator[tuple[str, int]]:
    for line in infile:
        direction, steps = line.strip().split()
        yield direction, int(steps)


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


def compare(head, tail) -> tuple[int, int]:
    return abs(head[0] - tail[0]), abs(head[1] - tail[1])


def distance(head, tail) -> int:
    return max(compare(head, tail))


def yank(head, tail):
    if head == tail or distance(head, tail) == 1:
        return
    dx, dy = compare(head, tail)
    if dx:
        tail[0] += 1 if head[0] > tail[0] else -1
    if dy:
        tail[1] += 1 if head[1] > tail[1] else -1


def print_grid(rope, height=5, width=6):
    print()
    for x in reversed(range(height)):
        for y in range(width):
            for knot, coords in enumerate(rope):
                if coords == [x,y]:
                    print(knot if knot else 'H', end='')
                    break
            else:
                print('.', end='')
        print()
    print()


def play(rope, input) -> int:
    """Play the input instructions on the given rope, return number of spaces visited by tail knot"""
    visited = set()
    print_grid(rope)
    print()

    for direction, steps in input:
        print('----------------')
        print(f'rope: {rope}')
        print(f'   -> {direction} {steps}')

        for i in range(steps):
            move(rope[0], direction)
            for head, tail in pairwise(rope):
                yank(head, tail)
            visited.add(tuple(rope[-1]))

        print_grid(rope)
        print()

    return len(visited)


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
input = list(parse(infile))


# Part 1
rope = [[0,0] for _ in range(2)]
print(play(rope, input))


# Part 2
rope = [[0,0] for _ in range(10)]
print(play(rope, input))
