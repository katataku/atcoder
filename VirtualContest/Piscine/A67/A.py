# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(100000000)
MOD = 10 ** 9 + 7

k, a, b = map(int, input().split())


if b - a <= 2 or a >= k:
    print(1 + k)
else:
    k -= a - 1
    print(a + (b - a) * (k // 2) + k % 2)
