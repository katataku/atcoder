# -*- coding: utf-8 -*-
from functools import reduce
import math

n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    if a[i] in d.keys():
        d[a[i]] += 1
    else:
        d[a[i]] = 1

ans = n * (n - 1) / 2
for tar in d.keys():
    if d[tar] > 1:
        ans = ans - (d[tar] * (d[tar] - 1) / 2)

print(int(ans))