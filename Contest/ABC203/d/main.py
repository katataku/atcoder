# -*- coding: utf-8 -*-
# Input#
import statistics

# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
import copy

from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

ans = MOD
n, k = map(int, input().split())

alist = []


for i in range(n):
    a = list(map(int, input().split()))
    alist.append(a)


memo_i = [[[] for i in range(n)] for j in range(n)]
memo_med = [[[] for i in range(n)] for j in range(n)]
ans = MOD


for i in range(n):
    for j in range(n):
        if j == 0:
            memo_i[i][j] = [alist[i][j]]
        else:
            memo_i[i][j] = copy.deepcopy(memo_i[i][j - 1])
            memo_i[i][j].append(alist[i][j])

            if len(memo_i[i][j]) > k:
                startpos = len(memo_i[i][j]) - k
                memo_i[i][j] = memo_i[i][j][startpos:]

        if i == 0:
            memo_med[i][j] = memo_i[i][j]
        else:
            memo_med[i][j] = copy.deepcopy(memo_med[i - 1][j])
            memo_med[i][j].extend(memo_i[i][j])
            if len(memo_med[i][j]) > k * k:
                startpos = len(memo_med[i][j]) - k * k
                memo_med[i][j] = memo_med[i][j][startpos:]

        if i > k - 2 and j > k - 2:
            ans = min(
                ans,
                int(
                    statistics.median_low(memo_med[i][j]),
                ),
            )


print(ans)
