# -*- coding: utf-8 -*-
from functools import reduce
import math

n, m = map(int, input().split())

anslist = [[i] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    anslist[a].append(b)

flag = True

while flag:
    flag = False
    for src in range(n):
        for tar in anslist[src]:
            if set(anslist[tar]) - set(anslist[src]) != {}:
                flag = True
                anslist[src] += anslist[tar]
                anslist[src] = list(set(anslist[src]))

ans = 0
for i in range(n):
    ans += len(set(anslist[i]))

print(ans)