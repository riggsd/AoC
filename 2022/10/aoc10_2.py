#!/usr/bin/env python3

import sys
from typing import Iterator


def parse(infile):
    return [line.strip().split() for line in infile]


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
input = parse(infile)

X = 1


def addx(val) -> callable:
    def _addx():
        global X
        X += val
    return _addx


def analyze(input) -> Iterator[str]:
    input = iter(input)
    cycle = -1
    stack = []

    while True:
        cycle += 1

        yield '#' if cycle % 40 in {X-1, X, X+1} else ' '

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


crt = iter(analyze(input))
for r in range(6):
    for c in range(40):
        print(next(crt), end='')
    print()

