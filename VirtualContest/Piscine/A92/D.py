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

ans = 0
for i in range(k, n + 2):
    low = (i + 1) * (i) // 2
    up = (n + 2) * (n + 1) // 2 - (n + 2 - i) * (n + 1 - i) // 2
    assert up >= low
    ans += up - low + 1

print(ans % MOD)
