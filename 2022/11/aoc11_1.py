#!/usr/bin/env python3

import sys
from dataclasses import dataclass
from typing import Iterator


@dataclass
class Monkey:
    i: int
    items: list[int] = None
    operation: callable = None
    test: int = None
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
                    monkey.test = int(toks[-1])
                case 'If':
                    k, v = bool(toks[1] == 'true:'), int(toks[-1])
                    monkey.throw_to[k] = v
                case _:
                    pass
        yield monkey


def print_monkies(monkies):
    for monkey in monkies:
        print(f'Monkey {monkey.i}:  {monkey.inspected:3d}  {monkey.items}')
    print()


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
monkies = list(parse(infile))

for round in range(20):
    print(f'---- round {round} ----')

    print_monkies(monkies)

    for monkey in monkies:
        print(f'Monkey {0}')
        monkey.inspected += len(monkey.items)
        for level in monkey.items:
            print(f'  Monkey inspects an item with a worry level of {level}')
            level = monkey.operation(level)
            print(f'    Worry level is multiplied to {level}')
            level //= 3
            print(f'    Monkey bored. Worry level {level}')
            print(f'    Current level {"is" if level % monkey.test == 0 else "is not"} divisble by {monkey.operation}')
            throw_to = monkey.throw_to[level % monkey.test == 0]
            print(f'    Item with level {level} is thrown to monkey {throw_to}')
            assert throw_to != monkey.i
            monkies[throw_to].items.append(level)
        monkey.items = []

    print_monkies(monkies)


top2 = sorted(monkies, key=lambda m: m.inspected, reverse=True)[:2]
monkey_business = top2[0].inspected * top2[1].inspected
print(monkey_business)
# 50609 is too low
