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

b = [0]
for i in range(n):
    item = a[i]
    if i > 0:
        b.append(b[-1] + item)
    else:
        b.append(item)

b.sort()
d = {}
for item in b:
    d[item] = d.get(item, 0) + 1

ans = 0
for key, value in d.items():
    if value > 1:
        ans += (value) * (value - 1) // 2
    else:
        if key == 0:
            ans += math.factorial(value)

print(d)
print(ans)