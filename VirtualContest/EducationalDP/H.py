# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

mp = []
h, w = map(int, input().split())
for i in range(h):
    a = input()
    mp.append(a)

dp = [{} for i in range(h)]
dp[0][0] = 1


def solve(tar_h, tar_w):
    if tar_w not in dp[tar_h]:
        if mp[tar_h][tar_w] == "#":
            dp[tar_h][tar_w] = 0
        else:
            dp[tar_h][tar_w] = 0
            if tar_h > 0:
                dp[tar_h][tar_w] += solve(tar_h - 1, tar_w)
            if tar_w > 0:
                dp[tar_h][tar_w] += solve(tar_h, tar_w - 1)
            dp[tar_h][tar_w] %= MOD
    return dp[tar_h][tar_w]


print(solve(h - 1, w - 1))
