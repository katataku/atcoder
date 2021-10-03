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
ans = 0
if n % 2 == 0:
    ans = (n // 2) ** 2
else:
    ans = (n // 2) * (n // 2 + 1)

print(ans)
