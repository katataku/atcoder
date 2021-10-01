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
t, a = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
diff = INF
for i in range(n):
    tmp = abs(a - (t - x[i] * 0.006))
    if diff > tmp:
        ans = i + 1
        diff = tmp
print(ans)
