#!/usr/bin/env python3

# https://adventofcode.com/2025/day/1

import sys


def input():
    for line in sys.stdin:
        direction = 1 if line[0] == 'R' else -1
        clicks = int(line[1:])
        yield direction, clicks


dial = 50  # starting position
count = 0  # times the dial has landed on zero

for direction, clicks in input():
    dial = (dial + direction * clicks) % 100
    if dial == 0:
        count += 1

print('Password:', count)
