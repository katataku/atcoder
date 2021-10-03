# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 998244353
INF = 10 ** 10

ans = 0

n = int(input())
a = list(map(int, input().split()))

h = []
heapq.heapify(h)

for item in a:
    heapq.heappush(h, item)

d_a = {}
acc = 1
while (len(h)) > 0:
    tar = heapq.heappop(h)
    if tar not in d_a:
        d_a[tar] = acc
        acc += 1

ans = 0
d = [0 for i in range(len(d_a))]
for i in range(n - 1, -1, -1):
    if i != n - 1:
        cnt = 0
        for i in range(len(d_a)):
            
    d[d_a[a[i]]] += 1

print(d_a)
print(ans % MOD)