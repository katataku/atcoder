# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque
import copy

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10
n, p, k = map(int, input().split())

mp = []
dist_master = [[INF for i in range(n)] for j in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    mp.append(a)

for i in range(n):
    dist_master[i][i] = 0
    for j in range(n):
        if mp[i][j] != 0:
            dist_master[i][j] = mp[i][j]


def solve(x):
    dist = copy.deepcopy(dist_master)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1:
                dist[i][j] = x
            for k in range(n):
                if dist[i][j] >= k:
                    tmp = True
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                if tmp and dist[i][j] < k:
                    cnt += 1
    return cnt


left = 0
right = n

while right - left > 1:
    mid = (right + left) // 2
    if solve(mid) <= k:
        left = mid
    else:
        right = mid

print(left)