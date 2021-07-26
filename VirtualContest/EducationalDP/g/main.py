# -*- coding: utf-8 -*-
from collections import deque

from sys import setrecursionlimit

setrecursionlimit(1000000)

INF = float("inf")
# Input#
# n = int(input())
n, m = map(int, input().split())
# a = list(map(int, input().split()))

d = deque()
d_tmp = deque()
x = [-1]
y = [[-1] for _ in range((n + 1))]

for _ in [0] * m:
    x_in, y_in = map(int, input().split())
    #    x.append(x_in)
    y[x_in].append(y_in)
    d.append((x_in, y_in))

memo = [-1] * (n + 1)
ans = -1


def dp(i):
    global ans
    if memo[i] == -1:
        ret = 0
        for x_in in y[i][1:]:
            tmp = dp(x_in) + 1
            if tmp > ret:
                ret = tmp
        memo[i] = ret
        if ret > ans:
            ans = ret
        return ret
    else:
        return memo[i]


for i, _ in d:
    if memo[i] == -1:
        dp(i)

print("{}".format(ans))
