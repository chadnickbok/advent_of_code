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

    i_first = int(m.group(1)) - 1
    i_second = int(m.group(2)) - 1
    char = m.group(3)
    password = m.group(4)

    char_first = password[i_first]
    char_second = password[i_second]

    first_right = char_first is char
    second_right = char_second is char

    if first_right != second_right:
        valid_count += 1

print(valid_count)

