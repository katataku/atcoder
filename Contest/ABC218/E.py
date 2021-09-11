# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10
n, m = map(int, input().split())

parent = [i for i in range(n)]


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(a, b):
    tar = min(find(a), find(b))
    parent[find(a)] = tar
    parent[find(b)] = tar


path = [{} for j in range(n + 1)]
all_cost = 0

h = []
heapq.heapify(h)

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    heapq.heappush(h, (c, a, b))
    all_cost += c

visitid = {}
visitid_cost = 0

while len(h) > 0:
    tar_cost, a, b = heapq.heappop(h)
    if tar_cost <= 0:
        union(a, b)
        visitid_cost += tar_cost
    else:
        if find(a) != find(b):
            union(a, b)
            visitid_cost += tar_cost


print(all_cost - visitid_cost)
