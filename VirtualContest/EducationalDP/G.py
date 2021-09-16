# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n, m = map(int, input().split())

path = {}
path_rev = {}


for i in range(m):
    x, y = map(int, input().split())
    path[x] = path.get(x, [])
    path_rev[y] = path_rev.get(y, [])
    path[x].append(y)
    path_rev[y].append(x)


dp = {}


def dfs(node):
    global path
    if node not in dp:
        dp[node] = 0
        for next in path.get(node, []):
            dp[node] = max(1 + dfs(next), dp[node])
    return dp[node]


ans = 0
for i in range(1, n + 1):
    if dfs(i) > ans:
        ans = dfs(i)

print(ans)
