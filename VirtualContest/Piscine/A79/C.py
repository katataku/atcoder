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

dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]


def solve(start, end):
    if dp[start][end] == INF:
        if start == end:
            dp[start][end] = a[start]
        else:
            dp[start][end] = max(
                a[start] - solve(start + 1, end), a[end] - solve(start, end - 1)
            )
        pass
    return dp[start][end]


for i in range(1, n):
    solve(i - 1, i)

print(solve(0, n - 1))
