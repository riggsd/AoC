#!/usr/bin/env python3

import sys
from enum import Enum
from typing import Iterator, TextIO, Tuple

LOSE, DRAW, WIN = 0, 3, 6

SHOULD_ROCK, SHOULD_PAPER, SHOULD_SCISSORS = "X", "Y", "Z"
SHOULD_LOSE, SHOULD_DRAW, SHOULD_WIN = "X", "Y", "Z" 


class Hand(Enum):
    ROCK     = 1
    PAPER    = 2
    SCISSORS = 3

    @classmethod
    def of(cls, c) -> "Hand":
        return {
            "A": cls.ROCK,
            "B": cls.PAPER,
            "C": cls.SCISSORS,
        }[c]

    def beats(self) -> "Hand":
        return {
            self.ROCK:     self.SCISSORS,
            self.PAPER:    self.ROCK,
            self.SCISSORS: self.PAPER,
        }[self]

    def loses_to(self) -> "Hand":
        return {
            self.ROCK:     self.PAPER,
            self.PAPER:    self.SCISSORS,
            self.SCISSORS: self.ROCK,
        }[self]


def parse(infile: TextIO) -> Iterator[Tuple[str, str]]:
    for line in infile:
        toks = line.strip().split()
        yield toks[0], toks[1]


def score(them: Hand, me: Hand) -> int:
    if me.beats() == them:
        return WIN + me.value
    if me.loses_to() == them:
        return LOSE + me.value
    if me == them:
        return DRAW + me.value


def play1(guide) -> Iterator[Tuple[Hand, Hand]]:
    for them, me in guide:
        them = Hand.of(them)
        if me == SHOULD_ROCK:
            me = Hand.ROCK
        elif me == SHOULD_PAPER:
            me = Hand.PAPER
        elif me == SHOULD_SCISSORS:
            me = Hand.SCISSORS
        yield them, me


def play2(guide) -> Iterator[Tuple[Hand, Hand]]:
    for them, me in guide:
        them = Hand.of(them)
        if me == SHOULD_WIN:
            me = them.loses_to()
        elif me == SHOULD_LOSE:
            me = them.beats()
        elif me == SHOULD_DRAW:
            me = them
        yield them, me


input = list(parse(sys.stdin))

total1 = sum(score(*hand) for hand in play1(input))
print(total1)

total2 = sum(score(*hand) for hand in play2(input))
print(total2)
