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
a = list(map(int, input().split()))

flag = {}
ans = "YES"
for item in a:
    if item in flag:
        ans = "NO"
        break
    else:
        flag[item] = True
print(ans)