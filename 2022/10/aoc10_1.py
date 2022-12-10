#!/usr/bin/env python3

import sys
from typing import Iterator


def parse(infile):
    return [line.strip().split() for line in infile]


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
input = parse(infile)

SAMPLE_CYCLES = list(range(20, 220+1, 40))

X = 1


def strength(cycle):
    return cycle * X


def addx(val) -> callable:
    def _addx():
        global X
        X += val
    return _addx


def score(cycle):
    return X * cycle


def analyze(input) -> Iterator[int]:
    input = iter(input)
    cycle = 0
    stack = []

    while True:
        cycle += 1

        if cycle in SAMPLE_CYCLES:
            yield score(cycle)

        if stack:
            stack.pop()()
        else:
            try:
                cmd = next(input)
            except StopIteration:
                return
            match cmd:
                case ['noop']:
                    pass
                case ['addx', val]:
                    stack.append(addx(int(val)))
                case _:
                    raise Exception(cmd)


print(sum(analyze(input)))
