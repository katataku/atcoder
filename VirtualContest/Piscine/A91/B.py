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

acc_left = 0
acc_right = 0
left = 0
right = n - 1

while left <= right:
    if acc_left < acc_right:
        acc_left += a[left]
        left += 1
    else:
        acc_right += a[right]
        right -= 1

print(abs(acc_left - acc_right))
