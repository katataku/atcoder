# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
k = int(input())

MOD = 10 ** 9 + 7
d = {}


def solve(acc):
    global k
    if acc not in d:
        if k == acc:
            d[acc] = 1
        elif acc > k:
            d[acc] = 0
        else:
            ret = 0
            for i in range(1, 10):
                ret += solve(acc + i)
            d[acc] = ret % MOD
    return d[acc]


ans = 0
if k % 9 == 0:
    ans = solve(0)

print(ans)