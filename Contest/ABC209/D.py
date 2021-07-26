# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

INF = 10 ** 10
n, q = map(int, input().split())

dist = [[INF for i in range(n)] for j in range(n)]

for i in range(n):
    dist[i][i] = 0

d = deque()

for i in range(n - 1):
    a, b = map(int, input().split())
    dist[a - 1][b - 1] = 1
    dist[b - 1][a - 1] = 1
    if a == 1:
        d.append(b - 1)


def get_dist(src, dest):
    dist[src][dest] = min(dist[src][dest], dist[dest][src])
    dist[dest][src] = min(dist[src][dest], dist[dest][src])
    return dist[src][dest]


def bfs(src, dest):
    if get_dist(src, dest) != INF:
        return dist[src][dest]
    while len(d) > 0:
        tar = d.popleft()
        for i in range(n):
            if get_dist(i, tar) != INF and get_dist(0, i) == INF:
                dist[0][i] = get_dist(0, tar) + get_dist(i, tar)
                d.append(i)
    return get_dist(src, dest)


for i in range(q):
    src, dest = map(int, input().split())
    src -= 1
    dest -= 1
    while True:
        if bfs(0, src) != INF and bfs(0, dest) != INF:
            break
    if (get_dist(src, 0) + get_dist(dest, 0)) % 2 == 0:
        print("Town")
    else:
        print("Road")
