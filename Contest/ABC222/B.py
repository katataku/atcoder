# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10
n, p = map(int, input().split())

a = list(map(int, input().split()))

ans = 0
for item in a:
    if item < p:
        ans += 1

print(ans)