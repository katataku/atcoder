# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

h, w = map(int, input().split())


s = []

s.append(["#" for i in range(w + 2)])

start_pos = (-1, -1)
for i in range(h):
    s.append(list(input()))
    s[i + 1].insert(0, "#")
    if "." in s[i + 1]:
        start_pos = (i + 1, s[i + 1].index("."))
    s[i + 1] += "#"
s.append(["#" for i in range(w + 2)])

max_pos = (-1, -1)
