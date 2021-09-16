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

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

index_a = 0
index_b = 0
index_c = 0
ans = 0
while index_a < n and index_b < n and index_c < n:
    if a[index_a] >= b[index_b]:
        index_b += 1
    else:
        if b[index_b] >= c[index_c]:
            index_c += 1
        else:
            ans += 1
            index_a += 1
            index_b += 1
            index_c += 1
print(ans)
