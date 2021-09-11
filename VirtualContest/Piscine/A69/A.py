# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for i in range(a + 1):
    if 500 * i > x:
        break
    for j in range(b + 1):
        if 100 * j > x:
            break
        for k in range(c + 1):
            if (x - (500 * i) - (100 * j) - (50 * k)) == 0:
                ans += 1

print(ans)
