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

a.sort()
b = [a[0]]
for i in range(n - 1):
    b.append(b[-1] + a[i + 1])

ans = 0
for i in range(n - 1):
    ans += (b[-1] - b[i]) - a[i] * (n - i - 1)
print(ans)