# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

n, m, t, k = map(int, input().split())
path = [{} for _ in range(n + 1)]

for i in range(m):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    path[a][b] = path[a].get(b, [])
    path[b][a] = path[b].get(a, [])

    path[a][b].append((c, d))
    path[b][a].append((c, d))


min_arrived = [INF for i in range(n)]


def dfs(node, time):
    if min_arrived[node] > time:
        min_arrived[node] = time
        if node != n - 1:
            for next, packed_list in path[node].items():
                for c, d in packed_list:
                    wait_time = 0
                    if k >= d:
                        while True:
                            cur_time = min_arrived[node] + wait_time
                            if k >= d - abs(t - cur_time) and k >= d - abs(
                                t - cur_time - 1
                            ):
                                break
                            wait_time += (
                                d - abs(t - min_arrived[node] - wait_time)
                            ) - k
                            if wait_time == 0:
                                wait_time += 1
                        dfs(next, min_arrived[node] + wait_time + c)


dfs(0, 0)
if min_arrived[n - 1] == INF:
    print(-1)
else:
    print(min_arrived[n - 1])
