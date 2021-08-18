# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, k = map(int, input().split())

d_calc_y = {}


def calc_y(n):
    if n not in d_calc_y:
        if n == 0:
            d_calc_y[n] = 0
        else:
            d_calc_y[n] = (n % 10) + calc_y(n // 10)
    return d_calc_y[n]


d_ans = {}


def solve(n, k):
    if n not in d_ans:
        d_ans[n] = ((n + calc_y(n)) % 100000, k)
    else:
        tmp_n, tmp_k = d_ans[n]
        k %= tmp_k - k
    tmp, _ = d_ans[n]
    if k == 0:
        return tmp
    else:
        return solve(tmp, k - 1)


ans1 = solve(n, k - 1)
print(ans1)
