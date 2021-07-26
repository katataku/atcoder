# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n = int(input())
a = list(map(int, input().split()))


ans1 = max(a)
ans2 = 0
abs_num = max(a)

for i in a:
    if abs_num > abs((ans1 / 2) - i) and i != ans1:
        abs_num = abs((ans1 / 2) - i)
        ans2 = i

print(str(ans1) + " " + str(ans2))
