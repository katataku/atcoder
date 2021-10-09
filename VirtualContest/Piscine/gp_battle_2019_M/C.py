# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n, m = map(int, input().split())

d = {}
for i in range(n):
    a, b = map(int, input().split())
    tar = i + 1 - a - b
    if m >= tar > 0:
        d[tar] = True

print(len(d))
