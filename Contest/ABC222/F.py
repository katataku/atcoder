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
path = [[] for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    path[u].append(v)
    path[v].append(u)


def dfs(node):
    global deepest_leaf
    global deepest_level
    for next in path[node]:
        if level[next] == -1:
            level[next] = level[node] + 1
            is_leaf[node] = False
            if level[next] > deepest_level:
                deepest_level = level[next]
                deepest_leaf = next
            dfs(node)


dist = [{} for i in range(n)]

level = [-1 for i in range(n)]
is_leaf = [True for i in range(n)]
level[0] = 0
deepest_leaf = -1
deepest_level = -1
dfs(0)


level = [-1 for i in range(n)]
is_leaf = [True for i in range(n)]
level[deepest_leaf] = 0
deepest_leaf = -1
deepest_level = -1
dfs(deepest_leaf)


diameter = deepest_level
ans = 0
for item in level:
    if item == diameter:
        ans += 1

print(ans % MOD)
