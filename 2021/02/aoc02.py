#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 2

Reads an input file of submarine commands, outputs position (sort of).
"""

import sys


def main1(commands):
    horiz, depth = 0, 0

    for direction, value in commands:
        if direction == 'forward':
            horiz += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value
        else:
            raise Exception(f'Unknown direction: {direction}')
        
    print(horiz * depth)


def main2(commands):
    horiz, depth = 0, 0
    aim = 0

    for direction, value in commands:
        if direction == 'forward':
            horiz += value
            depth += value * aim
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
        else:
            raise Exception(f'Unknown direction: {direction}')
        
    print(horiz * depth)


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')

    commands = [(direction, int(value)) for (direction, value) in [line.split() for line in infile]]

    main1(commands)
    main2(commands)
