# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

n, l = map(int, input().split())

diff = l

ans = 0
for i in range(1, n):
    tar = l + i
    if max(diff, diff * -1) > max(tar, tar * -1):
        ans += diff
        diff = tar
    else:
        ans += tar
print(ans)