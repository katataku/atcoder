# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n = int(input())

c = list(map(int, input().split()))


def sol(c, min_num):
    if len(c) == 1:
        return max(c[0] - min_num + 1, 0)
    else:
        if c[0] < min_num:
            return 0
        else:
            return sol(c[1:], min_num + 1) + sol(c, min_num + 1)


print(sol(c, 1))
