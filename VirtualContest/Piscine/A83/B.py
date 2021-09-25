# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n, l, t, x = map(int, input().split())
d = deque()
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    d.append((a, b))
    if b >= l and a > t:
        ans = "forever"
        d = deque()
        break

high_time = 0
while (len(d)) > 0:
    tar_a, tar_b = d.popleft()
    if tar_b < l:
        ans += tar_a
        high_time = 0
    else:
        if high_time + tar_a < t:
            high_time += tar_a
            ans += tar_a
        else:
            ans += t - high_time
            ans += x
            if high_time + tar_a != t:
                d.appendleft((tar_a, tar_b))
            high_time = 0

print(ans)