# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
n, l = map(int, input().split())

memo = {}


def solve(n):
    if n in memo.keys():
        return memo[n]
    if n == 0:
        memo[n] = 1
    else:
        ans = 0
        ans += solve(n - 1)
        if n >= l:
            ans += solve(n - l)
        memo[n] = ans % MOD
    return memo[n]


print(solve(n))
