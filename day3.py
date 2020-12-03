#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

print(len(lines[0].strip()))
print(lines[0])


slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

tree_counts = []

for slope in slopes:
    pos = 0
    trees = 0
    i = 0
    while i < len(lines):
        cur_line = lines[i].strip()
        if pos >= len(cur_line):
            pos = pos % len(cur_line)

        if cur_line[pos] is "#":
            trees += 1

        pos += slope[0]
        i += slope[1]
    print(trees)
    tree_counts.append(trees)

