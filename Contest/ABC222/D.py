# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 998244353
INF = 10 ** 10

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[-1 for i in range(b[n - 1] + 1)] for _ in range(n)]


def solve(index, pre):
    if dp[index][pre] == -1:
        ans = 0
        if index == n - 1:
            if pre <= a[index]:
                ans = b[index] - a[index] + 1
            else:
                ans = b[index] - pre + 1
        else:
            if pre < a[index]:
                ans = solve(index, a[index])
            else:
                ans = solve(index + 1, pre)
                if pre != b[index]:
                    ans += solve(index, pre + 1)
        dp[index][pre] = ans % MOD
    return dp[index][pre]


for i in range(n - 1, 0, -1):
    solve(i, b[i])


print(solve(0, 0))
