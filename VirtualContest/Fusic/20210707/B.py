# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n = int(input())

w = list(map(int, input().split()))

s1 = 0
s2 = 0
while len(w) > 0:
    if s1 >= s2:
        s2 += w.pop(-1)
    else:
        s1 += w.pop(0)


diff = abs(s1 - s2)

print(diff)
