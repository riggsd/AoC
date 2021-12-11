#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 10
https://adventofcode.com/2021/day/10

Reads an input file of corrupted/incomplete syntax tokens.
"""

import sys
from statistics import median


openers = {'(', '[', '{', '<'}
closers = {')', ']', '}', '>'}
closing = {'(': ')', '[': ']', '{': '}', '<': '>'}

corrupt_scores    = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_scores = {')': 1, ']': 2,  '}': 3,    '>': 4}


def main1(lines):
    print(sum(score1(parse1(line)) for line in lines))

def score1(c):
    return corrupt_scores[c] if c else 0

def parse1(line):
    """Part 1 parser simply returns the first corrupt char of corrupted lines, or None"""
    stack = []

    for c in line:
        if c in openers:
            stack.append(c)
        elif c in closers:
            if c != closing[stack[-1]]:
                print(f'corrupted! expected {closing[stack[-1]]} but found {c}')
                return c
            stack.pop()  # complete, empty chunk
        else:
            raise Exception(c)
    return None # incomplete or good


def main2(lines):
    completions = filter(lambda c: c is not None, map(parse2, lines))
    scores = map(score2, completions)
    print(median(scores))

def score2(cs):
    total = 0
    for c in cs:
        total *= 5
        total += incomplete_scores[c]
    return total

def parse2(line):
    """Part 2 parser simply returns the completion of incomplete lines, or None"""    
    stack = []

    for c in line:
        if c in openers:
            stack.append(c)
        elif c in closers:
            if c != closing[stack[-1]]:
                return None  # corrupt
            stack.pop()  # complete, empty chunk
        else:
            raise Exception(f'corrupted! wtf is {c} ???')
    
    cs = []
    while stack:
        cs.append(closing[stack.pop()])
    print(f'incomplete! complete by adding {cs}  score: {score2(cs)}')
    return ''.join(cs)


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    lines = list([line.strip() for line in infile.readlines()])

    main1(lines)
    main2(lines)
