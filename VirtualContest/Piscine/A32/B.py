# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
l, r = map(int, input().split())


def func(n):
    return n * (n + 1) // 2


def solve(degit):
    global l
    global r
    return func(min(10 ** degit - 1, r)) - func(max(10 ** (degit - 1), l) - 1)


ans = 0
for i in range(1, 20):
    if 10 ** (i) >= l:
        ans += solve(i) * i
        if 10 ** i > r:
            break

print(ans % MOD)
