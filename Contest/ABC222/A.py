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

l = len(str(n))
ans = "0" * (4 - l)
ans += str(n)

print(ans)
