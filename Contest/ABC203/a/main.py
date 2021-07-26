# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
ans = 0
a, b, c = map(int, input().split())
if a == b:
    ans = c
if a == c:
    ans = b
if b == c:
    ans = a

print(ans)
