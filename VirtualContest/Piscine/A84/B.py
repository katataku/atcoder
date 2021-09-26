# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n, m, q = map(int, input().split())

path = [{} for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    path[a][b] = c
    path[b][a] = c

x = list(map(int, input().split()))

visitid = [False for i in range(n)]
visitid[0] = True
ans = 1
d = deque()

h = []
heapq.heapify(h)


def add_heap(node):
    for next, cost in path[node].items():
        if not visitid[next]:
            heapq.heappush(h, (cost, next))


add_heap(0)
for day in range(q):
    while len(h) > 0:
        cost, next = heapq.heappop(h)
        if cost <= x[day]:
            if not visitid[next]:
                d.append(next)
        else:
            heapq.heappush(h, (cost, next))
            break

    while len(d) > 0:
        tar = d.popleft()
        if not visitid[tar]:
            visitid[tar] = True
            ans += 1
            add_heap(tar)

    print(ans)
