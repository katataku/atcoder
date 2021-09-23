# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

ans = 0
h = []
heapq.heapify(h)
for i in range(5):
    n = int(input())
    if n % 10 == 0:
        ans += n
    else:
        heapq.heappush(h, ((n % 10) * -1, n))

while len(h) > 0:
    _, tar = heapq.heappop(h)
    if len(h) == 0:
        ans += tar
    else:
        ans += (tar // 10) * 10 + 10

print(ans)