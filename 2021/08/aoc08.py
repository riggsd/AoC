#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 8
https://adventofcode.com/2021/day/8

Reads an input file of 10 unique scrambled 7-segment display values and scrambled 4 digit output values,
and reverse-engineers the scrambled wires.

This solution takes advantage of two statistical facts about 7-seg displays:
  - digits 1, 4, 7, 8 have unique segment lengths
  - segments b, e, f occur in a unique number of digits

Given all 10 unique digits, we can solve for all 7 segments using set theory.
"""

import sys
from collections import defaultdict


#                  0  1  2  3  4  5  6  7  8  9
segment_lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#                  6  *  5  5  *  5  6  *  *  6

unique_segments_by_length = {2: 1, 4: 4, 3: 7, 7: 8}

segments = [
    'a''b''c'   'e''f''g', # 0  6
          'c'      'f',    # 1  *
    'a'   'c''d''e'   'g', # 2  5
    'a'   'c''d'   'f''g', # 3  5
       'b''c''d'   'f',    # 4  *
    'a''b'   'd'   'f''g', # 5  5
    'a''b'   'd''e''f''g', # 6  6
    'a'   'c'      'f',    # 7  *
    'a''b''c''d''e''f''g', # 8  *
    'a''b''c''d'   'f''g', # 9  6
] #  8  6  8  7  4  9  7
#       *        *  *

segmentsU = [
          'c'      'f'   , # 1
       'b''c''d'   'f'   , # 4
    'a'   'c'      'f'   , # 7
    'a''b''c''d''e''f''g', # 8
]

segments_to_digits = {seg:i for i,seg in enumerate(segments)}

def is_unique(signal: str) -> bool:
    return len(signal) in {2, 4, 3, 7}


def main1(data):
    total = 0
    for signals, output in data:
        for value in output:
            if is_unique(value):
                total += 1
    print(total)


def main2(data):
    total = 0
    for signals, output in data:
        mapping = find_replacements(signals)
        value = output_to_value(mapping, output)
        total += value
    print(total)

def output_to_value(mapping, output):
    """Given four scrambled output signals, solve for its value"""
    digits = []
    for digitstr in output:
        segment = ''.join(sorted([mapping[c] for c in list(digitstr)]))
        digit = segments_to_digits[segment]
        #print(f'{digitstr} -> {segment} -> {digit}')
        digits.append(str(digit))
    assert len(digits) == 4
    return int(''.join(digits))


def find_uniques(signals):
    """Mapping of digit -> signal"""
    return {unique_segments_by_length[len(sig)]:set(sig) for sig in filter(is_unique, signals)}

def seg_freqs(signals):
    """Mapping of segment -> frequency"""
    # Given all 10 unique signals, we should see the 'e' segment 4 times, 'b' 6 times, 'f' 9 times
    freqs = defaultdict(int)
    for signal in signals:
        for segment in signal:
            freqs[segment] += 1
    counts = list(freqs.values())
    assert counts.count(4) == 1
    assert counts.count(6) == 1
    assert counts.count(9) == 1
    return freqs

def find_replacements(signals):
    """Given unique segment signals, find a mapping of replacement characters"""
    #print(signals)

    freqs = {v:k for k,v in seg_freqs(signals).items() if v in {4, 6, 9}}
    # for k,v in sorted(freqs.items()):
    #     print(f'{k} {v}')

    uniques = find_uniques(signals)  # digit -> signal
    # for k,v in sorted(uniques.items()):
    #     print(f'{k} {v}')
    
    a = (uniques[7] & uniques[8]) - (uniques[1] | uniques[4])
    assert len(a) == 1, f'a: {a}'
    a = a.pop()
    b = freqs[6]
    c = (uniques[1] & uniques[4] & uniques[7] & uniques[8]) - {freqs[9]}
    assert len(c) == 1, f'c: {c}'
    c = c.pop()
    d = (uniques[4] & uniques[8]) - (uniques[1] | uniques[7] | {b})
    assert len(d) == 1, f'd: {d}'
    d = d.pop()
    e = freqs[4]
    f = freqs[9]
    g = uniques[8] - (uniques[1] | uniques[4] | uniques[7] | {e})
    assert len(g) == 1, f'g: {g}'
    g = g.pop()

    # print(f'a: {a}  b: {b}  c: {c}  d: {d}  e: {e}  f: {f}  g: {g}')
    mapping = {a:'a', b:'b', c:'c', d:'d', e:'e', f:'f', g:'g'}
    assert len(set(mapping.values())) == 7
    return mapping


def parse(infile):
    """
    Produces tuples of (signals, output) where
    signals is a 10-tuple of unique segment signals and
    output is a 4-tuple of output data
    """
    for line in infile:
        toks = line.split(' | ')
        assert len(toks) == 2
        signals = toks[0].split()
        output = toks[1].split()
        assert len(signals) == 10
        assert len(output) == 4
        yield signals, output


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    data = list(parse(infile))
    
    main1(data)
    main2(data)
