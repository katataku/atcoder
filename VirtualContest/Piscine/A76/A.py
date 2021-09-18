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
s = list(input())
q = int(input())

flipped = False

for i in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if flipped:
            if a < n:
                a += n
            else:
                a -= n
            if b < n:
                b += n
            else:
                b -= n
        s[a], s[b] = s[b], s[a]
    else:
        flipped = not flipped

if not flipped:
    print("".join(s))
else:
    print("".join(s[n:] + s[:n]))
