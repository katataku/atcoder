# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

c = []
h, w, k = map(int, input().split())

for i in range(h):
    s = input()
    c.append(s)

ans = 0
ans_list = []
for h_list in itertools.product([True, False], repeat=h):
    for w_list in itertools.product([True, False], repeat=w):
        acc = 0
        for i in range(h):
            for j in range(w):
                if not h_list[i] and not w_list[j] and c[i][j] == "#":
                    acc += 1
        if acc == k:
            ans += 1
            ans_list.append((h_list, w_list))

print(ans)