#!/usr/bin/env python3

import sys

counts = []
total = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        counts.append(total)
        total = 0
        continue
    total += int(line)

top1 = max(counts)
print(top1)

top3 = sorted(counts)[-3:]
print(sum(top3))
