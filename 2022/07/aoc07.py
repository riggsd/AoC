#!/usr/bin/env python3

import sys
from typing import Iterator


class Node():
    def __init__(self, name, parent: 'Node', size: int=None, children: dict[str, 'Node']=None):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = children if children else {}

    def __str__(self):
        return self.name

    @property
    def is_dir(self) -> bool:
        return self.size is None

    def total_size(self) -> int:
        if self.size:
            return self.size
        return sum(node.total_size() for node in self.children.values())

    def walk(self) -> Iterator['Node']:
        yield self
        if self.children:
            for child in self.children.values():
                yield from child.walk()

    def child(self, name, size: int=None, children: dict[str, 'Node']=None) -> 'Node':
        node = Node(name, self, size=size, children=children)
        self.children[name] = node
        return node

def parse(infile) -> Iterator[list[str]]:
    for line in infile:
        yield line.split()


infile = sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])
input = parse(infile)

fs = Node('/', None)
pwd = fs

def mkdir(dirname):
    global pwd
    if dirname in pwd.children:
        pwd = pwd.children[dirname]
    else:
        pwd.child(dirname)

def mkfile(fname, size):
    pwd.child(fname, size=size)

def cd(dirname):
    global pwd
    if dirname == '/':
        pwd = fs
    elif dirname == '..':
        pwd = pwd.parent
    else:
        mkdir(dirname)

def print_tree(node, indent=''):
    if node.size is not None:
        print(f'{indent}- {node.name} (file, size={node.size})')
        return
    print(f'{indent}- {node.name} (dir total_size={node.total_size()})')
    for child in node.children.values():
        print_tree(child, indent + '  ')

def run(input):
    global pwd
    for line in input:
        if line[0] == '$':
            if line[1] == 'cd':
                cd(line[2] if len(line) > 2 else None)
        else:
            if line[0] == 'dir':
                mkdir(line[1])
            else:
                mkfile(line[1], int(line[0]))


run(input)
print_tree(fs)
print()


# Part 1
total = sum(node.total_size() for node in fs.walk() if node.is_dir and node.total_size() <= 100_000)
print(total)


# Part 2
DISK      = 70_000_000
REQ_SPACE = 30_000_000
used = fs.total_size()
free = DISK - used
need_to_free = REQ_SPACE - free
largest_dirs = [node for node in fs.walk() if node.total_size() >= need_to_free]
delete_me = sorted(largest_dirs, key=lambda x: x.total_size())[0]
print(delete_me.total_size())
