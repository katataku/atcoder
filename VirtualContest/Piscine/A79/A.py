# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

a, b, x, y = map(int, input().split())

visitid = [[dfs for i in range(101)] for j in range(2)]


def solve(tower, floor):
    if dp[tower][floor] == INF:
        if tower == 1 and floor == b:
            dp[tower][floor] = 0
        else:
            ret = INF
            dir = 1
            if b < floor:
                dir *= -1
            if tower == 0:
                ret = min(ret, y + solve(1, floor))
            if 0 < floor + dir < 101:
                ret = min(x + solve(tower, floor + dir), ret)
                if (dir > 0 and tower == 0) or (dir < 0 and tower == 1):
                    ret = min(ret, y + solve(1 - tower, floor + dir))
                if (dir > 0 and tower == 1) or (dir < 0 and tower == 0):
                    ret = min(ret, x + y + solve(1 - tower, floor + dir))
            dp[tower][floor] = ret
    return dp[tower][floor]


print(solve(0, a))
