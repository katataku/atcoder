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
a.sort()

if a[-1] < sum(a[:-1]):
    print("Yes")
else:
    print("No")