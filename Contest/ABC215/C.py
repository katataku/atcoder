# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

s, k = input().split()
k = int(k)
length = len(s)
s = list(s)
s.sort()

cnt = 1
d = {}
for item in itertools.permutations(s, length):
    item = "".join(map(str, (list(item))))
    if item not in d:
        if cnt == k:
            print(item)
            break
        else:
            cnt += 1
        d[item] = True
