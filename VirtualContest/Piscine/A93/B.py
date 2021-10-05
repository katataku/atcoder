# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

a = list(map(int, input().split()))
a.sort()

ans = 0
ans += a[2] - a[1]
a[0] += ans
ans += (a[2] - a[0]) // 2
if (a[2] - a[0]) % 2 != 0:
    ans += 2
print(ans)