# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

n, k = map(int, input().split())

h = list(map(int, input().split()))
h.sort()

ans = 0
cnt = 0
max_cnt = 1
while cnt < k:
    if len(h) == 0:
        break
    tar = h.pop(-1)
    next = 0
    if len(h) != 0:
        next = h[-1]
    diff = tar - next
    if cnt + (max_cnt * diff) <= k:
        tmp = diff * (diff + 1) // 2
        tmp += diff * next
        tmp *= max_cnt
        ans += tmp
        cnt += max_cnt * diff
    else:
        diff = (k - cnt) // max_cnt
        tmp = diff * (diff + 1) // 2
        tmp += diff * (tar - diff)
        tmp *= max_cnt
        ans += tmp
        cnt += max_cnt * diff
        tar -= diff
        while next != tar and cnt < k:
            if cnt + max_cnt <= k:
                ans += tar * max_cnt
            else:
                ans += tar * (k - cnt)
            cnt += max_cnt
            tar -= 1
    max_cnt += 1
    if tar == 0:
        break

print(ans)
