# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
from typing import Dict


n, m = map(int, input().split())

path = {}
rev_path = {}

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    path[a] = path.get(a, [])
    path[a].append(b)
    rev_path[b] = rev_path.get(b, [])
    rev_path[b].append(a)


def dfs(node):
    used[node] = True
    for next in path.get(node, []):
        if next not in used:
            dfs(next)
    vs.append(node)


def rdfs(node, k):
    used[node] = True
    cmp[k].append(node)
    for next in rev_path.get(node, []):
        if next not in used:
            rdfs(next, k)


vs = []
used = {}
for i in range(n):
    if i not in used:
        dfs(i)

used = {}
vs.reverse()
cmp = {}
k = 0
for node in vs:
    if node not in used:
        cmp[k] = []
        rdfs(node, k)
        k += 1

ans = 0
for key, value in cmp.items():
    value = len(value)
    if value > 1:
        ans += value * (value - 1) // 2

print(ans)
