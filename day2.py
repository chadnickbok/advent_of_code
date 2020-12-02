#!/usr/bin/env python3

import sys
import re

pattern = re.compile('(\d+)-(\d+) (\w): (\w+)')
valid_count = 0

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines:
    m = pattern.search(line)
    if m is None:
        print("heck", line)
        break

    n_min = int(m.group(1))
    n_max = int(m.group(2))
    char = m.group(3)

    n = 0
    for a in m.group(4):
        if a is char:
            n += 1
    
    if n >= n_min and n <= n_max:
        valid_count += 1


print(valid_count)

