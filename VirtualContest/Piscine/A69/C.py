# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

INF = 10 ** 10
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [INF for i in range(n + 1)]
dp[1] = 0

for j in range(2, n + 1):
    for i in range(1, min(j, k + 1)):
        dp[j] = min(dp[j], dp[j - i] + abs(h[j - 1] - h[j - 1 - i]))


print(dp[n])