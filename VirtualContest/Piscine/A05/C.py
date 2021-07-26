# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


l, r = map(int, input().split())

d_l = deque()
d_r = deque()

for i in range(min(2019, r - l + 1)):
    if l + i != r:
        d_l.append((l + i) % 2019)
    if i != 0:
        d_r.append((l + i) % 2019)

ans = 2020

for l_item in d_l:
    for r_item in d_r:
        ans = min(ans, (l_item * r_item) % 2019)

print(ans)