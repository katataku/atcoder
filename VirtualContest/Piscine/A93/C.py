# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

a, b, c = map(int, input().split())

tar = math.sqrt(a * b)
if c - a - b > 0 and 4 * a * b < (c - a - b) ** 2:
    print("Yes")
else:
    print("No")