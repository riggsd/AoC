#!/usr/bin/env python3

import sys


def transpose(matrix):
    return [[row[col] for row in matrix] for col, _ in enumerate(reversed(matrix[0]))]


def parse(infile: str) -> tuple:
    """Produce a dict of crate stacks, and a list of move instructions"""
    halves = infile.split('\n\n')
    assert len(halves) == 2
    stacks = halves[0]
    print(stacks)
    print()
    lines = stacks.splitlines()
    transposed = transpose(lines)
    stacks = {}
    for line in transposed:
        line = line[::-1]
        if not line[0].isdigit():
            continue
        num, crates = line[0], line[1:]
        while crates[-1] == ' ':
            crates.pop(-1)
        stacks[int(num)] = crates
    print_stacks(stacks)

    instructions = halves[1]
    parsed = []
    for line in instructions.splitlines():
        assert 'move' in line
        toks = line.split()
        assert len(toks) == 6
        parsed.append((int(toks[1]), int(toks[3]), int(toks[5])))

    return stacks, parsed


def print_stacks(stacks):
    for i, crates in stacks.items():
        print(f'{i}: {"".join(crates)}')
    print()


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
input = infile.read()


# part 1
stacks, instructions = parse(input)
for n, source, destination in instructions:
    for i in range(n):
        stacks[destination].append( stacks[source].pop(-1) )

print_stacks(stacks)
tops = ''.join(stack[-1] for stack in stacks.values())
print(tops)
print()


# part 2
stacks, instructions = parse(input)
for n, source, destination in instructions:
    crates = stacks[source][-n:]
    for i in range(n):
        stacks[source].pop(-1)
    stacks[destination].extend(crates)

print_stacks(stacks)
tops = ''.join(stack[-1] for stack in stacks.values())
print(tops)
