# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys
from typing import Any

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10


n = int(input())

dp = [INF for _ in range(n + 1)]


def solve(n):
    if dp[n] == INF:
        if n < 100:
            dp[n] = False
        elif n < 106:
            dp[n] = True
        else:
            dp[n] = any(
                [
                    solve(n - 100),
                    solve(n - 101),
                    solve(n - 102),
                    solve(n - 103),
                    solve(n - 104),
                    solve(n - 105),
                ]
            )
    return dp[n]


if solve(n):
    print(1)
else:
    print(0)
