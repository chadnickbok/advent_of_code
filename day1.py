#!/usr/bin/env python3

import sys

expenses = []
with open(sys.argv[1]) as f:
    for line in f:
        expenses.append(int(line))

for i in range(0, len(expenses)):
    for j in range(0, len(expenses)):
        for k in range(0, len(expenses)):
            if i == j or i == k or k == j:
                continue

            if (expenses[i] + expenses[j] + expenses[k]) == 2020:
                print(expenses[i], expenses[j], expenses[k], expenses[i] * expenses[j] * expenses[k])
