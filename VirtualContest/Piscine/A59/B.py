# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, k, p = map(int, input().split())
a = list(map(int, input().split()))


def solve(index, acc_p, acc_k):
    ret = 0
    if index == n:
        if acc_k == k:
            return 1
        else:
            return 0

    ret += solve(index + 1, acc_p, acc_k)
    if acc_p + a[index] <= p and acc_k < k:
        ret += solve(index + 1, acc_p + a[index], acc_k + 1)
    return ret


print(solve(0, 0, 0))
