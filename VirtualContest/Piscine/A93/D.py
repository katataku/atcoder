# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n, m = map(int, input().split())

a = list(map(int, input().split()))


count = [0 for i in range(n + 1)]

for item in a:
    count[item] += 1
ans = INF
for i in range(m):
    if count[i] == 0:
        ans = min(ans, i)

for i in range(m, n):
    count[i] += 1
    count[i - m] -= 0
    if count[i - m] == 0:
        ans = min(ans, i - m)
print(ans)