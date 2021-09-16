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

ans = 1
a.sort()
for item in a:
    ans *= item
    if ans > 10 ** 18:
        ans = -1
        break
print(ans)
