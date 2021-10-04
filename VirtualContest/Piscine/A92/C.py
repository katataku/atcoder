# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n = int(input())
h = []
heapq.heapify(h)

for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(h, (b, a))

ans = "Yes"
current = 0
while (len(h)) > 0:
    tar_b, tar_a = heapq.heappop(h)
    current += tar_a
    if current > tar_b:
        ans = "No"
        break

print(ans)
