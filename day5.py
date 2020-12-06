#!/usr/bin/env python3

import sys
import math

with open(sys.argv[1]) as f:
    lines = f.readlines()

rows = 128
seats = 8

seat_ids = []
for line in lines:
    x = 1
    cur_row = 0
    for i in range(0, 7):
        if line[i] == "B":
            divisor = math.pow(2, x)
            print("divisor", divisor)
            cur_row += rows / divisor
        x += 1

    x = 1
    cur_seat = 0
    for i in range(7, 10):
        if line[i] == "R":
            divisor = math.pow(2, x)
            print("divisor", divisor)
            cur_seat += seats / divisor
        x += 1

    cur_id = cur_row * 8 + cur_seat
    seat_ids.append(cur_id)

seat_ids.sort()

for i in range(0, len(seat_ids)):
    cur_seat = seat_ids[i]
    next_seat = seat_ids[i+1]
    if cur_seat + 1 != next_seat:
        print(cur_seat + 1)
        break