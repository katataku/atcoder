# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n = list(input())
n.sort(reverse=True)

ans = 0
for item_list in itertools.product([True, False], repeat=len(n)):
    a = 0
    b = 0
    for i in range(len(n)):
        if item_list[i]:
            a *= 10
            a += int(n[i])
        else:
            b *= 10
            b += int(n[i])
    ans = max(ans, a * b)
print(ans)
