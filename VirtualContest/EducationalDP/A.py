# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n = int(input())
a = list(map(int, input().split()))


dp = {}


def solve(n):
    if n in dp:
        return dp[n]
    if n == 1:
        dp[1] = 0
    elif n == 2:
        dp[2] = abs(a[0] - a[1])
    else:
        dp[n] = min(
            solve(n - 1) + abs(a[n - 2] - a[n - 1]),
            solve(n - 2) + abs(a[n - 3] - a[n - 1]),
        )
    return dp[n]


print(solve(n))
