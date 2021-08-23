# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
n, k = map(int, input().split())

s = input()

c = [{} for j in range(len(s) + 1)]

for i in range(26):
    c[n][i] = -1
for i in range(len(s)):
    i = len(s) - i - 1
    for alphabet in range(26):
        if ord(s[i]) - 97 == alphabet:
            c[i][alphabet] = i
        else:
            c[i][alphabet] = c[i + 1][alphabet]


def solve(n, acc):
    for i in range(26):
        if -1 != c[n][i] and len(s) - (c[n][i]) + acc >= k and acc + 1 <= k:
            ans = chr(97 + i) + solve(c[n][i] + 1, acc + 1)
            return ans
    return ""


print(solve(0, 0))
