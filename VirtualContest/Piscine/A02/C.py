# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n = int(input())

a_list = list(map(int, input().split()))

ans = 0
a_list.sort(reverse=True)

ans += a_list[0]
d = deque()
d.append((a_list[0], a_list[1]))
d.append((a_list[0], a_list[1]))

for i in range(2, n):
    a, b = d.popleft()
    ans += min(a, b)
    d.append((max(a, b), a_list[i]))
    d.append((min(a, b), a_list[i]))

print(ans)