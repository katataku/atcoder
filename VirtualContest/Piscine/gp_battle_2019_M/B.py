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

if s == "AtCoder":
    ans = "Yes"
elif s.lower() == "atcoder":
    ans = "Maybe"
else:
    ans = "No"
print(ans)