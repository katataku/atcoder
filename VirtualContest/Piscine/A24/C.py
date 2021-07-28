# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n = int(input())

a, b, c = map(int, input().split())

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

INF = 10 ** 10
ans = 0
memo = {}
ans = INF
for i in range(10000):
    if n < i * c:
        break
    for j in range(10000 - i):
        if n < i * c + j * b:
            break
        if (n - c * i - b * j) % a == 0:
            k = (n - c * i - b * j) // a
            ans = min(i + j + k, ans)


print(ans)