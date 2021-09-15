# -*- coding: utf-8 -*-
import math
import heapq
import sys
import copy
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

INF = 10 ** 10

s = input()
t = input()
dp = [[INF for i in range(len(t) + 1)] for j in range(len(s) + 1)]


def select_max(s, t):
    if len(s) >= len(t):
        return s
    else:
        return t


def solve(i, j):
    if i == 0 or j == 0:
        dp[i][j] = []
        return []
    if dp[i][j] == INF:
        if s[i - 1] == t[j - 1]:
            dp[i][j] = copy.deepcopy(solve(i - 1, j - 1))
            dp[i][j].append(s[i - 1])
        else:
            dp[i][j] = select_max(solve(i - 1, j), solve(i, j - 1))
    return dp[i][j]


print("".join((solve(len(s), len(t)))))
