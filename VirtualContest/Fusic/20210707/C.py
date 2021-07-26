# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
n, m = map(int, input().split())

memo = [-1 for i in range(n + 2)]

ans = 0
for i in range(m):
    b = int(input())
    memo[b] = 0


def step(n):
    if memo[n] != -1:
        return memo[n]

    if n == 0 or n == 1:
        memo[n] = 1
        return 1
    else:
        ans = 0
        ans += step(n - 1)
        ans += step(n - 2)
        memo[n] = ans % MOD
        return ans % MOD


print(step(n))