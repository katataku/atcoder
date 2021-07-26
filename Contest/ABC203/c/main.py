# -*- coding: utf-8 -*-
from functools import reduce
import math

n, k = map(int, input().split())


d = {}
alist = []
for i in range(n):
    a, b = map(int, input().split())
    if a in d.keys():
        d[a] += b
    else:
        d[a] = b
        alist.append(a)

alist.sort()

ans = 0
rest = k
pos = 0
for i in range(len(alist)):
    if pos + rest < alist[i]:
        ans = pos + rest
        rest = 0
        break
    else:
        rest += d[alist[i]]
        rest -= alist[i] - pos
        pos = alist[i]
        ans = pos

if rest > 0:
    ans += rest
print(ans)
