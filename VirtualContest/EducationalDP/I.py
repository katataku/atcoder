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

p = list(map(float, input().split()))
p.insert(0, 0)
dp = [[-1 for j in range(n + 1)] for i in range(n + 1)]

dp[0][0] = 1


def solve(i, j):
    if dp[i][j] == -1:
        dp[i][j] = 0
        if i > 0 and i >= j:
            dp[i][j] = solve(i - 1, j) * (1 - p[i])
            if j > 0:
                dp[i][j] += solve(i - 1, j - 1) * p[i]

    return dp[i][j]


ans = 0
for i in range(n // 2 + 1, n + 1):
    ans += solve(n, i)

print(ans)
