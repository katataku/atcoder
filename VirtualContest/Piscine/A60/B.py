# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, s = map(int, input().split())

d = []
for i in range(n):
    a, b = map(int, input().split())
    d.append((a, b))

rest_min = [0 for i in range(n)]
for i in range(n):
    if i == 0:
        rest_min[n - 1] = min(d[n - 1])
    else:
        i = n - 1 - i
        rest_min[i] = min(d[i]) + rest_min[i + 1]

dp = [{} for j in range(n + 1)]

for i in range(n + 1):
    if i == 0:
        dp[i][0] = True
        continue
    for item in dp[i - 1]:
        a, b = d[i - 1]
        if item + a <= s:
            dp[i][item + a] = True
        if item + b <= s:
            dp[i][item + b] = True


ans = "Impossible"
if s in dp[n]:
    rest = s
    cnt = n - 1
    ans = ""
    while cnt >= 0:
        a, b = d[cnt]
        if rest - a >= 0 and rest - a in dp[cnt]:
            ans = "A" + ans
            cnt -= 1
            rest -= a
            continue
        if rest - b >= 0 and rest - b in dp[cnt]:
            ans = "B" + ans
            cnt -= 1
            rest -= b


print(ans)
