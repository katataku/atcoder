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
a = list(map(int, input().split()))

dp = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = a[i]


def solve(l, r):
    if dp[l][r] == INF:
        if l + 1 == r:
            dp[l][r] = a[l] + a[r]
        else:
            ret = INF
            for i in range(1, r - l - 1):
                ret = min(
                    ret, (solve(l, l + i) + solve(l + i + 1, r) + sum(a[l : r + 1]))
                )
            dp[l][r] = ret
    return dp[l][r]


print(solve(0, n - 1))
