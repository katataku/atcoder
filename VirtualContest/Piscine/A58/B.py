# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
n = int(input())

path = {}
path_list = []
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    path[a] = path.get(a, [])
    path[b] = path.get(b, [])
    path[a].append(b)
    path[b].append(a)
    path_list.append((a, b))


dp = {}


def dfs(node, pre):
    dp[node] = 1
    for next in path[node]:
        if next != pre:
            dfs(next, node)
            dp[node] += dp[next]


dfs(0, -1)

ans = 0
for a, b in path_list:
    tar_a = dp[a]
    tar_b = dp[b]
    if tar_a > tar_b:
        tar_a, tar_b = tar_b, tar_a
    ans += tar_a * (n - tar_a)

print(ans)