# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
n = int(input())

c = list((input().split()))
path = {}
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    path[a] = path.get(a, [])
    path[b] = path.get(b, [])
    path[a].append(b)
    path[b].append(a)

dp = [[0 for i in range(3)] for j in range(n)]


def dfs(node, pre):
    if pre != -1 and len(path[node]) == 1:
        if c[node] == "a":
            dp[node][0] = 1
        else:
            dp[node][1] = 1
    else:
        tmp_0 = 1
        tmp_1 = 1
        tmp_2 = 1
        for next in path[node]:
            if next != pre:
                dfs(next, node)
                if c[node] == "a":
                    tmp_0 *= dp[next][0] + dp[next][2]
                else:
                    tmp_1 *= dp[next][1] + dp[next][2]
                tmp_2 *= dp[next][0] + dp[next][1] + (dp[next][2] * 2)
        if c[node] == "a":
            dp[node][0] += tmp_0
            dp[node][2] += tmp_2 - dp[node][0]
        else:
            dp[node][1] += tmp_1
            dp[node][2] += tmp_2 - dp[node][1]


dfs(0, -1)
print(dp[0][2] % MOD)
