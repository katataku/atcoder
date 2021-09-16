# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n = int(input())

dp = [{} for i in range(n)]

for i in range(n):
    a, b, c = map(int, input().split())
    dp[i][0] = a
    dp[i][1] = b
    dp[i][2] = c
    if i != 0:
        dp[i][0] += max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] += max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] += max(dp[i - 1][0], dp[i - 1][1])

print(max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
