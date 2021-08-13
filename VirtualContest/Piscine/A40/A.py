# -*- coding: utf-8 -*-
import math
import heapq
import sys
import itertools
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
n = int(input())

d = {}
d_path = {}
q = deque()


for i in range(n - 1):
    a, b = map(int, input().split())
    d_path[a] = d_path.get(a, [])
    d_path[a].append(b)
    d_path[b] = d_path.get(b, [])
    d_path[b].append(a)
d[a] = 0
d[b] = 1
cnt = {0: 1, 1: 1}
ans = [a]
ans1 = [b]
q.append(a)
q.append(b)


while len(q) > 0:
    tar = q.popleft()
    for b in d_path[tar]:
        a = tar
        if b not in d:
            d[b] = 1 - d[a]
            cnt[d[b]] += 1
            if d[b] == 0:
                ans.append(b)
            else:
                ans1.append(b)
            q.append(b)
    if cnt[0] >= n // 2 or cnt[1] >= n // 2:
        break

if len(ans1) >= n // 2:
    ans = ans1


print(" ".join(map(str, ans[: n // 2])))
