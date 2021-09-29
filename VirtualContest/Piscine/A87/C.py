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

ans = 0

ans += (1900 * m + 100 * (n - m)) * (2 ** m)
print(ans)