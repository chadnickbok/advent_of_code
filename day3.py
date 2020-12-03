#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


print(len(lines[0].strip()))
print(lines[0])

pos = 0
trees = 0
for line in lines:
    cur_line = line.strip()
    if pos >= len(cur_line):
        pos = pos % len(cur_line)

    if cur_line[pos] is "#":
        trees += 1

    pos += 3

print(trees)
