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
    while clicks >= 100:
        clicks -= 100
        count += 1  # multiple full rotations
    
    delta = (dial + direction * clicks)
    if dial != 0 and (delta > 100 or delta < 0):
        count += 1  # overflow past zero on our last rotation

    dial = delta % 100
    
    if dial == 0:
        count += 1  # we landed on zero itself

print('Password:', count)
