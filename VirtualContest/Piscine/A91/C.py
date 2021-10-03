# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = [0 for i in range(n + 1)]
for item in a:
    cnt[item] += 1

h = []
heapq.heapify(h)
for i in range(n + 1):
    if cnt[i] > 0:
        heapq.heappush(h, (cnt[i], i))

ans = 0
while len(h) > k:
    tar_cnt, _ = heapq.heappop(h)
    ans += tar_cnt
print(ans)