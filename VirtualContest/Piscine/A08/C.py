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
b = list(map(int, input().split()))


ans = -1
if sum(a) >= sum(b):
    ans = 0
    c = []
    for a_item, b_item in zip(a, b):
        c.append(a_item - b_item)
    c.sort()
    credit = 0
    while len(c) > 0:
        tar = c.pop(0)
        if tar >= 0:
            break
        else:
            tar *= -1
            ans += 1
            if tar > credit:
                ans += 1
                credit += c.pop(-1)
            credit -= tar


print(ans)