# -*- coding: utf-8 -*-

import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, m = map(int, input().split())

INF = 10 ** 10


path = {}
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    path[a] = path.get(a, {})
    path[b] = path.get(b, {})
    path[a][b] = c
    path[b][a] = c


for i in range(n):
    path[i][i] = 0


def dikstra(s):
    distlist = {s: 0}
    for key, value in path[s].items():
        distlist[key] = value
    h = []
    heapq.heapify(h)
    heapq.heappush(h, (0, s))
    visited = {}
    while len(visited) < n:
        cost, g = heapq.heappop(h)
        if g not in visited:
            visited[g] = True
            for next in path[g]:
                tmp = min(cost + path[g][next], distlist.get(next, INF))
                distlist[next] = tmp
                heapq.heappush(h, (tmp, next))
    return distlist


from0 = dikstra(0)
fromn = dikstra(n - 1)

for k in range(n):
    print(from0[k] + fromn[k])
