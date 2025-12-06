#!/usr/bin/env python3

# https://adventofcode.com/2025/day/6

import sys
import functools
from operator import add, mul


ops = { '+': add,'*': mul}


def input():
    """Return input as text"""
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    return infile.read()


def parse(data):
    """Parse columns into rows of values with operator, like Part 1 data"""
    lines = data.splitlines()
    ops = lines.pop(-1).split()  # strip the operators off, they're aligned with columns

    # restack columns as rows
    rotated = [''.join(row).strip() for row in zip(*lines)]

    # regroup to a vector of values with an operator, like in Part 1
    row = []
    for line in rotated:
        if line:
            row.append(int(line))
        else:  # blank line separates groups
            row.append(ops.pop(0))
            yield row
            row = []
    row.append(ops.pop(0))  # last row
    yield row


def calculate(row) -> int:
    """Compute the value for a given row, with operator as last element"""
    op, vals = ops[row[-1]], row[:-1]
    return functools.reduce(op, vals)


data  = list(parse(input()))
total = sum(calculate(row) for row in data)
print("Grand Total:", total)
