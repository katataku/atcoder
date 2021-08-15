# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
t = int(input())


for _ in range(t):
    n = int(input())
    d = {}
    ans = "Yes"
    h_q_l = []
    h_q_r = []
    heapq.heapify(h_q_l)
    d = {}
    heapq.heapify(h_q_r)
    for i in range(n):
        l, r = map(int, input().split())
        heapq.heappush(h_q_l, l)
        d[l] = d.get(l, [])
        d[l].append(r)

    print(ans)
