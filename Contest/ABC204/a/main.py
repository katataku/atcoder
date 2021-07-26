# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
ans = 0
a, b = map(int, input().split())
if a == b:
    ans = a
else:
    ans = 3 - a - b
print(ans)
