#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def qs_count(qs, n):
    count = 0
    for key in qs.keys():
        if qs[key] == n:
            count += 1
    return count

cur_qs = {}
count = 0
people = 0
for line in lines:
    if len(line.strip()) == 0:
        print(cur_qs.keys())
        count += qs_count(cur_qs, people)
        cur_qs = {}
        people = 0
        continue
    people += 1

    cur_line = line.strip()
    for i in range(0, len(cur_line)):
        a = cur_line[i]
        if a in cur_qs:
            cur_qs[a] += 1
        else:
            cur_qs[a] = 1

count += qs_count(cur_qs, people)

print(count)
