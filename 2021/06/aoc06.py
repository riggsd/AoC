#!/usr/bin/env python

import sys

infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')

school = map(int, infile.readline().split(','))

for day in range(1, 80+1):
    school2 = []
    for fish in school:
        if fish == 0:
            school2.append(6)
            school2.append(8)
        else:
            school2.append(fish - 1)
    school = school2

print(f'{day:2d}\t{len(school)}')
