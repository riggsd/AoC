#!/usr/bin/env python3

# https://adventofcode.com/2025/day/2

import sys

try:
    from itertools import batched
except ImportError:
    # batteries included in Python 3.12, but I'm on Python 3.11!
    # https://docs.python.org/3/library/itertools.html#itertools.batched
    from itertools import islice
    def batched(iterable, n, *, strict=False):
        # batched('ABCDEFG', 2) → AB CD EF G
        if n < 1:
            raise ValueError('n must be at least one')
        iterator = iter(iterable)
        while batch := tuple(islice(iterator, n)):
            if strict and len(batch) != n:
                raise ValueError('batched(): incomplete batch')
            yield batch


def input():
    infile = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    for tok in infile.read().split(','):
        start, end = tok.split('-')
        yield int(start), int(end)


def valid2(id: int) -> bool:
    idstr = str(id)
    for i in range(1, len(idstr)):  # for every length substring...
        try:
            batches = list(batched(idstr, i, strict=True))
        except ValueError:
            continue  # this length string not divisible by i
        first, rest = batches[0], batches[1:]
        for tok in rest:
            if first != tok:
                break  # this is NOT a sequence of repeating patterns of len i
        else:
            #print('\tinvalid:', i, id)
            return False  # this IS a sequence of repeating patterns of len i, so invalid!
    return True


sum = 0

for start, end in input():
    #print(start, '-', end)
    for id in range(start, end+1):
        if not valid2(id):
            sum += id

print('Invalid Sum:', sum)
