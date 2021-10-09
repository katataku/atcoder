# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

w, k, d = map(int, input().split())

if k <= d and (w - k) <= d:
    print("Yes")
else:
    print("No")
