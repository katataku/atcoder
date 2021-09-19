# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [-1 for _ in range(k + 1)]


def solve(k):
    if dp[k] == -1:
        if k in a:
            dp[k] = True
        else:
            ret = False
            for item in a:
                if k - item > 0:
                    ret = ret or not solve(k - item)
            dp[k] = ret
    return dp[k]


if solve(k):
    print("First")
else:
    print("Second")