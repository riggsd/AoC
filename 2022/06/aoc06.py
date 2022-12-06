#!/usr/bin/env python3

import sys


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
input = infile.read().strip()


def find_marker(input: str, width: int) -> int:
    for i in range(width, len(input)):
        window = input[i-width:i]
        if len(set(window)) == len(window):
            return i


print(find_marker(input, 4))
print(find_marker(input, 14))
