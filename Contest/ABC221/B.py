# -*- coding: utf-8 -*-
import math
import heapq
import itertools
from collections import deque
import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 10

s = input()
t = input()
cnt = 0

ans = "Yes"

flag = False
for i in range(len(s)):
    if s[i] != t[i] and not flag:
        if i == len(s) - 1 or s[i] != t[i + 1] or s[i + 1] != t[i]:
            ans = "No"
            break
        else:
            flag = True
            continue
    flag = False
print(ans)
