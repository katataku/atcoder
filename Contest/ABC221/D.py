# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n = int(input())
h = []
heapq.heapify(h)
for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(h, (a, 1))
    heapq.heappush(h, (a + b, -1))

d = [0 for _ in range(n + 1)]

cur_day = 0
cur_num = 0
tar_day, diff = heapq.heappop(h)

while len(h) >= 0:
    if cur_day != tar_day:
        d[cur_num] += tar_day - cur_day
        cur_day = tar_day
    cur_num += diff
    if len(h) > 0:
        tar_day, diff = heapq.heappop(h)
    else:
        break

print(" ".join(map(str, d[1:])))
