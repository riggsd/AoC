#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 3

Reads an input file of binary strings and calculates some bitwise nonsense.
"""

import sys


def main1(binaries):
    n = len(binaries)
    width = len(binaries[0])

    sums = [0 for _ in range(width)]

    for binary in binaries:
        for i, bit in enumerate(binary):
            sums[i] += int(bit)

    threshold = n / 2.0
    gamma_bits   = [str(int(sum >= threshold)) for sum in sums]
    epsilon_bits = [str(int(sum < threshold)) for sum in sums]
    gamma_str   = ''.join(gamma_bits)
    epsilon_str = ''.join(epsilon_bits)
    gamma   = int(gamma_str, base=2)
    epsilon = int(epsilon_str, base=2)
    print(f'gamma:  \t{gamma_str} {gamma}')
    print(f'epsilon:\t{epsilon_str} {epsilon}')
    print(f'power consumption:\t{gamma * epsilon}')


def main2(binaries):

    oxygen_values = binaries.copy()
    for i in range(len(binaries[0])):
        most_common_bits = most_common(oxygen_values)
        oxygen_values = [value for value in oxygen_values if value[i] == most_common_bits[i]]
        if len(oxygen_values) == 1:
            break
    if len(oxygen_values) > 1:
        raise Exception(f'Too many oxygen values! {len(oxygen_values)}')
    oxygen_str = oxygen_values[0]
    oxygen = int(oxygen_str, base=2)
    print(f'O2 generator:\t{oxygen_str} {oxygen}')

    co2_values = binaries.copy()
    for i in range(len(binaries[0])):
        least_common_bits = least_common(co2_values)
        co2_values = [value for value in co2_values if value[i] == least_common_bits[i]]
        if len(co2_values) == 1:
            break
    if len(co2_values) > 1:
        raise Exception(f'Too many CO2 values! {len(co2_values)}')
    co2_str = co2_values[0]
    co2 = int(co2_str, base=2)
    print(f'CO2 scrubber:\t{co2_str} {co2}')

    print(f'life support:\t{oxygen * co2}')

def most_common(binaries):
    n = len(binaries)
    width = len(binaries[0])

    sums = [0 for _ in range(width)]

    for binary in binaries:
        for i, bit in enumerate(binary):
            sums[i] += int(bit)

    threshold = n / 2
    return [str(int(sum >= threshold)) for sum in sums]

def least_common(binaries):
    n = len(binaries)
    width = len(binaries[0])

    sums = [[0,0] for _ in range(width)]  # 2D

    for binary in binaries:
        for i, bit in enumerate(binary):
            sums[i][int(bit)] += 1
    
    return [str(bit) for bit in [0 if sum[0] <= sum[1] else 1 for sum in sums]]


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')

    binaries = [line.strip() for line in infile]

    main1(binaries)
    main2(binaries)
