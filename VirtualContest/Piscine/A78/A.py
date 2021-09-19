# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10
n, d = map(int, input().split())
x_list = []

for i in range(n):
    a = list(map(int, input().split()))
    x_list.append(a)

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        acc = 0
        for ind in range(d):
            acc += (x_list[i][ind] - x_list[j][ind]) ** 2
        acc = math.sqrt(acc)
        if acc.is_integer():
            ans += 1
print(ans)
