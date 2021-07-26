# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, m = map(int, input().split())

a = list(map(int, input().split()))

d = {}
ans = "?"

for i in a:
    if i in d.keys():
        d[i] += 1
        if d[i] > n // 2:
            ans = i
            break
    else:
        d[i] = 1

print(ans)