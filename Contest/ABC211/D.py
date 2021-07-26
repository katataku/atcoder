# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
import copy
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, m = map(int, input().split())

memo = [[-1 for i in range(n)] for j in range(n)]
d1 = deque()
dic = {}
cnt = [0 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    memo[a - 1][b - 1] = 1
    memo[b - 1][a - 1] = 1
    if a - 1 in dic.keys():
        dic[a - 1].append(b - 1)
    else:
        dic[a - 1] = [b - 1]
    if b - 1 in dic.keys():
        dic[b - 1].append(a - 1)
    else:
        dic[b - 1] = [a - 1]

    if a == 1:
        d1.append(b - 1)

ans = 0
while len(d1) > 0:
    tar = d1.popleft()
    memo[tar][tar] = 0
    for i in dic[tar]:
        if memo[0][i] == -1:
            memo[0][i] = memo[0][tar] + memo[tar][i]
            if memo[0][n - 1] == -1:
                d1.append(i)
            cnt[i] += cnt[tar]
ans = cnt[n - 1]
print(ans % MOD)
