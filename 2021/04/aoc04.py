#!/usr/bin/env python3
"""
Advent Of Code 2021: Day 3
https://adventofcode.com/2021/day/4

Reads an input file of bingo numbers and boards, finds a winner.
"""

import sys


def main1(numbers, boards):
    print(f'Loaded {len(boards)} boards and {len(numbers)} numbers')
    
    for number in numbers:
        print(f'Draw: {number}')
        for board in boards:
            is_winner = board.play(number)
            if is_winner:
                print('BINGO!')
                print(board)
                print(f'Score: {board.score(number)}')
                return
    
    print(f'Nobody won!')


def main2(numbers, boards):
    print(f'Loaded {len(boards)} boards and {len(numbers)} numbers')
    
    last_winner = None
    for number in numbers:
        print(f'Draw: {number}')
        for board in boards.copy():
            is_winner = board.play(number)
            if is_winner:
                print('BINGO!')
                last_winner = board
                boards.remove(board)
        if not boards:
            break  # `number` is preserved, because Python.
    
    print('LAST WINNER!')
    print(last_winner)
    print(f'Score: {last_winner.score(number)}')


class Board():
    """A BINGO board"""

    def __init__(self, rows):
        assert len(rows) == 5
        for row in rows:
            assert len(row) == 5
        
        self.rows = rows
        self.marked = [[False for _ in range(5)] for _ in range(5)]
    
    def __str__(self):
        toks = []
        for i in range(5):
            toks.append(' '.join('%2d' % val for val in self.rows[i]) + '    ' + ' '.join('#' if marked else '\u00B7' for marked in self.marked[i]))
        return '\n'.join(toks)

    def play(self, number) -> bool:
        """Play a drawn number, check whether we've got BINGO"""
        for i in range(5):
            for j in range(5):
                if self.rows[i][j] == number:
                    self.marked[i][j] = True
        return self.check()
    
    def check(self) -> bool:
        """Check whether we've got BINGO"""
        # rows
        for row in self.marked:
            if all(row):
                return True
        
        # columns
        for i in range(5):
            if all([row[i] for row in self.marked]):
                return True
        
        # diagonals
        # if all(self.marked[i][i] for i in range(5)):
        #     return True
        # if all(self.marked[i][4-i] for i in range(5)):
        #     return True
        
        return False
    
    def score(self, number) -> int:
        """Calculate this board's score given the number drawn"""
        unmarked = []
        for i in range(5):
            for j in range(5):
                if not self.marked[i][j]:
                    unmarked.append(self.rows[i][j])
        return sum(unmarked) * number


def parse(lines):
    """Parse input file and return (numbers, boards)"""
    numbers = [int(tok) for tok in lines.pop(0).split(',')]
    assert lines.pop(0) == ''  # blank

    boards = []
    rows = []

    for line in lines:
        line = line.strip()
        if line:
            rows.append([int(tok) for tok in line.split()])
        else:
            assert len(rows) == 0
        if len(rows) == 5:
            boards.append(Board(rows))
            rows = []
    
    return numbers, boards


if __name__ == '__main__':
    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    numbers, boards = parse([line.strip() for line in infile])
    main1(numbers, boards)

    print('-----------------------')

    infile = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r')
    numbers, boards = parse([line.strip() for line in infile])
    main2(numbers, boards)
