# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

s = input()
t = input()

ans = len(t) + 1

for i in range(len(s) - len(t) + 1):
    tar_str = s[i : i + len(t)]
    tmp = 0
    for j in range(len(t)):
        if tar_str[j] != t[j]:
            tmp += 1
    ans = min(tmp, ans)
print(ans)