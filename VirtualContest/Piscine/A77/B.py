# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n = int(input())
c = [0, 0, 0, 0]
a = list(map(int, input().split()))
for item in a:
    c[item] += 1

dp = [
    [[-1 for _ in range(c[3] + 1)] for _ in range(c[2] + c[3] + 1)]
    for _ in range(n + 1)
]


def solve(tar_1, tar_2, tar_3):
    if dp[tar_1][tar_2][tar_3] == -1:
        sm = tar_1 + tar_2 + tar_3
        if sm == 0:
            dp[tar_1][tar_2][tar_3] = 0
        else:
            dp[tar_1][tar_2][tar_3] = n / sm
            if tar_1 > 0:
                dp[tar_1][tar_2][tar_3] += (tar_1 / sm) * solve(tar_1 - 1, tar_2, tar_3)
            if tar_2 > 0:
                dp[tar_1][tar_2][tar_3] += (tar_2 / sm) * solve(
                    tar_1 + 1, tar_2 - 1, tar_3
                )
            if tar_3 > 0:
                dp[tar_1][tar_2][tar_3] += (tar_3 / sm) * solve(
                    tar_1, tar_2 + 1, tar_3 - 1
                )
    return dp[tar_1][tar_2][tar_3]


print(solve(c[1], c[2], c[3]))
