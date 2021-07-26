# -*- coding: utf-8 -*-
# from collections import deque
from sys import setrecursionlimit

setrecursionlimit(1000000)


# INF = float("inf")

# d = deque()
# ---Input---#
n = int(input())
# n, k = map(int, input().split())
p = list(map(float, input().split()))
p = [-1] + p

memo = [[-1 for _ in [0] * (n + 1)] for _ in [0] * (n + 1)]
memo[0][0] = 1
for i in range(len(p))[1:]:
    memo[0][i] = 0
    memo[i][0] = memo[i - 1][0] * (1 - p[i])
memo[0][0] = 1


def dp(i, j):
    if memo[i][j] == -1:
        memo[i][j] = dp(i - 1, j) * (1 - p[i]) + dp(i - 1, j - 1) * p[i]
    return memo[i][j]


ans = 0
tar = int(n / 2) + 1
for i in range(n + 1):
    dp(i, i)
    dp(i, n)

for i in range(n + 1)[tar:]:
    ans += dp(n, i)


print("{}".format(ans))
