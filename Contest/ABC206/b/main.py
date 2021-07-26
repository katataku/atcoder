# -*- coding: utf-8 -*-
import math

# Input#
# n = int(input())
n = int(input())

i = 1
cnt = 0

while True:
    cnt += i
    if cnt >= n:
        break
    i += 1

print(i)