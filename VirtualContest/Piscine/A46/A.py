# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
h, w = map(int, input().split())

mp = []
for i in range(h):
    a = list(map(int, input().split()))
    mp.append(a)

ans = 0
for item in itertools.product("01", repeat=h):
    item = list(item)
    tmp_mp = []
    for i in range(len(item)):
        if item[i] == "1":
            tmp_mp.append(mp[i])
    R = []
    d = {}
    if len(tmp_mp) > 0:
        for j in range(w):
            flag = True
            tar = tmp_mp[0][j]
            for i in range(len(tmp_mp)):
                if tar != tmp_mp[i][j]:
                    flag = False
                    break
            if flag:
                R.append(tar)
                d[tar] = d.get(tar, 0)
                d[tar] += 1
                ans = max(ans, d[tar] * len(tmp_mp))
print(ans)
