# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque
from typing import AnyStr

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

w, n = map(int, input().split())
h = []
d = {}
for i in range(n):
    l, r, v = map(int, input().split())
    d[v] = (l, r - l)
    h.append(v)
h.sort(reverse=True)


def solve(acc_min, acc_buf, acc_value, index):
    ret = -1
    if len(h) > index:
        tar = h[index]
        index += 1
        ret = max(ret, solve(acc_min, acc_buf, acc_value, index))
        tar_min, tar_buf = d[tar]
        acc_min += tar_min
        acc_buf += tar_buf
        acc_value += tar
        if acc_min <= w:
            ret = max(ret, solve(acc_min, acc_buf, acc_value, index))
        if acc_min <= w <= acc_min + acc_buf:
            ret = max(acc_value, ret)

    return ret


print(solve(0, 0, 0, 0))
