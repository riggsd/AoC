#!/usr/bin/env python3

# https://adventofcode.com/2025/day/6

import sys
import functools
from operator import add, mul


OPS = {'+': add, '*': mul}


def input():
    """Return input as 2D list"""
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    return [line.split() for line in infile]


def rotate(data):
    """Rotate columns to rows"""
    h, w = len(data), len(data[0])
    return [[data[row][col] for row in range(h)] for col in range(w)]


def calculate(row) -> int:
    """Compute the value for a given row, with operator as last element"""
    op, vals = OPS[row[-1]], map(int, row[:-1])
    return functools.reduce(op, vals)


data  = rotate(input())
total = sum(calculate(row) for row in data)
print("Grand Total:", total)
