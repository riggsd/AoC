#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 13
https://adventofcode.com/2021/day/13

Reads an input file of dot coordinates and paper-folding instructions, and performs origami
"""

import sys


def main1(paper, instructions):
    """Part 1: count the dots after our first fold"""
    axis, ordinate = instructions[0]
    fold(paper, axis, ordinate)
    print(f'Total Dots: {dot_count(paper)}')


def main2(paper, instructions):
    """Part 2: Apply all folds to decode the secret visual message"""
    print_paper(paper)
    for axis, ordinate in instructions:
        fold(paper, axis, ordinate)
        print_paper(paper)


def fold(paper: list, axis: str, ordinate: int):
    """Fold paper along specified 'y' or 'x' axis"""
    print(f'fold {axis}={ordinate}')
    if axis == 'x':
        for x2 in range(len(paper[0])-1, ordinate, -1):
            x1 = ordinate - (x2 - ordinate)
            col2 = popx(paper, x2)
            overlayx(paper, x1, col2)
        cutline = popx(paper, ordinate)
        assert not any(cutline)
    elif axis == 'y':
        for y2 in range(len(paper)-1, ordinate, -1):
            y1 = ordinate - (y2 - ordinate)
            row1 = paper[y1]
            row2 = paper.pop(y2)
            paper[y1] = list(map(any, zip(row1, row2)))
        cutline = paper.pop(ordinate)
        assert not any(cutline)
    else:
        raise Exception(axis)

def popx(paper, x):
    """Pop column from paper at `x`"""
    return list([row.pop(x) for row in paper])

def overlayx(paper, x, col):
    """Overlay column of values `col` on top of column `x` of `paper`"""
    for y, val2 in enumerate(col):
        val1 = paper[y][x]
        paper[y][x] = any({val1, val2})

def dot_count(paper):
    return sum([len(list(filter(lambda v: v, row))) for row in paper])

def print_paper(paper):
    w, h = len(paper[0]), len(paper)
    print('  ' + ''.join(str(i % 10) for i in range(0, w)))
    print('  ' + '-' * w)
    for y, row in enumerate(paper):
        print(f'{y % 10}|' + ''.join(['\u2588' if v else '\u00B7' for v in row]))

def parse(infile):
    """
    Parse input file and produce two values: 
    - prepopulated "paper" as list of lists of bool
    - list of (axis,ordinate) fold instructions
    """
    coords, instructions = [], []
    w, h = 0, 0

    for line in infile:
        if ',' in line:
            x, y = map(int, line.strip().split(','))
            coords.append( (x,y) )
            if x >= w: w = x + 1
            if y >= h: h = y + 1
        elif not line.strip():
            continue
        else:
            axis, ordinate = line.strip().split(' ')[2].split('=')
            instructions.append( (axis, int(ordinate)) )
    
    paper = []
    for y in range(h):
        paper.append(list([False for x in range(w)]))

    for x,y in coords:
        paper[y][x] = True

    return paper, instructions


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    lines = list(infile.readlines())

    paper, instructions = parse(lines)
    main1(paper, instructions)

    paper, instructions = parse(lines)
    main2(paper, instructions)
