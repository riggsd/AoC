#!/usr/bin/env python3
import math
import sys
from dataclasses import dataclass
from typing import Iterator


@dataclass
class Monkey:
    i: int
    items: list[int] = None
    operation: callable = None
    divisor: int = None
    throw_to: dict[bool, int] = None
    inspected: int = 0


def op(args) -> callable:
    match args:
        case ['*', 'old']:
            return lambda old: old * old
        case ['*', val]:
            return lambda old: old * int(val)
        case ['+', val]:
            return lambda old: old + int(val)
        case _:
            raise Exception(args)


def parse(infile) -> Iterator[Monkey]:
    for block in infile.read().split('\n\n'):
        monkey = None
        for line in block.splitlines():
            toks = line.strip().split()
            match toks[0]:
                case 'Monkey':
                    monkey = Monkey(int(toks[1][:-1]))
                    monkey.throw_to = {}
                case 'Starting':
                    monkey.items = list(map(int, line.split(':')[1].split(',')))
                case 'Operation:':
                    monkey.operation = op(line.split('old',1)[1].strip().split())
                case 'Test:':
                    monkey.divisor = int(toks[-1])
                case 'If':
                    k, v = bool(toks[1] == 'true:'), int(toks[-1])
                    monkey.throw_to[k] = v
                case _:
                    pass
        yield monkey


def print_monkies(monkies):
    for monkey in monkies:
        print(f'Monkey {monkey.i}:  {monkey.inspected:6d}  {monkey.items}')
    print()


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
monkies = list(parse(infile))

master_divisor = math.lcm(*(m.divisor for m in monkies))

for round in range(10000):

    print_monkies(monkies)

    for monkey in monkies:
        monkey.inspected += len(monkey.items)
        for level in monkey.items:
            level = monkey.operation(level)
            level %= master_divisor
            throw_to = monkey.throw_to[level % monkey.divisor == 0]
            assert throw_to != monkey.i
            monkies[throw_to].items.append(level)
        monkey.items = []

    print_monkies(monkies)


top2 = sorted(monkies, key=lambda m: m.inspected, reverse=True)[:2]
monkey_business = top2[0].inspected * top2[1].inspected
print(monkey_business)

