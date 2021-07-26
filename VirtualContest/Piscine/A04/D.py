# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(100000000)
MOD = 10 ** 9 + 7


d = deque()

for i in range(1, 10):
    d.append(i)

k = int(input())


for i in range(k - 1):
    x = d.popleft()
    if x % 10 != 0:
        d.append(10 * x + (x % 10) - 1)
    d.append(10 * x + (x % 10))
    if x % 10 != 9:
        d.append(10 * x + (x % 10) + 1)


print(d.popleft())