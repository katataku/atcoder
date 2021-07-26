# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

n = int(input())
h = list(map(int, input().split()))

m = -1
ans = 0
for i in range(n):
    if m <= h[i]:
        ans += 1
    m = max(m, h[i])
print(ans)