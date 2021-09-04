# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
import bisect

n = int(input())
l_list = [0 for i in range(n)]
r_list = [0 for i in range(n)]

for i in range(n):
    t, l, r = map(int, input().split())
    if t == 2 or t == 4:
        r -= 0.5
    if t == 3 or t == 4:
        l += 0.5
    l_list[i] = l
    r_list[i] = r

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans += max(l_list[i], l_list[j]) <= min(r_list[i], r_list[j])

print(ans)